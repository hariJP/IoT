import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time

# set up credentials to access the Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/kali/.config/gspread/service_account.json', scope)
gc = gspread.authorize(creds)

# open the Google Sheet and select the first worksheet
sh = gc.open('ruok')
worksheet = sh.sheet1

# initialize variables for storing the previous sensor readings
previous_b = None
previous_c = None

# set up email credentials
sender_email = 'h4r1pr4s47h@gmail.com'
sender_password = 'termuxwave'
receiver_email = 'jhp952003@gmail.com'

# define a function to send the email
def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

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


