# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali
from select import select
import pyodbc
import os

current_path = os.path.dirname(__file__)

conn_str = (r'DRIVER={microsoft access driver (*.mdb, *.accdb)};'
            r'dbq=' + current_path + '\medlemsregister.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
for row in cursor.fetchall():
    print(row)
    
def close():
    os.system=("cls")

def menu5_1():



   print("her kan du se medlemene.")
   sql_str="INSERT INTO Medlemstyper ( MTypeNavn, Kontigent ) SELECT Medlemstyper.MTypeNavn, Medlemstyper.Kontigent FROM Medlemstyper;"
   cursor.execute(sql_str)

    



    
