import gspread
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from datetime import datetime
import time

# set up credentials to access the Google Sheet
creds = None
creds_file = '/home/kali/.config/gspread/service_account.json'
creds_scopes = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
    creds_file, scopes=creds_scopes)

gc = gspread.authorize(creds)

# open the Google Sheet and select the first worksheet
sh = gc.open('ruok')
worksheet = sh.sheet1

# generate and upload random sensor data with timestamp
while True:
    row = worksheet.get_all_values()[-1]
    timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    try:
        sensor_data_b = int(row[1])
    except ValueError:
        # handle the case where the value in the second column cannot be converted to an integer
        sensor_data_b = None
    try:
        sensor_data_c = int(row[2])
    except ValueError:
        # handle the case where the value in the third column cannot be converted to an integer
        sensor_data_c = None

    if sensor_data_b is not None and sensor_data_b > 90 and previous_b is not None and previous_b <= 90:
        send_email('Sonic Sensor Warning', 'The Sonic Sensor has crossed 100.')
    if sensor_data_c is not None and sensor_data_c > 90 and previous_c is not None and previous_c <= 90:
        send_email('Humidity Sensor Warning', 'The Humidity Sensor has crossed 100.')
    
    previous_b = sensor_data_b
    previous_c = sensor_data_c
    
    time.sleep(3) # wait for 3 seconds before checking the next sensor readings

