# Oppgave 1, 2 & 3 - Ole Halvor

import pyodbc
import os

# Lagrer path til det aktive scriptet i variabelen current_path
current_path = os.path.dirname(__file__)

# connection-strengen
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + current_path + '\Medlemsregister.accdb;')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


def menu1():
    sql_str = "select MedlemsID, Fornavn, Etternavn, Mobil from Medlemmer"
    cursor.execute(sql_str)
    # Prints the cursor formatted as a table
    # First the table header
    table_cell_formatting = "{:<8} {:<20} {:<12}"
    print(table_cell_formatting.format('ID', 'Navn', 'Mobil'))
    print(table_cell_formatting.format('--------',
          '-------------------', '------------'))
    # Print all the rows in a table
    for row in cursor.fetchall():
        print(table_cell_formatting.format(
            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A", row[3] or "N/A"))
    print()  # a blank line


menu1()

# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali
