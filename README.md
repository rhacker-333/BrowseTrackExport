# BrowseTrackExport

A Python tool to export your Google Chrome browsing history into CSV or Excel files by reading the local Chrome SQLite history database.  
Works on Windows out of the box and can be easily modified for macOS and Linux.

<img width="1149" height="950" alt="image" src="https://github.com/user-attachments/assets/7b8d876b-69ef-4920-ad85-8e6783604fa6" />
<img width="1521" height="1017" alt="image" src="https://github.com/user-attachments/assets/a443d7cc-cb55-439b-812b-32fda6c1ba74" />


## Features

- Export URLs, page titles, visit counts, and last visit times
- Save history data as CSV or Excel files
- Works locally with no internet connection or data upload
- Minimal dependencies: Python, pandas, `openpyxl` (for Excel export)
- Cross-platform paths easily configurable

## Installation & Setup

### 1. Install Python and dependencies

pip install pandas openpyxl


### 2. Close Google Chrome

Make sure Chrome is completely closed to avoid locking the history database.

### 3. Download or clone this repo

git clone https://github.com/yourusername/BrowseTrackExport.git
cd BrowseTrackExport


### 4. (Optional) Edit the script

- To export as Excel, change export lines in `export_chrome_history.py`:


Comment out CSV export line
data.to_csv("chrome_history.csv", index=False)

Uncomment Excel export line
data.to_excel("chrome_history.xlsx", index=False)


- (Optional) Update the Chrome history database path for macOS/Linux in the script if needed:

import os
import platform

user_home = os.path.expanduser("~")

if platform.system() == "Windows":
history_db = os.path.join(user_home, "AppData\Local\Google\Chrome\User Data\Default\History")
elif platform.system() == "Darwin": # macOS
history_db = os.path.join(user_home, "Library/Application Support/Google/Chrome/Default/History")
elif platform.system() == "Linux":
history_db = os.path.join(user_home, ".config/google-chrome/Default/History")
else:
raise Exception("Unsupported OS")


## Usage

Run the script to export your browsing history:

python export_chrome_history.py


The output file (`chrome_history.csv` or `chrome_history.xlsx`) will be created in the current directory.

## Troubleshooting

- **Database locked error?**  
  Close Google Chrome before running the script.

- **File not found?**  
  Verify that the Chrome user profile path in the script matches your operating system and profile setup.

- **No Excel file created?**  
  Ensure `openpyxl` is installed and that you have switched the export lines for Excel output as shown above.

## Customization

Modify the script to change export formats, filenames, or to add filtering options as per your needs.

