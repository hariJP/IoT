import gspread

# Authenticate with Google Sheets API using a service account
# Replace 'service_account.json' with the path to your service account file
sa = gspread.service_account(filename='service_account.json')

# Open the Google Sheets file by name
sh = sa.open("ruok")

# Get the first worksheet in the file by name
wks = sh.worksheet("Sheet1")

# Print the number of rows and columns in the worksheet
print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

