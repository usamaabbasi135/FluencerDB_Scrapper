from selenium.webdriver.common.by import By

def extract_table_data(driver):
    table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    records = []
    for row in table_rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 6:
            records.append({
                "ID": cols[0].text.strip(),
                "Name": cols[1].text.strip(),
                "Username": cols[2].text.strip(),
                "Email": cols[3].text.strip(),
                "Phone": cols[4].text.strip(),
                "Followers": cols[5].text.strip(),
            })
    return records