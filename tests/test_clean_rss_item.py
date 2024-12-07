import pytest
from pathlib import Path
from utils.clean_data import clean_rss_item

def read_file(file_path):
    """Helper function to read file content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def test_clean_rss_item_with_real_data():
    input_text = Path("data/swix_newletter_iteration_06_12_2024.txt").read_text()
    expected_output = Path("data/swix_newletter_iteration_clean_06_12_2024.txt").read_text()

    # Split input by <item> tag to match process_file behavior
    items = input_text.split('<item>')

    # Process each item and join with double newlines
    cleaned_items = []
    for item in items:
        cleaned = clean_rss_item(item)
        if cleaned:  # Ignore empty lines
            cleaned_items.append(cleaned)

    result = '\n\n'.join(cleaned_items)

    # Normalize whitespace in both strings for comparison
    result = '\n'.join(line.strip() for line in result.splitlines())
    expected = '\n'.join(line.strip() for line in expected_output.splitlines())

    assert result == expected

# Keep some basic test cases for edge cases
@pytest.mark.parametrize("input_text,expected_output", [
    # Test case with empty input
    ("", ""),

    # Test case with plain text (no HTML)
    ("Just some regular text without any HTML", "Just some regular text without any HTML"),

    # Test case with simple HTML
    ("<p>Simple paragraph</p>", "Simple paragraph"),
])
def test_clean_rss_item_edge_cases(input_text, expected_output):
    result = clean_rss_item(input_text)
    assert result.strip() == expected_output.strip()
