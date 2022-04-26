# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali

from turtle import clear
import pyodbc
import os
import csv


header = ['fornavn', 'etternavn', 'telefon', 'E-post']
data = []

with open('medlemsregistrer.accdb', 'w', encoding='UTF8', newline='') as f:
    
    writer = csv.writer(f)
    
    writer.writerow(header)

    writer.writerow(data)

current_path = os.path.dirname(__file__)

conn_str = (r'DRIVER={microsoft access driver (*.mdb, *.accdb)};'
            r'dbq=' + current_path + '\medlemsregister.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
    
def close():
    os.system=("cls")

def menu5():
    clear()
    print("vedlikehold.")
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
        sql_str="SELECT Medlemmer.Fornavn, Medlemmer.Etternavn, Medlemmer.[E-post]FROM Poststeder INNER JOIN (Medlemstyper INNER JOIN Medlemmer ON Medlemstyper.MTypeID = Medlemmer.MTypeID) ON Poststeder.Postnr = Medlemmer.Postnr;"
        cursor.execute(sql_str)

    elif ans == "5":
        print("tilbake til hovedmenyen.")
        sql_str="cls"
        cursor.execute(sql_str)


    def menu6():
        clear(close)



    



    
