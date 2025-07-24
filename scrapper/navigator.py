# scraper/navigator.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def perform_search(driver, keyword):
    driver.get("https://fluencerdb.com/search")

    # Wait for search input to be visible
    try:
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )
    except:
        print("[ERROR] Search input box not found.")
        driver.save_screenshot("search_box_error.png")
        raise

    search_box.clear()
    search_box.send_keys(keyword)

    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()

    # Wait for results to load
    time.sleep(3)

def go_to_next_page(driver):
    try:
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.pagination li a[aria-label='Next »']"))
        )
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)
        return True
    except TimeoutException:
        print("[INFO] No more pages or next button not found.")
        return False
