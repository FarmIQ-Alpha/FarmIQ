import pandas as pd
import os

# Load and preprocess data
file_path = 'psenica.csv'  # Update this to the actual path of your CSV file
data = pd.read_csv(file_path, delimiter=';')
data['Value'] = data.iloc[:, 1].str.replace(',', '.').astype(float)
data.rename(columns={data.columns[0]: 'Year'}, inplace=True)
data['Year'] = pd.to_datetime(data['Year'], format='%Y')  # Convert 'Year' to datetime
data.set_index('Year', inplace=True)  # Set the datetime column as the index

# Calculate 3-year moving average and shift it to align with the forecast year
data['3Y_MA'] = data['Value'].rolling(window=3).mean().shift(1)

# Forecast the next year based on the last calculated moving average
next_year = data.index[-1].year + 1
next_year_forecast = data['3Y_MA'].iloc[-1]

# Extract file name without extension
file_name = os.path.splitext(os.path.basename(file_path))[0]

print(f"Forecast for the {file_name} year {next_year}: {next_year_forecast}")



