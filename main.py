# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali
import Pyodbc

current_path = Pyodbc.path.dirname(__file__)

conn_str = (r'DRIVER={microsoft access driver (*.mdb, *.accdb)};'
r'dbq=' + current_path + '\medlemsregistrer.accdb;')

conn = Pyodbc.connect(conn_str)
cursor = conn.cursor()
sql_str = "select * from kontaktinfo_python"
cursor.execute(sql_str)
for row in cursor.fetchall():
    print(row)

    
