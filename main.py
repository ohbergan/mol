# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali

from turtle import clear
import pyodbc
import os

current_path = os.path.dirname(__file__)

conn_str = (r'DRIVER={microsoft access driver (*.mdb, *.accdb)};'
            r'dbq=' + current_path + '\medlemsregister.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
    
def close():
    os.system=("cls")

def menu5():
    clear()
    print("betalte medlemmer.")
    ans=input("\velg tall.")

    if ans == "1":

        print("her kan du se medlemene som er full eller støtte .")
        sql_str="INSERT INTO Medlemstyper ( MTypeNavn, Kontigent ) SELECT Medlemstyper.MTypeNavn, Medlemstyper.Kontigent FROM Medlemstyper;"
        cursor.execute(sql_str)


    elif ans == "2":
        print("hvem vil du slette?")
        sql_str=f"DELETE FROM medlemmer where MedlemsID like {input}"
        cursor.execute(sql_str)

    
    elif ans == "3":
        print("hvor mye vil du ligge i kortinget?")
        sql_str=""
        cursor.execute(sql_str)


    elif ans == "4":
        print("skriv ut csv-fil her.")
        sql_str=""
        cursor.execute(sql_str)

    elif ans == "5":
        print("tilbake til hovedmenyen.")
        sql_str="cls"
        cursor.execute(sql_str)


    



    
