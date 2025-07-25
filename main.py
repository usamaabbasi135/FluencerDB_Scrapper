# main.py

from config import HEADLESS, MAX_PAGES, OUTPUT_DIR
from scrapper.driver import get_driver
from scrapper.navigator import perform_search, go_to_next_page
from scrapper.parser import extract_table_data
from utils.excel_writer import save_to_excel
import time
from utils.progress_tracker import load_progress, save_progress
from utils.keyword_utils import remove_keyword_from_file


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

progress = load_progress()

def main():
    keywords = load_keywords_from_file()
    progress = load_progress()

    for keyword in keywords:
        success = False
        remove_keyword_from_file(keyword)
        while not success:
            print(f"\n====== Starting keyword: {keyword} ======")
            driver = get_driver(headless=HEADLESS)

            all_data = []
            current_page = progress.get(keyword, 1)
            print(current_page)
        
            try:
                perform_search(driver, keyword,current_page)
                
                while True:
                    print(f"[INFO] Scraping page {current_page} for keyword: {keyword}")
                    page_data = extract_table_data(driver)
                    all_data.extend(page_data)

                    progress[keyword] = current_page
                    
                    if current_page % 10 == 0:
                        save_to_excel(all_data, keyword, OUTPUT_DIR)
                        save_progress(progress)
                        print(progress)

                    if MAX_PAGES and current_page >= MAX_PAGES:
                        break

                    if not go_to_next_page(driver):
                        break

                    current_page += 1

                save_to_excel(all_data, keyword, OUTPUT_DIR)
                save_progress(progress)
                success = True

            except Exception as e:
                print(f"[ERROR] Failed for keyword '{keyword}': {e}")
                print("[INFO] Retrying the same keyword after short delay...")
                time.sleep(5)
            finally:
                try:
                    driver.quit()
                except:
                    pass

        # Optional: short delay between keywords to avoid suspicion
        time.sleep(3)

if __name__ == "__main__":
    main()