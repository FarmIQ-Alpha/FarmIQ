import pandas as pd


class PredictPrices:
    def __init__(self):
        # Load the dataset with semicolon delimiter and the first column as index
        self.file_path = 'ARIMA_models/celdatasetza3ma.csv'
        
    def read_data(self):
        return pd.read_csv(self.file_path, delimiter=';', index_col=0, decimal=',')

    def run(self):
        # Read the data from file
        data = self.read_data()

        # Replace 'z' with NaN
        data.replace('z', pd.NA, inplace=True)

        # Explicit conversion to float to handle decimal commas
        data = data.apply(lambda x: pd.to_numeric(x, errors='coerce'))

        # Replace 'z' values by using a 3-year moving average on the last three available years
        for row in data.index:
            last_three_years = data.columns[-3:]  # Get the last three available years
            for col in data.columns:
                if pd.isna(data.at[row, col]):
                    if len(last_three_years) >= 3:
                        data.at[row, col] = data.loc[row, last_three_years].mean()  # Calculate 3MA
                    else:
                        # If less than 3 years are available, use NaN
                        data.at[row, col] = pd.NA

        # Ensure all data is of type float
        data = data.astype(float)

        # Calculate the 3-year moving average, shifted to the right by one year
        # Using transposition to comply with deprecation warning
        data_3Y_MA = data.T.rolling(window=3).mean().shift(1).T

        # Get the last available moving average for each product and prepare for next year's forecast
        last_year = data.columns[-1]
        return data_3Y_MA[last_year].round(2)

if __name__ == '__main__':
    # Output the forecast data
    print("Forecast data:")
    forecasts = PredictPrices()
    print(forecasts.run())
