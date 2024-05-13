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

b=database_get(f'''SELECT pkl.leto_id, ((Meritev/cast(Stopnja_samozadostnosti as float))*Željena_stopnja_samozadostnosti)/pkl.Meritev_na_enoto as kolicnik 
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

sum=database_get('SELECT SUM(Meritev) as skupaj FROM podkategorija_kmečki_pridelki_leto WHERE leto_id=2022')
print(sum)
c=database_get(f'''SELECT   round(cast(meritev as float)/{sum[0][0]},6) as delez
            FROM 
                podkategorija_kmečki_pridelki_leto pkl
            
            WHERE pkl.leto_id=2023
            ;
            ''')
#print(database_get('SELECT kkp.Željena_stopnja_samozadostnosti,pkp.naziv FROM podkategorija_kmečki_pridelki pkp JOIN kategorija_kmečki_pridelk kkp ON pkp.kategorija_id=kkp.kategorija_id'))

for int in c:
    print(int)
