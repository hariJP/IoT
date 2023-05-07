import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import numpy as np
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

# Initialize empty lists for each column of data
timestamps = []
data1 = []
data2 = []
data3 = []

# Read the data from the sheet and append to the corresponding lists
for row in sheet.get_all_values():
    timestamps.append(row[0])
    data1.append(int(row[1]))
    data2.append(int(row[2]))
    data3.append(int(row[3]))

    # Plot the data in three different colors
    plt.clf()
    plt.plot(timestamps, data1, 'r-', label='Data 1')
    plt.plot(timestamps, data2, 'g-', label='Data 2')
    plt.plot(timestamps, data3, 'b-', label='Data 3')
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Sensor Data')
    plt.show(block=False)

    # Wait for 3 seconds before plotting the next data point
    time.sleep(3)

