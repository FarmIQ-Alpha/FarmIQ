from database import *
def razdeli_proračun (proracun):
    sum = database_get('SELECT SUM(Meritev) as skupaj FROM podkategorija_kmečki_pridelki_leto WHERE leto_id=2022')
    potrebna_površina=database_get(f'''
    SELECT 
        pk.naziv,
        round(((Meritev/cast(Stopnja_samozadostnosti as float))*Željena_stopnja_samozadostnosti)/pkl.Meritev_na_enoto,0) as potrebna_površina, 
        round(({proracun}*(cast(pkl.meritev as float)/{sum[0][0]}))/(((Meritev/cast(Stopnja_samozadostnosti as float))*Željena_stopnja_samozadostnosti)/pkl.Meritev_na_enoto),2) as subvencija_na_polščino 
            FROM 
                podkategorija_kmečki_pridelki_leto pkl
            JOIN 
                podkategorija_kmečki_pridelki pk ON pkl.podkategorija_id = pk.podkategorija_id   
            JOIN
                kategorija_kmečki_pridelki kkp on pk.kategorija_id=kkp.kategorija_id
            JOIN
            kategorija_leto kl ON pk.kategorija_id=kl.kategorija_id and  pkl.leto_id=kl.leto_id
            
            WHERE pkl.leto_id=2022
            ;
            ''')
    zahtevana_površina=0
    skupna_količina_kmetiskih_zemljišč_v_sloveniji=595000
    for int in potrebna_površina:
        zahtevana_površina=zahtevana_površina+int[1]

    if zahtevana_površina > skupna_količina_kmetiskih_zemljišč_v_sloveniji:
        napaka=f"Napaka izbrali ste željene stopnje samozadostnosti, ki presega kapacitete slovenkega kmetistva želeli ste porabiti {a} hektarjev trenutno pa jih je registriranih le 595 000"

        return napaka

    return(potrebna_površina)

#spremeni število med oklepaji razdeli_proračun da določiš poljubni proračun az subvencije
potrebna_površina=razdeli_proračun(10000000)
for int in potrebna_površina:
    print(f"ime polščine: {int[0]}, zahtevana površina : {int[1]} ha , subvencija na hektar: {int[2]} eur/ha")



