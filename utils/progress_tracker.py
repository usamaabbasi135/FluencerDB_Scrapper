import json
import os

PROGRESS_FILE = "progress.json" # File to store scraping progress (page numbers per keyword)

def load_progress():
    """
    Load progress from the progress.json file.
    If the file doesn't exist, return an empty dictionary.

    Returns:
        dict: A dictionary mapping keywords to the last scraped page.
    """

    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(progress):
    """
    Save the current progress to the progress.json file.

    Args:
        progress (dict): A dictionary mapping keywords to the last scraped page.
    """
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)
