project_name: BrowseTrackExport

description: >
  BrowseTrackExport is a Python tool that exports your Google Chrome browsing history into CSV or Excel files by reading the local Chrome SQLite history database.
  It uses sqlite3 and pandas for data extraction and formatting. The project is Windows-ready and can be easily adapted for macOS and Linux.

<img width="1195" height="908" alt="image" src="https://github.com/user-attachments/assets/1d3a2bb3-4eb9-419b-a6f8-12f63a6e6dfe" />
<img width="1496" height="985" alt="image" src="https://github.com/user-attachments/assets/23eefa5f-a42d-42ae-a45c-d10c40ae2cee" />


features:
  - Extracts browsing history: URLs, page titles, visit counts, and last visit times.
  - Exports history data to CSV or Excel (.xlsx) format.
  - Reads Chrome’s SQLite history database locally — no data leaves your machine.
  - Simple setup with minimal dependencies.
  - Easy adaptation for cross-platform support.

requirements:
  - Python 3.x
  - pandas library
  - openpyxl library (required if exporting to Excel)

install_command: "pip install pandas openpyxl"

usage_steps:
  - step: Install Python and Required Packages
    details: >
      Make sure Python is installed on your system. Then install the necessary packages using:
      pip install pandas openpyxl.
  - step: Close Google Chrome
    details: >
      Ensure Chrome is completely closed to avoid database-lock issues.
  - step: Download or Clone the Repository
    details: |
      Download the project files or clone the repository to your local machine:
      ```
      git clone https://github.com/yourusername/BrowseTrackExport.git
      cd BrowseTrackExport
      ```
  - step: Modify the Script for Excel Export (Optional)
    details: |
      By default, the script exports browsing history to CSV. To generate an Excel file instead, open `export_chrome_history.py` and:
      ```
      # Comment out the CSV export line:
      # data.to_csv("chrome_history.csv", index=False)

      # Uncomment or add the Excel export line:
      data.to_excel("chrome_history.xlsx", index=False)
      ```
  - step: Adapt for Your Operating System (Optional)
    details: |
      The default Chrome history path supports Windows. To use on macOS or Linux, update the path in the script like so:
      ```
      import os
      import platform

      user_home = os.path.expanduser("~")

      if platform.system() == "Windows":
          history_db = os.path.join(user_home, r"AppData\Local\Google\Chrome\User Data\Default\History")
      elif platform.system() == "Darwin":  # macOS
          history_db = os.path.join(user_home, "Library/Application Support/Google/Chrome/Default/History")
      elif platform.system() == "Linux":
          history_db = os.path.join(user_home, ".config/google-chrome/Default/History")
      else:
          raise Exception("Unsupported OS")
      ```
  - step: Run the Script
    details: |
      Execute the script with Python:
      ```
      python export_chrome_history.py
      ```
  - step: Locate the Output File
    details: >
      After successful execution, find the exported file (chrome_history.csv or chrome_history.xlsx) in the project directory.

notes:
  - The script creates a temporary copy of the Chrome History database to avoid access conflicts.
  - Chrome stores timestamps in WebKit format; the script converts them to human-readable form.
  - Ensure your browsing data privacy before exporting your history.
  - The script overwrites output files with the same name without warning.

license: "Specify your license here (e.g., MIT License)."
