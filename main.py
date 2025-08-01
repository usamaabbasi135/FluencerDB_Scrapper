# main.py
# Import configuration constants
from config import HEADLESS, MAX_PAGES, OUTPUT_DIR

# Import modules for browser automation
from scrapper.driver import get_driver
from scrapper.navigator import perform_search, go_to_next_page
from scrapper.parser import extract_table_data

# Import utilities for file writing and progress tracking
from utils.excel_writer import save_to_excel
from utils.progress_tracker import load_progress, save_progress
from utils.keyword_utils import remove_keyword_from_file

import time

def load_keywords_from_file(file_path="keywords.txt"):
    """
    Reads keywords from a text file, one per line.
    Removes extra whitespace and skips blank lines.
    
    Args:
        file_path (str): Path to the keywords file. Defaults to 'keywords.txt'.

    Returns:
        list: A list of cleaned, non-empty keyword strings.
    """
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Load existing progress from previous run (if any)
progress = load_progress()

def main():

    # Load the list of keywords to be scraped
    keywords = load_keywords_from_file()

    # Load previously saved scraping progress
    progress = load_progress()

    # Loop over each keyword in the keyword list
    for keyword in keywords:
        success = False

        # Remove the keyword from the keyword file early
        # This ensures if it's successfully scraped, it won't repeat
        remove_keyword_from_file(keyword)

        # Retry scraping the same keyword until success
        while not success:
            print(f"\n====== Starting keyword: {keyword} ======")

            # Launch a stealth browser instance
            driver = get_driver(headless=HEADLESS)

            all_data = []

            # Resume from last saved page, or start from page 1
            current_page = progress.get(keyword, 1)
            print(current_page)
        
            try:
                # Go directly to the target page for this keyword
                perform_search(driver, keyword,current_page)
                
                # Loop through all result pages for this keyword
                while True:
                    print(f"[INFO] Scraping page {current_page} for keyword: {keyword}")

                    # Extract data from current page and append# Extract data from current page and append
                    page_data = extract_table_data(driver)
                    all_data.extend(page_data)

                    # Save current page number in progress
                    progress[keyword] = current_page
                    
                    # Every 10 pages, save Excel + progress file to disk
                    if current_page % 10 == 0:
                        save_to_excel(all_data, keyword, OUTPUT_DIR)
                        save_progress(progress)
                        print(progress)

                    # Stop scraping if maximum page limit is reached
                    if MAX_PAGES and current_page >= MAX_PAGES:
                        break

                    # Try to go to the next page; if not found, stop loop
                    if not go_to_next_page(driver):
                        break

                    current_page += 1

                # Final save after last page scraped
                save_to_excel(all_data, keyword, OUTPUT_DIR)
                save_progress(progress)
                success = True

            except Exception as e:

                # Handle any unexpected errors and retry
                print(f"[ERROR] Failed for keyword '{keyword}': {e}")
                print("[INFO] Retrying the same keyword after short delay...")
                time.sleep(5)

            finally:

                # Ensure browser is closed after each attempt
                try:
                    driver.quit()
                except:
                    pass

        # Small delay between keywords to avoid being flagged as a bot
        time.sleep(3)

# Entry point for the script
if __name__ == "__main__":
    main()