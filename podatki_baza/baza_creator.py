import sqlite3
import pandas as pd


# Connect to a new SQLite database
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Create a table named 'leta' with 'leto_id' and 'naziv' columns, both integers
cur.execute('''
CREATE TABLE kategorija_kmečki_pridelki (
    kategorija_id INTEGER,
    Naziv VARCHAR(100),
    Željena_stopnja_samozadostnosti integer
)
''')
leto_id;pod_kategorija_id;meritev_na_enoto;meritev

# Commit changes and close the connection
conn.commit()
conn.close()


