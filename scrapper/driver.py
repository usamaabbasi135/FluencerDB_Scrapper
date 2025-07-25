import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def get_driver(headless=False):
    """
    Launches a new Chrome browser instance using undetected_chromedriver.
    
    Args:
        headless (bool): Whether to run the browser in headless (invisible) mode.

    Returns:
        WebDriver: A Selenium WebDriver object to control the browser.
    """
    options = Options()
    if headless:
        options.add_argument("--headless") # Run browser invisibly
    options.add_argument("--start-maximized") # Open in full screen
    options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation

    driver = uc.Chrome(options=options) # Launch browser
    return driver