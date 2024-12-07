import feedparser
from html import unescape
import re
from datetime import datetime

def clean_rss_item(item):
    """
    Cleans an RSS feed item by decoding HTML entities and removing HTML tags.
    """
    # Decode HTML entities
    decoded_item = unescape(item)
    # Remove HTML tags using regex
    clean_text = re.sub(r'<.*?>', '', decoded_item)
    # Remove leading and trailing whitespace
    return clean_text.strip()

def fetch_rss(rss_url):
    """
    Fetches and parses the RSS feed from the provided URL.
    """
    return feedparser.parse(rss_url)

def get_most_recent_date(feed):
    """
    Gets the most recent date from the RSS feed entries.
    """
    if not feed.entries:
        return None
    # Get the most recent entry by sorting the entries by their publication date
    latest_entry = max(feed.entries, key=lambda entry: datetime(*entry.published_parsed[:6]))
    return datetime(*latest_entry.published_parsed[:6]).date()

def get_rss_items_by_date(feed, target_date=None):
    """
    Filters RSS items by a specific date. If no date is provided, takes the most recent date.
    """
    items = []
    for entry in feed.entries:
        # Parse publication date
        pub_date = datetime(*entry.published_parsed[:6]).date()
        if target_date is None or pub_date == target_date:
            # Clean and store the relevant content
            title = clean_rss_item(entry.title)
            description = clean_rss_item(entry.description)
            link = entry.link
            items.append(f"{title}\n{description}\n{link}")
    return items
