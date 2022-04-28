# Oppgave 1, 2 & 3 - Ole Halvor
import pyodbc
import os
from datetime import datetime

# A class used to modify a string


class StrMod:
    def black(str):
        return f"\033[30m{str}\033[0m"

    def red(str):
        return f"\033[31m{str}\033[0m"

    def green(str):
        return f"\033[32m{str}\033[0m"

    def yellow(str):
        return f"\033[33m{str}\033[0m"

    def blue(str):
        return f"\033[34m{str}\033[0m"

    def magenta(str):
        return f"\033[35m{str}\033[0m"

    def cyan(str):
        return f"\033[36m{str}\033[0m"

    def gray(str):
        return f"\033[37m{str}\033[0m"

    def bg_black(str):
        return f"\033[40m{str}\033[0m"

    def bg_red(str):
        return f"\033[41m{str}\033[0m"

    def bg_green(str):
        return f"\033[42m{str}\033[0m"

    def bg_yellow(str):
        return f"\033[43m{str}\033[0m"

    def bg_blue(str):
        return f"\033[44m{str}\033[0m"

    def bg_magenta(str):
        return f"\033[45m{str}\033[0m"

    def bg_cyan(str):
        return f"\033[46m{str}\033[0m"

    def bg_gray(str):
        return f"\033[47m{str}\033[0m"

    def bg_test(str):
        return f"\033[15m{str}\033[0m"

    def bold(str):
        return f"\033[1m{str}\033[22m"

    def italic(str):
        return f"\033[3m{str}\033[23m"

    def underline(str):
        return f"\033[4m{str}\033[24m"

    def reverse_color(str):
        return f"\033[7m{str}\033[27m"


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


# The first menu item
def menu1():
    # Clear the screen
    clearScreen()

    # Run an SQL qurey that selects a list of members
    sql_str = "select MedlemsID, Fornavn, Etternavn, Mobil from Medlemmer"
    cursor.execute(sql_str)

    # Create the table formatting
    table_header_formatting = StrMod.bold(StrMod.blue("{:<9} {:<20} {:<12}"))
    table_divider_formatting = "{:<9} {:<20} {:<12}"
    table_row_formatting = StrMod.blue("{:<9} ") + "{:<20} {:<12}"

    # Print the table header to console
    print(table_header_formatting.format('MedlemsID', 'Navn', 'Mobil'))
    print(table_divider_formatting.format('---------',
          '-------------------', '------------'))

    # Print all table rows
    for row in cursor.fetchall():
        print(table_row_formatting.format(
            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A", row[3] or "N/A"))

    # Create a input to stop the script from continuing without the user wanting to continue
    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))


# The second menu item
def menu2():
    # Clear the screen
    clearScreen()

    # Get memberid from the user
    memberID = input("MedlemsID: ")

    # Run an SQL qurey that gets information from the member specified in the memberID variable
    sql_str = "select top 1 * from Medlemmer where MedlemsID like "+memberID
    cursor.execute(sql_str)

    # Clear the screen
    clearScreen()

    # Print the information found during the SQL qurey
    for row in cursor.fetchall():
        print(StrMod.bold("MEDLEMSINFORMASJON"))
        print(f"{StrMod.bold(StrMod.blue('MedlemsID:'))} {row[0] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Fornavn:'))} {row[1] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Etternavn:'))} {row[2] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Adresse:'))} {row[3] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Postnr:'))} {row[4] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Telefon:'))} {row[5] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Mobil:'))} {row[6] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('E-post:'))} {row[7] or 'N/A'}")
        print(f"{StrMod.bold(StrMod.blue('Fødelsdato:'))} {row[8] or 'N/A'}")
        print(
            f"{StrMod.bold(StrMod.blue('MedlemstypeID:'))} {row[9] or 'N/A'}")
        print(
            f"{StrMod.bold(StrMod.blue('Betalt:'))} {'Ja' if row[10] == True else 'Nei'}")

    # Create a input to stop the script from continuing without the user wanting to continue
    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))


