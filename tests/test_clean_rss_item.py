import pytest
from pathlib import Path
from utils.get_data import clean_rss_item

def test_clean_rss_item_with_real_data():
    """
    Test clean_rss_item with real data from a file.
    """
    input_text = Path("data/swix_newletter_iteration_06_12_2024.txt").read_text(encoding="utf-8")
    expected_output = Path("data/swix_newletter_iteration_clean_06_12_2024.txt").read_text(encoding="utf-8")

    # Split input by <item> tag to simulate feed item processing
    items = input_text.split('<item>')

    # Clean each item and join results
    cleaned_items = []
    for item in items:
        cleaned = clean_rss_item(item)
        if cleaned:  # Ignore empty lines
            cleaned_items.append(cleaned)

    result = '\n\n'.join(cleaned_items)

    # Normalize whitespace for comparison
    result = '\n'.join(line.strip() for line in result.splitlines())
    expected = '\n'.join(line.strip() for line in expected_output.splitlines())

    assert result == expected

@pytest.mark.parametrize("input_text,expected_output", [
    # Test case with empty input
    ("", ""),

    # Test case with plain text (no HTML)
    ("Just some regular text without any HTML", "Just some regular text without any HTML"),

    # Test case with simple HTML
    ("<p>Simple paragraph</p>", "Simple paragraph"),

    # Test case with encoded HTML entities
    ("&lt;p&gt;Encoded paragraph&lt;/p&gt;", "Encoded paragraph"),

    # Test case with complex HTML
    ("<div><p>Complex <strong>HTML</strong></p></div>", "Complex HTML"),
])
def test_clean_rss_item_edge_cases(input_text, expected_output):
    """
    Test clean_rss_item with edge cases.
    """
    result = clean_rss_item(input_text)
    assert result.strip() == expected_output.strip()

