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
x_data = []
y_data = []

# set up the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
index = count()

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
    ax.set_title('Temperature Data')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Temperature (C)')

# start the animation
ani = FuncAnimation(fig, animate, interval=5000)
plt.show()

