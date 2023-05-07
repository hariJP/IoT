import gspread
from oauth2client.service_account import ServiceAccountCredentials
import serial

# Replace with the name of your Google Sheet and worksheet
SHEET_NAME = 'ruok'
WORKSHEET_NAME = 'ruok'

# Replace with the path to your Google service account credentials file
CREDENTIALS_FILE = '/home/kali/.config/gspread/service_account.json'

# Replace with the serial port your device is connected to
SERIAL_PORT = '/dev/ttyACM0'

# Open the serial port
ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)

# Authenticate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Open the worksheet
sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)

# Loop forever, reading data from the serial port and writing it to the worksheet
while True:
    # Read a line of data from the serial port
    data = ser.readline().decode('utf-8').strip()

    # Write the data to the worksheet
    sheet.append_row([data])

