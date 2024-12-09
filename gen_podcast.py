import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Configure the Gemini API with your key
genai.configure(api_key=GEMINI_API_KEY)

def generate_with_gemini(prompt):
    """
    Make an API call to Gemini and return the response
    """
    model = genai.GenerativeModel('gemini-exp-1206')

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "Write a short podcast script about artificial intelligence"
    result = generate_with_gemini(prompt)
    if result:
        print(result)
