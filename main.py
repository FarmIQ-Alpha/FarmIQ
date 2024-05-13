from Napoved_Spletnih_Strani.web_predict import WebScraper
from Napoved_Spletnih_Strani.web_predict1 import WebScraper1
from V1_subvencije_razdeljevalnik.algoritem_napoved import Izdelek, Algoritem
from ARIMA_models.Napoved_cene_stari_podatki2 import PredictPrices
from ARIMA_models.Napoved_kolicine_stari_podatki1 import PredictQuantity

print('WebScraper:')
webscraper = WebScraper()
webscraper.run()

print('-' * 30)

print('WebScraper1:')
webscraper = WebScraper1()
webscraper.run()

print('-' * 30)

print('Algoritem za napoved cen in povrsine:')
izdelek1 = Izdelek('psenica', 2.00, 500)
izdelek2 = Izdelek('koruza', 1.90, 450)
a = Algoritem(izdelek1, izdelek2, 75, 1.10, .05, 1000, 100000)
rezultat = a.izracun()

for ključ, vrednost in rezultat.items():
    print(ključ, vrednost)

print('-' * 30)

print("Forecast data prices:")
forecasts = PredictPrices()
print(forecasts.run())

print('-' * 30)

print("Forecast data quantity:")
forecasts = PredictQuantity()
print(forecasts.run())