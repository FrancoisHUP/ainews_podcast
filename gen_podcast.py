import google.generativeai as genai

# Configure the Gemini API with your key
GOOGLE_API_KEY = "AIzaSyCwHrbWXzGAHq8TQ4Fs17"
genai.configure(api_key=GOOGLE_API_KEY)

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
