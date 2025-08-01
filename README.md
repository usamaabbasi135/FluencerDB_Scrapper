# FluencerDB Web Scraper

This project is a fully automated, modular web scraper built using **Selenium** and **undetected-chromedriver**. It extracts influencer data from [FluencerDB](https://fluencerdb.com) based on dynamic keyword searches and saves the output to Excel files. The scraper supports resuming from where it left off, tracks page-level progress, and is structured for easy scaling.

---

## Features

-  **Dynamic keyword-based search**
-  **Scrapes all pages of results** per keyword
-  **Exports data to Excel** (`.xlsx`) with progress-based updates
-  **Resume-safe** using `progress.json`
-  **Retry mechanism** on failure
-  **Smart URL jumping** to avoid unnecessary clicks
-  **Stealth scraping** using undetected Chrome driver
-  **Clean modular structure** for future scaling
---

## Project Structure
```text
fluencer_scraper/
│
├── main.py # Main orchestration script
├── config.py # Constants and settings
│
├── scrapper/ # Scraping modules
│ ├── driver.py # Sets up undetected Chrome driver
│ ├── navigator.py # Navigates search, pagination
│ ├── parser.py # Parses table data from the page
│
├── utils/ # Utility modules
│ ├── excel_writer.py # Saves data to Excel
│ ├── progress_tracker.py # Loads and saves page-level progress
│ └── keyword_utils.py # Reads and edits keywords.txt
│
├── data/ # Output Excel files
│ └── *.xlsx
│
├── keywords.txt # Input list of keywords (one per line)
├── progress.json # Auto-generated file for resuming progress
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```
---

## How It Works

1. **Reads keywords** from `keywords.txt`
2. For each keyword:
   - If progress exists, resumes from last page
   - Otherwise starts from page 1
3. Scrapes all result pages (`50 records/page`)
4. Saves data to `data/<keyword>.xlsx`
5. Saves scraping progress to `progress.json`
6. Removes completed keywords from the list

---
## Configuration

Set scraping options in `config.py`:

```python
BASE_URL = "https://fluencerdb.com/search"
RESULTS_PER_PAGE = 50
MAX_PAGES = 2000  # Set to None to auto-detect later
WAIT_TIME = 30   # Seconds to wait for page elements
HEADLESS = False # Set to True if you want to run without browser window
OUTPUT_DIR = "data"
```
## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fluencerdb-scraper.git
cd fluencerdb-scraper
```

## 2. Install Dependencies

To install all required Python libraries, run the following command:

```bash
pip install -r requirements.txt
```
## 3. Add Keywords

Create or edit a file named `keywords.txt` in the root folder and add one keyword per line. For example:
```text
pet
health
fitness
fashion
```

## 4. Run the Scraper
```bash
python main.py
```

## Output

Each keyword will generate:

-  An Excel file: `data/keyword.xlsx`
-  A JSON progress file: `progress.json`

You can open the Excel file to view structured influencer data.

---

## Resume After Crash

The script is **crash-safe** and includes automatic recovery:

- Automatically resumes from the **last scraped page** for each keyword
- Retries the same keyword if an error occurs
- You **don’t need to restart from scratch**

## Known Limitations

- Does not solve image-based CAPTCHAs (e.g., "select bicycles")
- Runs slower in headless mode if CAPTCHA is active
- Does not use proxy rotation (yet)

---

## To-Do / Roadmap

- [ ] Parallel scraping with ThreadPoolExecutor
- [ ] Full CAPTCHA bypass using JavaScript injection
- [ ] Proxy pool for IP rotation
- [ ] Export logs and error summaries
- [ ] Optional: Web-based dashboard

---

## Credits

Built with love by **Usama Abbasi**

Feel free to fork, modify, and use. Pull Requests (PRs) are welcome!

## Author
- Usama Abbasi
- Data Scientis and Analyst | Afiniti
- Contact: usamahafeez.abbasi1234@gmail.com
