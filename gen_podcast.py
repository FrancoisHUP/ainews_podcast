import google.generativeai as genai
from dotenv import load_dotenv
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from pathlib import Path

load_dotenv()

MOCK = True

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

if not GEMINI_API_KEY and not MOCK:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Configure the Gemini API with your key
genai.configure(api_key=GEMINI_API_KEY)

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
RANGE_NAME = 'Sheet1!A1:B1'  # Adjust the range as needed

def authenticate_google_sheets():
    creds = None
    if Path('token.json').exists():
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def log_to_google_sheets(prompt, result):
    creds = authenticate_google_sheets()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    values = [[prompt, result]]
    body = {'values': values}
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body
    ).execute()

def generate_with_gemini(prompt, mock=False):

    if mock:
        mock_response = "MOCK RESPONSE"
        log_to_google_sheets("MOCK PROMPT", mock_response)
        return mock_response

    try:
        model = genai.GenerativeModel('gemini-exp-1206')
        response = model.generate_content(prompt)
        result_text = response.text
        log_to_google_sheets(prompt, result_text)
        return result_text
    except Exception as e:
        print(f"Error generating content: {e}")
        return None

if __name__ == "__main__":
    prompt = "Write a short podcast script about artificial intelligence"
    result = generate_with_gemini(prompt, mock=MOCK)
    if result:
        print(result)
