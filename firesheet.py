import gspread
from oauth2client.service_account import ServiceAccountCredentials
import firebase_admin
from firebase_admin import messaging

# Set up the Firebase app
cred = firebase_admin.credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Set up the Google Sheet API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Name of your Google Sheet').sheet1

# Loop indefinitely to check the sensor data
while True:
    # Get the latest sensor data from the Google Sheet
    data = sheet.get_all_values()
    latest_data = data[-1]  # Assumes that the latest data is at the bottom

    # Extract the sensor values
    date_time = latest_data[0]
    value1 = int(latest_data[1])
    value2 = int(latest_data[2])

    # Check if the sensor value crossed the limit
    if value1 > 90:
        # Send a notification using FCM
        message = messaging.Message(
            notification=messaging.Notification(
                title='Sensor value crossed the limit!',
                body='Sensor value 1 crossed the limit of 90 at {}'.format(date_time)
            ),
            topic='your-topic'
        )
        response = messaging.send(message)
        print('Notification sent:', response)

    # Wait for 3 seconds before checking the sensor data again
    time.sleep(3)
