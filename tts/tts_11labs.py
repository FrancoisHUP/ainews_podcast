import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
API_KEY = os.getenv("ELEVENLABS_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in the .env file")

# Eleven Labs API endpoints
VOICES_URL = "https://api.elevenlabs.io/v1/voices"
TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech"

def fetch_available_voices():
    """
    Fetch available voices from the Eleven Labs API.

    Returns:
        list: A list of available voices with their details.
    """
    headers = {"xi-api-key": API_KEY}
    response = requests.get(VOICES_URL, headers=headers)

    if response.status_code == 200:
        voices = response.json().get("voices", [])
        # for voice in voices:
        #     print(f"Voice Name: {voice['name']}, Voice ID: {voice['voice_id']}")
        return voices
    else:
        print(f"Failed to retrieve voices: {response.status_code}, {response.text}")
        return []

def text_to_speech(text, output_file="output/output.mp3", voice_id=None):
    """
    Convert text to speech using Eleven Labs API.

    Args:
        text (str): The text to convert into speech.
        output_file (str): The filepath to save the generated audio.
        voice_id (str): The ID of the voice to use.
    """
    if not voice_id:
        raise ValueError("You must provide a valid voice_id.")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": API_KEY,
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,  # Adjust voice stability (0 to 1)
            "similarity_boost": 0.75,  # Adjust similarity boost (0 to 1)
        },
    }   
    return requests.post(f"{TTS_URL}/{voice_id}", json=payload, headers=headers)
    

# Example usage
if __name__ == "__main__":
    output_path = "data/output_sample.mp3"

    # Fetch available voices and pick one
    voices = fetch_available_voices()
    if voices:
        selected_voice_id = voices[0]["voice_id"]  # Use the first available voice

        # Example dialogue
        dialogue = """
        Hello! Welcome to our service.
        This is a test dialogue to demonstrate text-to-speech using Eleven Labs.
        We hope you enjoy the results!
        """

        # Convert text to speech
        response = text_to_speech(dialogue, voice_id=selected_voice_id)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"Audio saved as {output_path}")
        else:
            print(f"Failed to generate audio: {response.status_code}, {response.text}")

# Voices available 
# Voice Name: Aria, Voice ID: 9BWtsMINqrJLrRacOk9x
# Voice Name: Roger, Voice ID: CwhRBWXzGAHq8TQ4Fs17
# Voice Name: Sarah, Voice ID: EXAVITQu4vr4xnSDxMaL
# Voice Name: Laura, Voice ID: FGY2WhTYpPnrIDTdsKH5
# Voice Name: Charlie, Voice ID: IKne3meq5aSn9XLyUdCD
# Voice Name: George, Voice ID: JBFqnCBsd6RMkjVDRZzb
# Voice Name: Callum, Voice ID: N2lVS1w4EtoT3dr4eOWO
# Voice Name: River, Voice ID: SAz9YHcvj6GT2YYXdXww
# Voice Name: Liam, Voice ID: TX3LPaxmHKxFdv7VOQHJ
# Voice Name: Charlotte, Voice ID: XB0fDUnXU5powFXDhCwa
# Voice Name: Alice, Voice ID: Xb7hH8MSUJpSbSDYk0k2
# Voice Name: Matilda, Voice ID: XrExE9yKIg1WjnnlVkGX
# Voice Name: Will, Voice ID: bIHbv24MWmeRgasZH58o
# Voice Name: Jessica, Voice ID: cgSgspJ2msm6clMCkdW9
# Voice Name: Eric, Voice ID: cjVigY5qzO86Huf0OWal
# Voice Name: Chris, Voice ID: iP95p4xoKVk53GoZ742B
# Voice Name: Brian, Voice ID: nPczCjzI2devNBz1zQrb
# Voice Name: Daniel, Voice ID: onwK4e9ZLuTAKqWW03F9
# Voice Name: Lily, Voice ID: pFZP5JQG7iQjIQuC4Bku
# Voice Name: Bill, Voice ID: pqHfZKP75CvOlQylNhV4