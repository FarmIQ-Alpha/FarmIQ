import sqlite3
import pandas as pd

def database(query):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()


def database_get(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        return("Error: unable to fetch data", e)
    conn.close()

def database_canculator(kategorija):
    id = database_get(f'SELECT kategorija_id FROM kategorija_kmečki_pridelki WHERE Naziv = "{kategorija}"')
    sum_kategory = database_get(f'''SELECT 
         SUM(pkl.Meritev) AS total_meritev
        FROM 
            podkategorija_kmečki_pridelki_leto pkl
        JOIN 
            podkategorija_kmečki_pridelki pk ON pkl.podkategorija_id = pk.podkategorija_id
        WHERE 
         pkl.leto_id >= strftime("%Y", "now") - 2
            AND pk.kategorija_id = {id[0][0]};
        ''')
    print(sum_kategory)
    temp = database_get(f'SELECT naziv, SUM(Meritev)/{float(sum_kategory[0][0])} AS total_meritev FROM podkategorija_kmečki_pridelki_leto pkl JOIN podkategorija_kmečki_pridelki pk ON pkl.podkategorija_id = pk.podkategorija_id  WHERE leto_id >= strftime("%Y", "now") - 2 GROUP BY pk.podkategorija_id ORDER BY pk.podkategorija_id')
    print(temp)


