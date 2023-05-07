import gspread
from oauth2client.service_account import ServiceAccountCredentials
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

# Initialize empty lists to store data
timestamps = []
sensor1_values = []
sensor2_values = []
sensor3_values = []

# Continuously read data from the sheet and update the plot
while True:
    # Clear the lists
    timestamps.clear()
    sensor1_values.clear()
    sensor2_values.clear()
    sensor3_values.clear()
    
    # Get the data from the sheet
    rows = sheet.get_all_values()
    for row in rows:
        # Convert the timestamp string to a datetime object
        timestamp = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        timestamps.append(timestamp)
        
        # Convert the time delta string to a timedelta object
        time_delta = datetime.datetime.strptime(row[1], '%H:%M:%S') - datetime.datetime(1900, 1, 1)
        time_delta_seconds = time_delta.total_seconds()
        sensor1_values.append(time_delta_seconds)
        
        # Convert the sensor value strings to integers
        sensor2_values.append(int(row[2]))
        sensor3_values.append(int(row[3]))
    
    # Create a pandas dataframe with the data
    data = {'timestamp': timestamps, 'sensor1': sensor1_values, 'sensor2': sensor2_values, 'sensor3': sensor3_values}
    df = pd.DataFrame(data)
    
    # Group the data by minute and calculate the mean of each group
    df['minute'] = df['timestamp'].dt.floor('Min')
    df_mean = df.groupby('minute').mean()
    
    # Create the plot
    plt.plot(df_mean.index, df_mean['sensor1'], label='Sensor 1')
    plt.plot(df_mean.index, df_mean['sensor2'], label='Sensor 2')
    plt.plot(df_mean.index, df_mean['sensor3'], label='Sensor 3')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Sensor Value')
    plt.title('Relative Sensor Data')
    plt.show()
    
    # Wait for 3 seconds before updating the plot again
    time.sleep(3)

