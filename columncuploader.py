import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import datetime
import time

# Replace with the name of your Google Sheet
SHEET_NAME = 'ruok'

# Replace with the path to your Google service account credentials file
CREDENTIALS_FILE = '/home/akash/.config/gspread/service_account.json'

# Authenticate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open(SHEET_NAME).sheet1

# Generate and upload random sensor data with timestamp
while True:
    data_b = random.randint(20, 100)
    data_c = random.randint(20, 100)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet.append_row([timestamp, data_b, data_c])
    time.sleep(3) # Wait for 3 seconds before next upload

