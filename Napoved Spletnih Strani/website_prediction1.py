from bs4 import BeautifulSoup
import pandas as pd
import requests

class WebScraper():
    def __init__(self):
        self.url = 'https://walletinvestor.com/commodity-forecast/wheat-prediction'
        self.target_class = 'kv-grid-table table table-hover table-bordered table-striped table-condensed kv-table-wrap'

    def get_table_from_website(self):
        """
        Gets table from the website
    
        Returns:
            BeautifulSoup: table
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find('table', class_=self.target_class)
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching data: {e}")

    def get_data_from_table(self, table):
        """
        Gets data from the table

        Args:
            BeautifulSoup: table

        Returns:
            DataFrame: data
        """
        data = []

        for row in table.find_all('tr'):
            cells = row.find_all(['th', 'td'])

            if len(cells) < 7 or "Date" in cells[1].get_text(strip=True):
                continue

            date = cells[1].get_text(strip=True)
            opening_price = float(cells[2].get_text(strip=True).split(':')[1])
            closing_price = float(cells[3].get_text(strip=True).split(':')[1])
            minimum_price = float(cells[4].get_text(strip=True).split(':')[1])
            maximum_price = float(cells[5].get_text(strip=True).split(':')[1])
            change = float(cells[6].get_text(strip=True).split(':')[1].split()[0])

            data.append([date, opening_price, closing_price, minimum_price, maximum_price, change])

        return pd.DataFrame(data, columns=['Date', 'Opening price', 'Closing price', 'Minimum price', 'Maximum price', 'Change'])

    def get_prediction(self, data, target_year=2024, option='Opening price'):
        """
        Gets average of the desired field. All the fields are Opening price, Closing price, Minimum price, Maximum price, Change

        Args:
            data (DataFrame): The data
            target_year (int): Targeted year, default 2024
            option (string): Desired field, defualt is Opeing price

        Returns:
            float: average of desired field
        """
        available_options = ['Date', 'Opening price', 'Closing price', 'Minimum price', 'Maximum price', 'Change']
        
        if option not in available_options:
            raise ValueError(f"Invalid option '{option}' provided. Available options: {', '.join(available_options)}")

        try:
            data['Date'] = data['Date'].astype(str)
            subset_data = data[data['Date'].str.contains(str(target_year))]

            average = subset_data[option].astype(float).mean()

            print(f"Average {option} for {target_year}: {average:.2f}")
            return average
        except KeyError:
            raise ValueError("Invalid option provided.")
        except Exception as e:
            raise RuntimeError(f"Error: {e}")

    def run(self, target_year=2024, option='Opening price'):
        """
        Gets prediction of the desired field. All the fields are Opening price, Closing price, Minimum price, Maximum price, Change

        Args:
            target_year (int): Targeted year, default 2024
            option (string): Desired field, defualt is Opeing price

        Returns:
            float: average of desired field
        """
        table = self.get_table_from_website()
        data = self.get_data_from_table(table)
        self.get_prediction(data, target_year, option)

if __name__ == '__main__':
    webscraper = WebScraper()
    webscraper.run()