# The third menu item
def menu3():
    # Create a loop to avoid exiting the submenu
    while True:
        # Clear the screen
        clearScreen()

        # Print the selections
        print(StrMod.bold("SPØRRINGER"))
        print(f"[{StrMod.blue('1')}] Medlemmer med ubetalt kontigent")
        print(f"[{StrMod.blue('2')}] Medlemmer som er pensjonister (eldre enn 67 år)")
        print(
            f"[{StrMod.blue('3')}] Medlemmer som er unge voksene (mellom 18 og 30 år gamle)")
        print(f"[{StrMod.blue('4')}] Finn medlemmer eldre enn...")
        print(f"[{StrMod.blue('5')}] Finn medlemmer som bor i...")
        print(f"[{StrMod.blue('6')}] Gjennomsnittlig alder på medlemmer")
        print(f"[{StrMod.blue('7')}] Medlemmer i Bestfold og Telemark")
        print(f"[{StrMod.blue('8')}] Tibalke til hovedmenyen")

        # Use try to handle input errors
        try:
            # Get menu choice from the user and store it in a variable
            menu_choice = int(input(StrMod.bold("Menyvalg:")+" "))

            # Check that the menu choice is valid
            if menu_choice > 0 and menu_choice <= 8:
                # User selected menu choice 1, run the appropiate code
                if menu_choice == 1:
                    # Run an SQL qurey that selects a list of members
                    sql_str = "select MedlemsID, Fornavn, Etternavn from Medlemmer where Betalt=False"
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Create the table formatting
                    table_header_formatting = StrMod.blue(
                        "{:<9} {:<20}")
                    table_divider_formatting = "{:<9} {:<20}"
                    table_row_formatting = StrMod.blue(
                        "{:<9} ") + "{:<20}"

                    # Print the table header to console
                    print(table_header_formatting.format(
                        'MedlemsID', 'Navn', 'Mobil'))
                    print(table_divider_formatting.format('---------',
                                                          '-------------------'))
                    # Print all table rows
                    for row in cursor.fetchall():
                        print(table_row_formatting.format(
                            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 2, run the appropiate code
                elif menu_choice == 2:
                    # Run an SQL qurey that selects a list of members
                    sql_str = "select MedlemsID, Fornavn, Etternavn from Medlemmer where (((Int((Date()-[Fødselsdato])/365))>67))"
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Create the table formatting
                    table_header_formatting = StrMod.blue(
                        "{:<9} {:<20}")
                    table_divider_formatting = "{:<9} {:<20}"
                    table_row_formatting = StrMod.blue(
                        "{:<9} ") + "{:<20}"

                    # Print the table header to console
                    print(table_header_formatting.format(
                        'MedlemsID', 'Navn', 'Mobil'))
                    print(table_divider_formatting.format('---------',
                                                          '-------------------'))

                    # Print all table rows
                    for row in cursor.fetchall():
                        print(table_row_formatting.format(
                            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 3, run the appropiate code
                elif menu_choice == 3:
                    # Run an SQL qurey that selects a list of members
                    sql_str = "select MedlemsID, Fornavn, Etternavn, Fødselsdato from Medlemmer WHERE (((Int((Date()-[Fødselsdato])/365))<30 And (Int((Date()-[Fødselsdato])/365))>18))"
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Create the table formatting
                    table_header_formatting = StrMod.blue(
                        "{:<9} {:<20}")
                    table_divider_formatting = "{:<9} {:<20}"
                    table_row_formatting = StrMod.blue(
                        "{:<9} ") + "{:<20}"

                    # Print the table header to console
                    print(table_header_formatting.format(
                        'MedlemsID', 'Navn', 'Mobil'))
                    print(table_divider_formatting.format('---------',
                                                          '-------------------'))

                    # Print all table rows
                    for row in cursor.fetchall():
                        print(table_row_formatting.format(
                            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 4, run the appropiate code
                elif menu_choice == 4:
                    # Clear the screen
                    clearScreen()

                    # Create a loop to let users retry if they fail to write the age correctly
                    while True:
                        # Use try to handle input errors
                        try:
                            # Get age from the user and store it in a variable
                            age_input = int(
                                input(StrMod.bold("Finn medlemmer eldre enn:")+" "))

                            # Run an SQL qurey that selects a list of members
                            sql_str = "select MedlemsID, Fornavn, Etternavn, Fødselsdato from Medlemmer WHERE (((Int((Date()-[Fødselsdato])/365))>"+str(
                                age_input)+"))"
                            cursor.execute(sql_str)

                            # Clear the screen
                            clearScreen()

                            # Create the table formatting
                            table_header_formatting = StrMod.blue(
                                "{:<9} {:<20}")
                            table_divider_formatting = "{:<9} {:<20}"
                            table_row_formatting = StrMod.blue(
                                "{:<9} ") + "{:<20}"

                            # Print the table header to console
                            print(table_header_formatting.format(
                                'MedlemsID', 'Navn', 'Mobil'))
                            print(table_divider_formatting.format('---------',
                                                                  '-------------------'))

                            # Print all table rows
                            for row in cursor.fetchall():
                                print(table_row_formatting.format(
                                    row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                            # Create a input to stop the script from continuing without the user wanting to continue
                            input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                            # Stop the loop as the function was completed succesfully
                            break
                        except ValueError:
                            # Let the user know what was wrong
                            print("Du må oppgi et tall")

                # User selected menu choice 5, run the appropiate code
                elif menu_choice == 5:
                    # Get city from the user and store it in a variable
                    city_input = input(StrMod.bold(
                        "Finn medlemmer som bor i:")+" ").upper()

                    # Run an SQL qurey that selects a list of members
                    sql_str = f"select Medlemmer.MedlemsID, Medlemmer.Fornavn, Medlemmer.Etternavn, Poststeder.Poststed FROM Poststeder INNER JOIN Medlemmer ON Poststeder.Postnr = Medlemmer.Postnr WHERE (((Poststeder.Poststed)='{city_input}'))"
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Create the table formatting
                    table_header_formatting = StrMod.blue(
                        "{:<9} {:<20}")
                    table_divider_formatting = "{:<9} {:<20}"
                    table_row_formatting = StrMod.blue(
                        "{:<9} ") + "{:<20}"

                    # Print the table header to console
                    print(table_header_formatting.format(
                        'MedlemsID', 'Navn', 'Mobil'))
                    print(table_divider_formatting.format('---------',
                                                          '-------------------'))
                    # Print all table rows
                    for row in cursor.fetchall():
                        print(table_row_formatting.format(
                            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 6, run the appropiate code
                elif menu_choice == 6:
                    # Run an SQL qurey that gets an average
                    sql_str = f"select avg((Int((Date()-[Fødselsdato])/365))) FROM Medlemmer "
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Print the average onto the users screen
                    for row in cursor.fetchall():
                        print(StrMod.bold(StrMod.blue(
                            "Gjennomsalder på medlemmer: ")) + str(int(row[0])))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 7, run the appropiate code
                elif menu_choice == 7:
                    # Run an SQL qurey that selects a list of members
                    sql_str = f"select Medlemmer.MedlemsID, Medlemmer.Fornavn, Medlemmer.Etternavn, Poststeder.Poststed FROM Poststeder INNER JOIN Medlemmer ON Poststeder.Postnr = Medlemmer.Postnr WHERE (((Poststeder.Postnr) Between '3070' And '3295')) OR (((Poststeder.Postnr) Between '3650' And '3999'))"
                    cursor.execute(sql_str)

                    # Clear the screen
                    clearScreen()

                    # Create the table formatting
                    table_header_formatting = StrMod.blue(
                        "{:<9} {:<20}")
                    table_divider_formatting = "{:<9} {:<20}"
                    table_row_formatting = StrMod.blue(
                        "{:<9} ") + "{:<20}"

                    # Print the table header to console
                    print(table_header_formatting.format(
                        'MedlemsID', 'Navn', 'Mobil'))
                    print(table_divider_formatting.format('---------',
                                                          '-------------------'))
                    # Print all table rows
                    for row in cursor.fetchall():
                        print(table_row_formatting.format(
                            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A"))

                    # Create a input to stop the script from continuing without the user wanting to continue
                    input(StrMod.bold("\nKLIKK ENTER FOR Å FORTSETTE"))

                # User selected menu choice 8, run the appropiate code
                elif menu_choice == 8:
                    # Stop the submenu loop and exit the submenu
                    break
            else:
                # Let the user know the menu choice isn't valid
                print(f"Menyvalg ikke gyldig")

        except ValueError:
            # Let the user know the menu choice isn't valid
            print("Menyvalg ikke gyldig")


# The fourth menu item
def menu4():
    clearScreen()
    print("\nHovedmeny for Vedlikehold medlemmer\n")
    print("\n1. Legg til et nytt medlem")
    print("\n2. Slett et medlem")
    print("\n3. Registrere om et medlem har betalt kontigenten")
    print("\n4. Endre data for et medlem, f.eks, endre adresse")
    print("\n5. Tilbake til hovedmenyen")
    ans = input("\nHva ønsker du å gjøre? Velg tall.\n")

    if ans == "1":
        print("Her kan du legge til et nytt medlem")

        first_name = input("Fornavn: ")
        last_name = input("Etternavn: ")
        adress = input("Adresse: ")
        postal_code = input("Postnummer: ")
        phone = input("Telefon: ")
        mobile = input("Mobil: ")
        email = input("E-post: ")
        birthdate = datetime.strptime(
            input("Fødselsdato (dd.mm.yyyy): "), '%d.%m.%Y')
        membertype = int(input("Medlemstype (1 = fullt, 2 = støtte): "))

        cursor.execute(
            f"INSERT INTO Medlemmer (Fornavn, Etternavn, Adresse, Postnr, Telefon, Mobil, Fødselsdato, `E-post`, MTypeID, Betalt) VALUES ('{first_name}','{last_name}','{adress}','{postal_code}','{phone}','{mobile}','{birthdate}','{email}',{membertype},{False})")
        conn.commit()

        print("Brukeren ble opprettet!")

    elif ans == "2":
        print("Her kan du slette et medlem")
        medlems_id = int(input("\nMedlemsID til medlem som skal slettes: \n"))
        sql_str = f"DELETE FROM Medlemmer WHERE MedlemsID like {medlems_id}"
        cursor.execute(sql_str)

        print("Medlemmet ble slettet!")

    elif ans == "3":
        print("Her ser du om et medlem har betalt kontigenten, 1 = betalt")
        sql_str = "select MedlemsID, Fornavn, Etternavn, Mobil, Betalt from Medlemmer"
        cursor.execute(sql_str)
        # Prints the cursor formatted as a table
        # First the table header
        table_formatting = "{:<9} {:<20} {:<12}"
        print(table_formatting.format('MedlemsID', 'Navn', 'Kontigent'))
        print(table_formatting.format('---------',
              '-------------------', '------------'))
        # Print all the rows in a table
        for row in cursor.fetchall():
            if row[4] == True:
                print(table_formatting.format(
                    row[0] or "N/A", (row[1] + " " + row[2]) or "N/A", row[4] or "N/A"))

        print()  # a blank line

    elif ans == "4":

        def menu44():
            clearScreen()
            print("\nHovedmeny for endring av medlem\n")
            print("1. Endre all informasjonen til et medlem")
            print("2. Endre Fornavn")
            print("3. Endre Etternavn")
            print("4. Endre Adresse")
            print("5. Endre Postnummer")
            print("6. Endre Telefon")
            print("7. Endre Mobil")
            print("8. Endre E-Post")
            print("9. Endre Fødselsdato")
            print("10. Endre Medlemstype")
            print("11. Endre Betalt")
            ans = input("\nHva ønsker du å gjøre? Velg tall.\n")

            if ans == "1":

                print("Her kan du endre all informasjonen til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                first_name = input("Fornavn: ")
                last_name = input("Etternavn: ")
                adress = input("Adresse: ")
                postal_code = input("Postnummer: ")
                phone = input("Telefon: ")
                mobile = input("Mobil: ")
                email = input("E-post: ")
                birthdate = datetime.strptime(
                    input("Fødselsdato (dd.mm.yyyy): "), '%d.%m.%Y')
                membertype = int(
                    input("Medlemstype (1 = fullt, 2 = støtte): "))
                betalt = True if input("Betalt (Ja, Nei): ") == "Ja" else False

                cursor.execute(
                    f"UPDATE Medlemmer SET Fornavn = '{first_name}', Etternavn= '{last_name}', Adresse = '{adress}', Postnr = '{postal_code}', Telefon = '{phone}', Mobil = '{mobile}', E-Post = '{email}', Fødselsdag = '{birthdate}', Medlemstype = '{membertype}', Betalt = {betalt} WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "2":
                print("Her kan du endre fornavnet til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                first_name = input("Fornavn: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Fornavn = '{first_name}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "3":
                print("Her kan du endre etternavnet til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                last_name = input("Etternavn: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Etternavn = '{last_name}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "4":
                print("Her kan du endre adressen til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                adress = input("Adresse: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Adresse = '{adress}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "5":
                print("Her kan du endre Postnummeret til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                postal_code = input("Postnr: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Postnr = '{postal_code}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "6":
                print("Her kan du endre Telefonnummeret til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                phone = input("Telefon: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Telefon = '{phone}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "7":
                print("Her kan du endre Mobilnummeret til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                mobile = input("Mobil: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Mobil = '{mobile}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "8":
                print("Her kan du endre Eposten til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                email = input("Epost: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET E-post = '{email}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "9":
                print("Her kan du endre Fødselsdatoen til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                birthdate = input("Fødselsdato: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Fødelsdato = '{birthdate}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "10":
                print("Her kan du endre Medlemstypen til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                membertype = input("Medlemstype: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Medlemstype = '{membertype}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")

            elif ans == "11":
                print("Her kan du endre Betalt til et medlem:")

                memeberID = input("ID til medlemme du ønsker å endre: ")
                betalt = input("Betalt: ")

                cursor.execute(
                    f"UPDATE Medlemmer SET Betalt = '{betalt}' WHERE MedlemsID = {memeberID}")
                conn.commit()

                print("Medlemmet ble endret!")
        menu44()

    elif ans == "5":
        print("Trykk [ENTER] for å fortsette!")

# Oppgave 5 & 6 - Ali


# Create a loop to avoid exiting the program
while True:
    # Clear the screen
    clearScreen()

    # Print the selections
    print(StrMod.bold("HOVEDMENY"))
    print(f"[{StrMod.blue('1')}] Vis en tabell med alle medlemmer")
    print(f"[{StrMod.blue('2')}] Vis all registert ifno om et enkelt medlem")
    print(
        f"[{StrMod.blue('3')}] Spørringer")
    print(f"[{StrMod.blue('4')}] Vedlikeholde medlemmer")
    print(f"[{StrMod.blue('5')}] Vedlikehold")
    print(f"[{StrMod.blue('6')}] Avslutt")

    # Use try to handle input errors
    try:
        # Get menu choice from the user and store it in a variable
        menu_choice = int(input(StrMod.bold("Menyvalg:")+" "))

        # Check that the menu choice is valid
        if menu_choice > 0 and menu_choice <= 6:
            # User selected menu choice 1, run the appropiate code
            if menu_choice == 1:
                # Run the chosen menu
                menu1()

            # User selected menu choice 2, run the appropiate code
            elif menu_choice == 2:
                # Run the chosen menu
                menu2()

            # User selected menu choice 3, run the appropiate code
            elif menu_choice == 3:
                # Run the chosen menu
                menu3()

            # User selected menu choice 4, run the appropiate code
            elif menu_choice == 4:
                # Run the chosen menu
                menu4()

            # User selected menu choice 5, run the appropiate code
            elif menu_choice == 5:
                # Run the chosen menu
                print()

            # User selected menu choice 8, run the appropiate code
            elif menu_choice == 6:
                # Stop the menu loop and exit the program
                break
        else:
            # Let the user know the menu choice isn't valid
            print(f"Menyvalg ikke gyldig")

    except ValueError:
        # Let the user know the menu choice isn't valid
        print("Menyvalg ikke gyldig")
