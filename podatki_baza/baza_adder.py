import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Path to your CSV file
csv_file_path = 'podatki_v_csv/leto_podkategorija.csv'

# Open the CSV file
with open(csv_file_path, newline='', encoding='windows-1250') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')

    # Skip the header row if your CSV has headers
    next(csvreader)

    insert_query = 'INSERT INTO podkategorija_kmečki_pridelki_leto (leto_id,podkategorija_id,Meritev_na_enoto,Meritev) VALUES (?,?,?,?)'




    # Insert each row from the CSV into the database
    for row in csvreader:
        try:
            cursor.execute(insert_query, row)
        except sqlite3.IntegrityError:
            print(f"Error occurred when inserting row: {row}")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted from CSV into database successfully.")
