class Izdelek:
    def __init__(self, ime, lanska_cena, donos):
        self.ime = ime
        self.lanska_cena = lanska_cena
        self.donos = donos

class Algoritem:
    def __init__(self, izdelek1, izdelek2, ponder, napoved_sursa, napoved_tujih, skupno_zemljisce, budget):
        self.izdelek1 = izdelek1
        self.izdelek2 = izdelek2
        self.ponder = ponder
        self.napoved_sursa = napoved_sursa
        self.napoved_tujih = napoved_tujih
        self.skupno_zemljisce = skupno_zemljisce
        self.budget = budget

    def izracun(self):
        # 1. Določi odstotke za oba produkta
        odstotek1, odstote0k2 = self.ponder, 100 - self.ponder

        # 2. Izračunaj prihodnjo ceno za vsako vrsto pšenice
        prihodnja_cena1 = self.napoved_sursa + self.napoved_tujih / 2
        prihodnja_cena2 = self.napoved_sursa + self.napoved_tujih / 2

        # 3. Izračunaj pričakovano povečanje cen za obe vrsti pšenice
        povecanje_cen1 = self.izdelek1.lanska_cena + prihodnja_cena1 / 2
        povecanje_cen2 = self.izdelek2.lanska_cena + prihodnja_cena2 / 2

        # 4. Določi alocirane deleže njiv na podlagi odstotkov in donosa
        alocirani_delez1 = (odstotek1 / 100) * (self.skupno_zemljisce / self.izdelek1.donos)
        alocirani_delez2 = (odstotek2 / 100) * (self.skupno_zemljisce / self.izdelek2.donos)

        # 5. Izračunaj skupno vrednost subvencije za vsak produkt
        subvencija1 = self.budget * (alocirani_delez1 / self.skupno_zemljisce) * povecanje_cen1
        subvencija2 = self.budget * (alocirani_delez2 / self.skupno_zemljisce) * povecanje_cen2

        # 6. Izračunaj velikost subvencije na hektar za vsak produkt
        velikost_subvencije_na_hektar1 = subvencija1 / alocirani_delez1
        velikost_subvencije_na_hektar2 = subvencija2 / alocirani_delez2

        return {
            'prihodnja_cena_psenica1': prihodnja_cena1,
            'prihodnja_cena_psenica2': prihodnja_cena2,
            'povecanje_cen_psenica1': povecanje_cen1,
            'povecanje_cen_psenica2': povecanje_cen2,
            'subvencija_psenica1': subvencija1,
            'subvencija_psenica2': subvencija2,
            'velikost_subvencije_na_hektar1': velikost_subvencije_na_hektar1,
            'velikost_subvencije_na_hektar2': velikost_subvencije_na_hektar2
        }


if __name__ == "__main__":
    izdelek1 = Izdelek('psenica', 2.00, 500)
    izdelek2 = Izdelek('koruza', 1.90, 450)
    a = Algoritem(izdelek1, izdelek2, 75, 1.10, .05, 1000, 100000)
    rezultat = a.izracun()
    
    for ključ, vrednost in rezultat.items():
        print(ključ, vrednost)
