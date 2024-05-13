import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# SQL query to fetch all data from the table named 'table'
sql_query = "SELECT * FROM leta"

try:
    # Execute the SQL command
    cursor.execute(sql_query)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        print(row)  # Here, you can process each row as needed
except Exception as e:
    print("Error: unable to fetch data", e)

# Close the database connection
conn.close()
