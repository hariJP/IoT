import gspread
import matplotlib.pyplot as plt

# Authenticate with Google Sheets API using a service account
# Replace 'service_account.json' with the path to your service account file
sa = gspread.service_account(filename='service_account.json')

# Open the Google Sheets file by name
sh = sa.open("ruok")

# Get the first worksheet in the file by name
wks = sh.worksheet("Sheet1")

# Get the values from the worksheet
data = wks.get_all_values()

# Extract the column headings and the data rows
headings = data[0]
rows = data[1:]

# Convert the data rows to a dictionary for easy plotting
data_dict = {}
for row in rows:
    name = row[0]
    score = int(row[1])
    data_dict[name] = score

# Create a bar chart to visualize the scores
names = list(data_dict.keys())
scores = list(data_dict.values())
plt.scatter(names, scores)
plt.title('Student Scores')
plt.xlabel('Student Name')
plt.ylabel('Score')
plt.show()

