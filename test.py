from podcastfy.client import generate_podcast
import os
from pathlib import Path

def main():
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key is None:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")


    expected_output = Path("data/swix_newletter_iteration_clean_06_12_2024.txt").read_text(encoding="utf-8")

    expected = '\n'.join(line.strip() for line in expected_output.splitlines())
    process_content = generate_podcast(transcript_file=expected, 
                     transcript_only=True, 
                     )
    print(process_content.model_name)

if __name__ == "__main__":
    main()