from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
impo



class WebScraper1():
    def __init__(self):
        # kolicina v 50 t
        self.url = 'https://www.proplanta.de/Markt-und-Preis/MATIF-Weizen/'
        self.target_class = 'FARBE_LISTE_KOPF_DUNKEL_MITTE'

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

            if "Kontrakt" in cells[0].get_text(strip=True):
                continue

            kontrakt = cells[0].get_text(strip=True)
            schluss_Kurs = cells[1].get_text(strip=True)
            aktueller_Kurs = cells[3].get_text(strip=True)
            eröffnung = cells[5].get_text(strip=True)
            hoch = cells[6].get_text(strip=True)
            tief = cells[7].get_text(strip=True)
            geld = cells[12].get_text(strip=True)

            schluss_Kurs = float(schluss_Kurs) if schluss_Kurs not in ['-', ''] else 0.0
            aktueller_Kurs = float(aktueller_Kurs) if aktueller_Kurs not in ['-', ''] else 0.0
            eröffnung = float(eröffnung) if eröffnung not in ['-', ''] else 0.0
            hoch = float(hoch) if hoch not in ['-', ''] else 0.0
            tief = float(tief) if tief not in ['-', ''] else 0.0
            geld = float(geld) if geld not in ['-', ''] else 0.0

            data.append([kontrakt, schluss_Kurs, aktueller_Kurs, eröffnung, hoch, tief, geld])

        return pd.DataFrame(data, columns=['Kontrakt', 'Schluss_Kurs', 'Aktueller_Kurs', 'Eröffnung', 'Hoch', 'Tief', 'Geld'])

    def get_prediction(self, data, target_year=2025, option='Schluss_Kurs'):
        """
        Gets average of the desired field. All the fields are Opening price, Closing price, Minimum price, Maximum price, Change

        Args:
            data (DataFrame): The data
            target_year (int): Targeted year, default 2025
            option (string): Desired field, defualt is Schluss_Kurs

        Returns:
            float: average of desired field
        """
        available_options = ['Kontrakt', 'Schluss_Kurs', 'Aktueller_Kurs', 'Eröffnung', 'Hoch', 'Tief', 'Geld']
        
        if option not in available_options:
            raise ValueError(f"Invalid option '{option}' provided. Available options: {', '.join(available_options)}")

        try:
            data['Kontrakt'] = data['Kontrakt'].astype(str)
            subset_data = data[data['Kontrakt'].str.contains(str(target_year))]

            average = subset_data[option].astype(float).mean()

            #print(f"Average {option} for {target_year}: {average:.2f}")
            return average
        except KeyError:
            raise ValueError("Invalid option provided.")
        except Exception as e:
            raise RuntimeError(f"Error: {e}")

    def run(self, target_year=2025, option='Schluss_Kurs'):
        """
        Gets prediction of the desired field. All the fields are Opening price, Closing price, Minimum price, Maximum price, Change

        Args:
            target_year (int): Targeted year, default 2025
            option (string): Desired field, defualt is Schluss_Kurs

        Returns:
            float: average of desired field
        """
        table = self.get_table_from_website()
        data = self.get_data_from_table(table)
        return self.get_prediction(data, target_year, option)

if __name__ == '__main__':
    #sleep(5)
    webscraper = WebScraper1()
    import json
    data = {"hello": webscraper.run()}
    print(json.dumps(data))
