# scraper/navigator.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from config import WAIT_TIME
def perform_search(driver, keyword,page=1):
    """
    Performs a keyword search on the FluencerDB website.

    Steps:
    - Opens the search page
    - Waits for the input field to load
    - Types the keyword
    - Clicks the search button
    - Waits for results to load

    Args:
        driver (WebDriver): The Selenium Chrome driver.
        keyword (str): The keyword to search for.
    """
    url = f"https://fluencerdb.com/search/{keyword}?page={page}"
    driver.get(url)

    if page == 1:
    # Wait until the search box is visible (up to 60 seconds)
        try:
            search_box = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.ID, "search-query"))
            )
        except:
            print("[ERROR] Search input box not found.")
            driver.save_screenshot("search_box_error.png") # Save screenshot for debugging
            raise

        # Type the keyword into the input box and click Search
        search_box.clear()
        search_box.send_keys(keyword)

        search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
        search_button.click()

        # Wait for results to load
        time.sleep(3)
    else:
        # If page > 1, wait for table rows directly
        WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
        )

def go_to_next_page(driver):
    """
    Attempts to click the 'Next' button to go to the next page of results.

    Returns:
        bool: True if next page was clicked, False if there are no more pages.
    """
    try:
        # Wait up to 10 seconds for the 'Next »' button to be clickable
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.pagination li a[aria-label='Next »']"))
        )

        # Use JavaScript click to ensure reliability
        driver.execute_script("arguments[0].click();", next_btn)

        # Wait for the page to load
        time.sleep(3)
        return True
    except TimeoutException:
        # If the button is not found or not clickable, we're likely at the last page
        print("[INFO] No more pages or next button not found.")
        return False
