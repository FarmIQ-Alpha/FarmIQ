from Napoved_Spletnih_Strani.web_predict import WebScraper
from V1_subvencije_razdeljevalnik.algoritem_napoved import Izdelek, Algoritem

print('WebScraper:')
webscraper = WebScraper()
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
