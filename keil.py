import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
from datetime import datetime
from itertools import count
from matplotlib.animation import FuncAnimation
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# set up credentials to access the Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/kali/.config/gspread/service_account.json', scope)
gc = gspread.authorize(creds)

# open the Google Sheet and select the first worksheet
sh = gc.open('ruok')
worksheet = sh.sheet1

# initialize lists to store the data
x_data = []
y_data = []

# set up the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
index = count()

# set up email credentials
sender_email = 'h4r1pr4s47h@gmail.com'
sender_password = 'biomoswave'
receiver_email = 'jhp952003@gmail.com'

# define a function to send email
def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    # create SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

# define a function to update the plot in real-time
def animate(i):
    # read the last row of data from the Google Sheet
    row = worksheet.get_all_values()[-1]
    timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    sensor_data = int(row[1])

    # add the data to the lists
    x_data.append(timestamp)
    y_data.append(sensor_data)

    # plot the data
    ax.clear()
    ax.plot(x_data, y_data)

    # set the plot title and axis labels
    ax.set_title('Sensor Data')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Sensor Reading')
    
    # check if the sensor reading is above 90 and send email if true
    if sensor_data > 90:
        message = f"Warning! The sensor reading reached {sensor_data} at {timestamp}. You have to look at this immediately."
        send_email("Sensor Reading Warning", message)

# start the animation
ani = FuncAnimation(fig, animate, interval=1000)
plt.show()

