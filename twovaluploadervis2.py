import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import datetime
import time

# Replace with the name of your Google Sheet
SHEET_NAME = 'ruok'

# Replace with the path to your Google service account credentials file
CREDENTIALS_FILE = '/home/kali/.config/gspread/service_account.json'

# Authenticate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open(SHEET_NAME).sheet1

# Initialize data lists
timestamps = []
data1 = []
data2 = []
data3 = []

# Retrieve data from the sheet
rows = sheet.get_all_values()
for row in rows:
    timestamps.append(datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
    data1.append(int(row[1]))
    data2.append(int(row[2]))
    data3.append(int(row[3].split(":")[2]) + int(row[3].split(":")[1]) * 60 + int(row[3].split(":")[0]) * 3600)

# Plot the data
plt.plot(timestamps, data1, 'r', label='Data 1')
plt.plot(timestamps, data2, 'g', label='Data 2')
plt.plot(timestamps, data3, 'b', label='Data 3')
plt.legend()
plt.show()


