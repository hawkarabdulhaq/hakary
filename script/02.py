# Step 1: Import necessary libraries
import pandas as pd
import requests
from openpyxl import load_workbook

# Optional: gspread usage for Google Sheets interaction
# import gspread
# from gspread_dataframe import set_with_dataframe

# Step 2: Download the Excel file
file_url = 'https://docs.google.com/spreadsheets/d/1kDudF69cgYiPnZnTP7MNF69_SMAvDTJi/export?format=xlsx'
file_path = 'Temperature_Data.xlsx'
r = requests.get(file_url)
with open(file_path, 'wb') as f:
    f.write(r.content)

# Step 3: Read the Excel file
excel_data = pd.ExcelFile(file_path)

# Assuming the sheet with temperature data is the first one
df = pd.read_excel(excel_data, sheet_name=0)

# Step 4: Check the column names
print("Column names in the DataFrame:")
print(df.columns)

# Step 5: Filter out rows where temperature is below 25°C
filtered_data_below = df[df['temperature'] < 25]

# Step 6: Round the temperature values to 2 decimal places
filtered_data_below['temperature'] = filtered_data_below['temperature'].round(2)

# Step 7: Save the filtered data to a new sheet "Below_25"
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    filtered_data_below.to_excel(writer, sheet_name='Below_25', index=False)

# Step 8: Filter out rows where temperature is above 25°C
filtered_data_above = df[df['temperature'] > 25]

# Step 9: Round the temperature values to 2 decimal places
filtered_data_above['temperature'] = filtered_data_above['temperature'].round(2)

# Step 10: Save the filtered data to a new sheet "Above_25"
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    filtered_data_above.to_excel(writer, sheet_name='Above_25', index=False)

print("Filtered data has been saved to both 'Below_25' and 'Above_25' sheets.")
