import random

egyenleg = 1000  # Kezdeti egyenleg
numbers = [0] * 20
mynums = []
db_talalat = 0
value = 0
tipus = 0
nev = ""


# Nev es jatektipus bekerese
def be():
    global tipus, nev
    nev = input("Add meg a neved: ")
    if nev == "Vanda":
        print("Köszönjük, hogy velünk játszol " + nev + "😘🥰❤️")
    else:
        print("Üdvözlünk a játékban " + nev + "!")
    # while True:
    #     try:
    #         tipus = int(input("Kedves " + nev + ", add meg a játékod típusát (1-10): "))
    #         if 1 <= tipus <= 10:
    #             break
    #         else:
    #             print("Nem megfelelő a játék típusa. Próbáld újra!")
    #     except ValueError:
    #         print("Hibás bemenet! Kérlek, számot adj meg.")


# Egyenleg feltoltes
def coin_upload():
    global egyenleg, value
    while True:
        try:
            value = int(input("Add meg, hogy mennyi Ft-ot szeretnél feltölteni: "))
            if value > 0:
                egyenleg += value
                print("Az új egyenleged:", egyenleg, "Ft")
                break
            else:
                print("Pozitív összeget adj meg!")
        except ValueError:
            print("Hibás bemenet! Kérlek, számot adj meg.")


# Sorsolas szamok random generalasa
def numbers_generate(size, min_val, max_val):
    global numbers
    numbers = set()
    while len(numbers) < size:
        numbers.add(random.randint(min_val, max_val))
    return numbers


# A szamok egyezosegenek vizsgalata
def talalatok():
    global db_talalat
    eltalalt = []
    for i in mynums:
        if i in numbers:
            eltalalt.append(i)
            db_talalat += 1
    if db_talalat > 0:
        print("Az eltalált számaid:", str(eltalalt).strip("[]"))
    else:
        print("Sajnos egyetlen számot sem találtál el :(")


def nyerotabla():
    global egyenleg
    matrix = [
        [1500000, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8000, 100000, 0, 0, 0, 0, 0, 0, 0, 0],
        [350, 1200, 20000, 0, 0, 0, 0, 0, 0, 0],
        [30, 100, 500, 5000, 0, 0, 0, 0, 0, 0],
        [3, 15, 25, 75, 1000, 0, 0, 0, 0, 0],
        [1, 3, 5, 10, 25, 250, 0, 0, 0, 0],
        [0, 0, 0, 2, 4, 13, 120, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 3, 25, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 1, 1, 0, 0, 0, 0, 0]
    ]
    if db_talalat >= 1:
        nyeremeny = matrix[11 - db_talalat][1 - tipus] * value
    else:
        nyeremeny = 0
    egyenleg += nyeremeny
    print("11 - db_talalat:", 11 - db_talalat)
    print("11 - tipus:", 11 - tipus)
    print("matrix[10 - db_talalat][10 - tipus]:", matrix[9 - db_talalat][9 - tipus])
    print(f"A nyereményed: {nyeremeny} Ft")
    # print(f"Jelenlegi egyenleged: {egyenleg} Ft")


# READ TO N
def readton():
    global mynums
    while True:
        jatekmod = input("Add meg, hogy milyen játékmódban akarsz játszani (gepi/kezi): ").lower()
        if jatekmod == "gepi":
            mynums = numbers_generate(10, 1, 80)
            print("A gépi számaid:", str(mynums).strip("{}"))
            break
        elif jatekmod == "kezi":
            while len(mynums) < 10:
                try:
                    n = int(input("Add meg a számodat (1-80 között): "))
                    if 1 <= n <= 80:
                        if n in mynums:
                            print("A megadott számot már korábban megadtad!")
                        else:
                            mynums.append(n)
                    else:
                        print("A számnak 1 és 80 között kell lennie. Próbáld újra.")
                except ValueError:
                    print("Hibás érték! Kérlek, számot adj meg.")
            print("Az általad megadott számok:", str(mynums).strip("[]"))
            break
        else:
            print("Nem megfelelően megadott játékmód! Kérlek, válassz: 'gepi' vagy 'kezi'.")


def main():
    global egyenleg, tipus
    be()
    while egyenleg > 0:
        print(f"Jelenlegi egyenleged: {egyenleg} Ft")
        tét = int(input("Add meg a téted (Ft-ban): "))
        if tét > egyenleg:
            print("Nincs elég egyenleged a tét felrakásához.")
            continue
        egyenleg -= tét
        print(f"A téted: {tét} Ft, maradék egyenleged: {egyenleg} Ft")
        while True:
            try:
                tipus = int(input("Kedves " + nev + ", add meg a játékod típusát (1-10): "))
                if 1 <= tipus <= 10:
                    break
                else:
                    print("Nem megfelelő a játék típusa. Próbáld újra!")
            except ValueError:
                print("Hibás bemenet! Kérlek, számot adj meg.")
        readton()
        print("A gép által sorsolt számok:", str(numbers_generate(20, 1, 80)).strip("{}"))
        talalatok()
        nyerotabla()
        if egyenleg <= 0:
            print("Az egyenleged elfogyott. Kérlek, töltsd fel újra, hogy folytathasd a játékot!")
            coin_upload()


if __name__ == '__main__':
    main()
