# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali

from turtle import clear
import pyodbc
import os
import csv


header = ['navn', 'telefon', 'E-post', 'fodselsdato']
data = [
    ['Laila Bakken', 12456819, '', '04.04.1952'],
    
    ['Stig Bjørnsen', 25435895, 'stig120@c2i.net', '31.03.1936'],
    
    ['Liv Borgen', 26525554, '', '23.09.1954'],
    
    ['Kari Dale', 32562156, '', '26.02.1976'],
    
    ['Åge Dalen', 25453855, 'dalen@c2i.net', '23.09.1998'],
   
    ['Arve Dalvik', 95255655, 'a.dalvik@tiscali.no', '05.01.1967'],
   
    ['Geir Fjell ', 65246524, 'gfjell@hotmail.com', '11.07.1946'],
   
    ['Gjertrud Fjell ', 65645544, '', '09.09.1980'],
   
    ['Kristoffer Fjell ', 87688838, 'krisfjell@c2i.net', '05.09.1943'],
  
    ['Mona Gran ', 45525955, 'mona.gran@start.no', '19.05.1961'],
  
    ['Mons Larsen ', 55289358, 'monsla@online.no', '31.12.1975'],
  
    ['Line Li ', 25462888, 'lineli@start.no', '16.12.1980'],
 
    ['Anita Lia ', 25465863, 'anita124@online.no', '06.08.1936'],
  
    ['Petter Lia ', 45343543, 'petterlia@tiscali.no', '14.09.1965'],
  
    ['Jonas Moen ', 32564879, 'jmoen@start.no', '07.08.1947'],
  
    ['Beate Monsen ', 25642516, 'beate2000@hotmail.com', '30.10.1978'],
  
    ['Anette Nilsen ', 56745464, 'anetten@start.no', '02.12.1965'],
  
    ['Janne Nilsen ', 65245621, 'janne100@tiscali.no', '19.08.1947'],
   
    ['Kåre Paulsen ', 25612558, 'kpaul@c2i.net', '03.11.1956'],
  
    ['Amund Pettersen ', 12356625, 'AmundP@online.no', '30.06.1940'],
 
    ['Petter Svendsen ', 65232165, 'petter1024@online.no', '16.01.1966'],
 
    ['Johnny Vik ', 21546872, 'jovik@start.no', '09.02.1968'],
 
 
    ['Birger Øverdal', 25632565, 'birger@hotmail.com', '06.02.1953'],
 
    ['Kari Åsen', 23245245, 'kari@msn.com', '13.03.1975'],

    ['Rut Hauge', 33445566, 'ruthauge@online.no', '28.12.1976'],
  
    ['Birger Knudsen', 33545678, '', '12.05.1974'],
  
    ['Oddbjørn Lunn',33976545, '', '23.06.1956'],
  
    ['Anne Hem Vestlie', 34565678, 'annehem@tiscali.no', '20.08.1996']
]

with open('medlemsliste.csv', 'w', encoding='UTF8', newline='') as f:
    
    writer = csv.writer(f)
    
    writer.writerow(header)

    writer.writerows(data)

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
        sql_str=f"{input}*(1+10/100)"
        cursor.execute(sql_str)


    elif ans == "4":
        print("skriv ut csv-fil her.")
        sql_str="SELECT Medlemmer.[Fornavn] & " " & [Etternavn] AS Navn, Medlemmer.Telefon, Medlemmer.[E-post], Medlemmer.FødselsdatoFROM Poststeder INNER JOIN (Medlemstyper INNER JOIN Medlemmer ON Medlemstyper.MTypeID = Medlemmer.MTypeID) ON Poststeder.Postnr = Medlemmer.Postnr;"
        cursor.execute(sql_str)

    elif ans == "5":
        print("tilbake til hovedmenyen.")
        clear()


    def menu6():
        clear(close)



    



    
