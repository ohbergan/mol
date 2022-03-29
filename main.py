# Oppgave 1, 2 & 3 - Ole Halvor


# Oppgave 4 - Emil

import os
import pyodbc

# Lagrer path til det aktive scriptet i variabelen current_path

current_path = os.path.dirname(__file__)

# connection-strengen

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + current_path + '\Medlemsregister.accdb;')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function used for clearing the terminal
def clear():
    os.system('cls')

   
# The program starts here
def menu4():
    clear()
    print("\nHovedmeny for Vedlikehold medlemmer\n")
    print("\n1. Legg til et nytt medlem")
    print("\n2. Slett et medlem")
    print("\n3. Registrere om et medlem har betalt kontigenten")
    print("\n4. Endre data for et medlem, f.eks, endre adresse")
    print("\n5. Tilbake til hovedmenyen")
    ans=input("\nHva ønsker du å gjøre? Velg tall.")


    if ans == "1":
        print("Her kan du legge til et nytt medlem")
        sql_str = f"CREATE USER '{input}' for Medlemsregister"
        cursor.execute(sql_str)
    
    elif ans == "2":
        print("Her kan du slette et medlem")
        sql_str = f"DELETE FROM Medlemsregister where USER_ID = '{input}'"
        cursor.execute(sql_str)
    
    elif ans == "3":
        print("Her ser du om et medlem har betalt kontigenten")
    
    elif ans == "4":
        print("Her kan du endre data til et medlem (adresse, tlf osv)")
    
    elif ans == "5":
        print("Trykk [ENTER] for å fortsette!")
    
menu4()
        
# Oppgave 5 & 6 - Ali
