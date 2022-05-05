import csv
import pyodbc
import os
from datetime import datetime

# Saves the path for the running script so that it can be used to reference files
current_path = os.path.dirname(__file__)

# The connection string tells PYODBC to connect to the database
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + current_path + '\Medlemsregister.accdb;')

# Connect to the database
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# A function used to clear the screen


def clearScreen():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def menu5():
            clearScreen()
            print("\nHovedmeny for endring av medlem\n")
            print("1. Legg til en medlemstype (Fullt medlem, støttemedlem osv)")
            print("2. Slett en medlemstype")
            print("3. Øk kontingentenmed 10%")
            print("4. Skrive medlemslisten ut til en csv-fil")
            print("5. Tilbake til Hovedmenyen")
            ans = input("\nHva ønsker du å gjøre? Velg tall.\n")


            if ans == "1":

                Medlemstype_navn = input("Navn på medlemstype: ")
                Kontigent = int(input("Pris på kontigent: "))


                cursor.execute(
                    f"INSERT INTO Medlemstyper (MTypeNavn, Kontigent) VALUES ('{Medlemstype_navn}', {Kontigent});")
                conn.commit()

            elif ans == "2":

                print("Her kan du slette en medlemstype")   
                Medlemstype_ID = int(input("\nMedlemstypeID til medlemstype som skal slettes: \n"))
                
                sql_str = f"DELETE FROM Medlemstyper WHERE MTypeID like {Medlemstype_ID}"
                cursor.execute(sql_str)
                conn.commit()

                print("Medlemstypen ble slettet!") 
                input("Trykk ENTER for å gå videre: ")

            elif ans == "3":
                mTypeId = int(input("\nOppgi MTypeID: \n"))
                sql_str =  f"UPDATE Medlemstyper SET Kontigent = Kontigent*1.1 WHERE MTypeID = {mTypeId}"
                cursor.execute(sql_str)
                conn.commit()

                print("Kontigenten er oppdatert med 10%!") 
                input("Trykk ENTER for å gå videre: ")

            elif ans =="4":
                 # Run an SQL qurey that selects a list of members

                sql_str = "select MedlemsID, Fornavn, Etternavn, Mobil from Medlemmer"

                cursor.execute(sql_str)

                # Store header and data info for the CSV
                header = ['memberid', 'first_name', 'last_name', 'mobile']
                data = []

                # Clear the screen
                clearScreen()

                # Add all table rows to data list
                for row in cursor.fetchall():
                    data.append([row[0], row[1] or "", row[2] or "", row[3] or ""])


                # Create CSV file
                with open('exports/members.csv', 'w', encoding='UTF8', newline='') as f:

                    # Create a writer
                    writer = csv.writer(f)

                    # Write header
                    writer.writerow(header)

                    # Write multiple rows
                    writer.writerows(data)


                print("CSV fil opprettet i exports mappen")
                input("Trykk ENTER for å gå videre: ")