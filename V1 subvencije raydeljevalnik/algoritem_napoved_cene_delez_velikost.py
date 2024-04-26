def lanska_povprecna_cena(cena):
    return cena

def prihodnja_cena(napoved_sursa, napoved_tujih):
    return napoved_sursa + napoved_tujih / 2

def pricakovano_povecanje_cen(cena_lani, cena_prihodnje):
    return lanska_povprecna_cena(cena_lani) + cena_prihodnje / 2

def donos_posameznega_produkta(donos):
    return donos

def ponder(psenica1, psenica2):
    try:
        odstotek1 = float(input(f"Vnesite odstotek za '{psenica1}': "))
        if odstotek1 < 0 or odstotek1 > 100:
            print("Vnesite veljaven odstotek med 0 in 100.")
            return None
        odstotek2 = 100 - odstotek1
        print(f"{odstotek1}% za {psenica1} in {odstotek2}% za {psenica2}.")
        return odstotek1, odstotek2
    except ValueError:
        print("Prosimo vnesite številčno vrednost za odstotek.")
        return None

def skupna_zemljišča(velikost_zemljišč):
    return velikost_zemljišč

def količina_subvencij(budget):
    return budget



def algoritem(lanska_cena_psenica1, lanska_cena_psenica2, napoved_sursa, napoved_tujih, donos_psenica1, donos_psenica2, skupno_zemljisce, budget):
    # 1. Določi odstotke za oba produkta
    psenica1, psenica2 = 'psenica1', 'psenica2'
    odstotki = ponder(psenica1, psenica2)
    if not odstotki:
        return "Algoritem ni izvedel izračuna zaradi neveljavnega vnosa."

    odstotek1, odstotek2 = odstotki

    # 2. Izračunaj prihodnjo ceno za vsako vrsto pšenice
    prihodnja_cena1 = prihodnja_cena(napoved_sursa, napoved_tujih)
    prihodnja_cena2 = prihodnja_cena(napoved_sursa, napoved_tujih)

    # 3. Izračunaj pričakovano povečanje cen za obe vrsti pšenice
    povecanje_cen1 = pricakovano_povecanje_cen(lanska_cena_psenica1, prihodnja_cena1)
    povecanje_cen2 = pricakovano_povecanje_cen(lanska_cena_psenica2, prihodnja_cena2)

    # 4. Določi alocirane deleže njiv na podlagi odstotkov in donosa
    alocirani_delez1 = (odstotek1 / 100) * (skupno_zemljisce / donos_psenica1)
    alocirani_delez2 = (odstotek2 / 100) * (skupno_zemljisce / donos_psenica2)

    # 5. Izračunaj skupno vrednost subvencije za vsak produkt
    subvencija1 = budget * (alocirani_delez1 / skupno_zemljisce) * povecanje_cen1
    subvencija2 = budget * (alocirani_delez2 / skupno_zemljisce) * povecanje_cen2

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
    rezultat = algoritem(
        lanska_cena_psenica1=2.00, # Primer lanske cene za psenica1
        lanska_cena_psenica2=1.90, # Primer lanske cene za psenica2
        napoved_sursa=1.10,  # Primer napovedi cene SURS
        napoved_tujih=0.05,  # Primer tuje napovedi
        donos_psenica1=500,  # Primer donosa za psenica1
        donos_psenica2=450,  # Primer donosa za psenica2
        skupno_zemljisce=1000,  # Skupna velikost zemljišč v hektarih
        budget=100000  # Proračun za subvencije
    )
    print(rezultat)
