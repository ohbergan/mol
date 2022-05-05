# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali

import pyodbc
import os





current_path = os.path.dirname(__file__)

conn_str = (r'DRIVER={microsoft access driver (*.mdb, *.accdb)};'
            r'dbq=' + current_path + '\medlemsregister.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
    

  




def clear():
     command = 'clear'
     if os.name in ('nt', 'dos'): 
         command = 'cls'
     os.system(command)




def menu5():
    print("\nvedlikehold\n")
    print("1. \nLegg til en medlemstype (Fullt medlem, støttemedlem osv)")
    print("2. \nSlett en medlemstype")
    print("3. \nØk kontingentenmed 10%")
    print("4. \nSkrive medlemslisten ut til en csv-fil")
    print("5. \ntilbake til hovedmeny")
    ans = input("\nhva vil du velge i dag?\n")

    if ans == "1":
        print("Legg til en medlemstype (Fullt medlem, støttemedlem osv).")
        MTypeNavn = int(input("\nligg inn MTypenavn: \n"))
        Kontigent = int(input("\nligg inn kotigent: \n"))
        sql_str=f"INSERT INTO Medlemstyper (MTypeNavn, Kontigent) VALUES ('{MTypeNavn}','{Kontigent}');"
        cursor.execute(sql_str)
        input()


    elif ans == "2":
        print("Slett en medlemstype?")
        MTypeID = int(input("\nMTypeID skal bli slettes: \n"))
        sql_str=f"DELETE FROM MedlemsType WHERE MTypeID like {MTypeID}"
        cursor.execute(sql_str)

    
    elif ans == "3":
        print("hvor mye vil du ligge i kortinget?")
        sql_str=f"select {input}*(1+10/100)"
        cursor.execute(sql_str)


    elif ans == "4":
        print("Skrive medlemslisten ut til en csv-fil.")
        sql_str="SELECT Medlemmer.[Fornavn] & " " & [Etternavn] AS Navn, Medlemmer.Telefon, Medlemmer.[E-post], Medlemmer.FødselsdatoFROM Poststeder INNER JOIN (Medlemstyper INNER JOIN Medlemmer ON Medlemstyper.MTypeID = Medlemmer.MTypeID) ON Poststeder.Postnr = Medlemmer.Postnr;"
        cursor.execute(sql_str)

        
           

     
    



menu5()

def menu6():
    clear()



    



    
