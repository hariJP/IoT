import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time

# set up credentials to access the Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/kali/.config/gspread/service_account.json', scope)
client = gspread.authorize(creds)

# open the Google Sheet and select the first worksheet
sheet = client.open('ruok').sheet1  # replace with your sheet name

# continuously generate and upload temperature data every 5 seconds
while True:
    temperature = random.uniform(20, 130)
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    sheet.append_row([current_time, temperature])
    time.sleep(5)

