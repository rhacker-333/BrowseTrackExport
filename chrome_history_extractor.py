import sqlite3
import pandas as pd
import os
import shutil

# Path to Chrome History DB
history_db = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"

# Copy to avoid access issues
shutil.copy2(history_db, "History_copy")

# Connect to the copied DB
conn = sqlite3.connect("History_copy")
cursor = conn.cursor()

# Query for browsing history
query = """
SELECT urls.url, urls.title, urls.visit_count, datetime(urls.last_visit_time / 1000000 - 11644473600, "unixepoch") as last_visit_time
FROM urls
ORDER BY last_visit_time DESC
"""

# Fetch data
data = pd.read_sql_query(query, conn)

# Export to Excel or CSV
#data.to_csv("chrome_history.csv", index=False)
data.to_excel("chrome_history.xlsx", index=False)

# Cleanup
conn.close()
os.remove("History_copy")

print("✅ Chrome history exported successfully!")
