import gspread
import matplotlib.pyplot as plt

# Authenticate and open worksheet
gc = gspread.service_account()
sh = gc.open("ruok")
worksheet = sh.sheet1

# Get data from worksheet
data = worksheet.get_all_values()
headers = data.pop(0)

# Extract relevant columns
times = [row[1] for row in data if row[2] != ""]
values = [float(row[2]) for row in data if row[2] != ""]

# Plot data
plt.plot(times, values)
plt.xlabel(headers[1])
plt.ylabel(headers[2])
plt.show()

