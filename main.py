# main.py

from config import HEADLESS, MAX_PAGES, OUTPUT_DIR
from scrapper.driver import get_driver
from scrapper.navigator import perform_search, go_to_next_page
from scrapper.parser import extract_table_data
from utils.excel_writer import save_to_excel

def main():
    keyword = input("Enter search keyword: ")
    driver = get_driver(headless=HEADLESS)

    try:
        perform_search(driver, keyword)
        all_data = []

        page = 1
        while True:
            print(f"[INFO] Scraping page {page}...")
            page_data = extract_table_data(driver)
            all_data.extend(page_data)

            if MAX_PAGES and page >= MAX_PAGES:
                break

            if not go_to_next_page(driver):
                break

            page += 1

        save_to_excel(all_data, keyword, OUTPUT_DIR)

    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"[WARNING] Could not close driver cleanly: {e}")

if __name__ == "__main__":
    main()