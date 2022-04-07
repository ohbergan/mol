# Oppgave 1, 2 & 3 - Ole Halvor

import pyodbc
import os


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


# Lagrer path til det aktive scriptet i variabelen current_path
current_path = os.path.dirname(__file__)

# connection-strengen
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + current_path + '\Medlemsregister.accdb;')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


def clearScreen():
    print("\033[H\033[J", end="")


def menu1():
    clearScreen()
    sql_str = "select MedlemsID, Fornavn, Etternavn, Mobil from Medlemmer"
    cursor.execute(sql_str)
    # Prints the cursor formatted as a table
    # First the table header
    table_header_formatting = StrMod.bold(StrMod.blue("{:<9} {:<20} {:<12}"))
    table_divider_formatting = "{:<9} {:<20} {:<12}"
    table_row_formatting = StrMod.bold(StrMod.blue("{:<9} ")) + "{:<20} {:<12}"
    print(table_header_formatting.format('MedlemsID', 'Navn', 'Mobil'))
    print(table_divider_formatting.format('---------',
          '-------------------', '------------'))
    # Print all the rows in a table
    for row in cursor.fetchall():
        print(table_row_formatting.format(
            row[0] or "N/A", (row[1] + " " + row[2]) or "N/A", row[3] or "N/A"))
    print()  # a blank line


def menu2():
    clearScreen()
    memberID = input("MedlemsID: ")
    sql_str = "select top 1 * from Medlemmer where MedlemsID like "+memberID

    cursor.execute(sql_str)
    clearScreen()
    for row in cursor.fetchall():
        betalt = 'Ja' if row[0] == True else 'Nei'
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
        print()
        input(StrMod.bold("KLIKK ENTER FOR Å FORTSETTE"))


def menu3():
    clearScreen()
    memberID = input("MedlemsID: ")
    sql_str = "select top 1 * from Medlemmer where MedlemsID like "+memberID

    cursor.execute(sql_str)
    clearScreen()
    for row in cursor.fetchall():
        betalt = 'Ja' if row[0] == True else 'Nei'
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
        print()
        input(StrMod.bold("KLIKK ENTER FOR Å FORTSETTE"))


menu3()

# Oppgave 4 - Emil


# Oppgave 5 & 6 - Ali
