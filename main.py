from pathlib import Path
import argparse
from datetime import datetime
from utils.get_data import fetch_rss, get_rss_items_by_date, get_most_recent_date
from tts.tts_11labs import text_to_speech, fetch_available_voices

def main():
    args = parse_args()

    rss_url = args.rss_url
    target_date = None

    output_file_path = Path("data/swix_newletter_iteration_clean_06_12_2024.txt")
    
    # Fetch and process the RSS feed
    print(f"Fetching RSS feed from {rss_url}...")
    feed = fetch_rss(rss_url)

    if feed.bozo:
        print("Failed to fetch or parse the RSS feed.")
        return

    # Determine the target date
    if args.date:
        target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        target_date = get_most_recent_date(feed)
        if not target_date:
            print("No valid entries found in the RSS feed.")
            return

    print(f"Processing RSS feed for date: {target_date}...")
    items = get_rss_items_by_date(feed, target_date)

    if not items:
        print("Date not found! Sorry :(")
        return

    # Concatenate all items into a single text block
    text_content = "\n\n".join(items)
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Save text_content to a file
    output_file_path.write_text(text_content, encoding="utf-8")

    # Use the date for the output filename
    output_path = output_dir/f"{target_date}.mp3"

    # TODO create the script and mp3, save the mp3
    print(f'Text content \n{text_content[:100]} [...]\n')

    print(f"Converting to MP3 and saving to {output_path}...")
    
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

def parse_args():
    parser = argparse.ArgumentParser(description="Convert RSS feed to MP3.")
    parser.add_argument("rss_url", help="The URL of the RSS feed")
    parser.add_argument("--date", help="The date to filter RSS items (format: YYYY-MM-DD)", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    main()
