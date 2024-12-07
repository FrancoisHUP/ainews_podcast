from pathlib import Path
from html import unescape
import re

def clean_rss_item(item):
    """
    Cleans an RSS feed item by decoding HTML entities and removing HTML tags.
    """
    # Decode HTML entities
    decoded_item = unescape(item)
    # Remove HTML tags using regex
    clean_text = re.sub(r'<.*?>', '', decoded_item)
    # Remove leading and trailing whitespace
    clean_text = clean_text.strip()
    return clean_text

def process_file(input_file, output_file):
    """
    Reads an input file, cleans the data, and writes the cleaned content to an output file.
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Split content by items (assuming RSS-like format)
    items = content.split('<item>')
    cleaned_items = []

    for item in items:
        cleaned = clean_rss_item(item)
        if cleaned:  # Ignore empty lines
            cleaned_items.append(cleaned)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n\n'.join(cleaned_items))  # Separate items with double newlines for readability

# File paths
input_file = Path("data/swix_newletter_iteration_06_12_2024.txt")
output_file = Path("data/swix_newletter_iteration_clean_06_12_2024.txt")

# Process the file
process_file(input_file, output_file)

print(f"Cleaned content saved to {output_file}.")
