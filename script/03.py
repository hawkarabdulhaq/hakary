# Step 1: Import necessary libraries
import pandas as pd
import folium

# Step 2: Load the Excel file
file_path = 'Temperature_Data.xlsx'  # Update this to the local file path if necessary
excel_data = pd.ExcelFile(file_path)

# Step 3: Read data from "Below_25" and "Above_25" sheets
below_25_data = pd.read_excel(excel_data, sheet_name='Below_25')
above_25_data = pd.read_excel(excel_data, sheet_name='Above_25')

# Step 4: Create a map centered around an average location
map_center = [below_25_data['latitude'].mean(), below_25_data['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Step 5: Add markers for "Below_25" data points (blue)
for index, row in below_25_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Latitude: {row['latitude']}, Longitude: {row['longitude']}, Temperature: {row['temperature']}",
        icon=folium.Icon(color='blue')
    ).add_to(m)

# Step 6: Add markers for "Above_25" data points (red)
for index, row in above_25_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Latitude: {row['latitude']}, Longitude: {row['longitude']}, Temperature: {row['temperature']}",
        icon=folium.Icon(color='red')
    ).add_to(m)

# Step 7: Save the map to an HTML file named 'index.html'
m.save('index.html')

print("Map has been created and saved as 'index.html'.")
