from database import *
def score_kategory(zeljena_stopnja_samozadostnosti,indeksNapovedanihCen):
    zeljena_stopnja_samozadostnosti
    indeksNapovedanihCen
def IzračunajPotrebnoKoličino(kategorija,zeljena_stopnja_samozadostnosti):
    database_get('SELECT Meritev_na_enoto, FROM podkategorija_kmečki_pridelki pkp JOIN kategorija_kmečki_pridelki kkp on pkp.kategorija_id= kkp.kategorija_id ')

a=database_get(f'''SELECT 
             SUM(pkl.Meritev_na_enoto)/3 AS avrige_meritev
            FROM 
                podkategorija_kmečki_pridelki_leto pkl
            JOIN 
                podkategorija_kmečki_pridelki pk ON pkl.podkategorija_id = pk.podkategorija_id
            WHERE 
             pkl.leto_id >= strftime("%Y", "now") - 2 group by pkl.podkategorija_id;
            ''')
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

print(razdeli_proračun(10000000))


