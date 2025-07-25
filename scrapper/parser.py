from selenium.webdriver.common.by import By

def extract_table_data(driver):
    """
    Extracts influencer data from the current page's HTML table.

    Returns:
        list of dict: Each dictionary contains one influencer's data:
            - ID, Name, Username, Email, Phone, Followers  etc
    """

    # Find all rows in the table body
    table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    records = []
    for row in table_rows:
        # Get all columns in the row
        cols = row.find_elements(By.TAG_NAME, "td")
        # Only process rows with at least 12 columns
        if len(cols) >= 12:
            records.append({
                "ID": cols[0].text.strip(),
                "Name": cols[1].text.strip(),
                "Username": cols[2].text.strip(),
                "Email": cols[3].text.strip(),
                "Phone": cols[4].text.strip(),
                "Followers": cols[5].text.strip(),
                "Following": cols[6].text.strip(),
                "Biography": cols[7].text.strip(),
                "Link": cols[8].text.strip(),
                "Niche": cols[9].text.strip(),
                "Business": cols[10].text.strip(),
                "Verified": cols[11].text.strip(),
            })
    return records