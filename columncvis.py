import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
from datetime import datetime
from itertools import count
from matplotlib.animation import FuncAnimation


# set up credentials to access the Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/kali/.config/gspread/service_account.json', scope)
gc = gspread.authorize(creds)

# open the Google Sheet and select the first worksheet
sh = gc.open('ruok')
worksheet = sh.sheet1

# initialize lists to store the data
x_data_b = []
y_data_b = []
y_data_c = []

# set up the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
index = count()

# define a function to update the plot in real-time
def animate(i):
    # read the last row of data from the Google Sheet
    row = worksheet.get_all_values()[-1]
    timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    sensor_data_b = int(row[1])
    sensor_data_c = int(row[2])

    # add the data to the lists
    x_data_b.append(timestamp)
    y_data_b.append(sensor_data_b)
    y_data_c.append(sensor_data_c)

    # plot the data
    ax.clear()
    ax.plot(x_data_b, y_data_b, label='Sonic Sensor')
    ax.plot(x_data_b, y_data_c, label='Humidity Sensor')

    # set the plot title and axis labels
    ax.set_title('Sensor Data')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Sensor Reading')
    ax.legend()

# start the animation
ani = FuncAnimation(fig, animate, interval=1000)
plt.show()

