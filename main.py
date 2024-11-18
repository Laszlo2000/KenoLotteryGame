# PYQT: pyqt5-tools designer
import random

egyenleg = 0
numbers = [0] * 20
mynums = []
db_talalat = 0
tipus = 0
nev = ""


# Nev es jatektipus bekerese
def be():
    global tipus, nev
    nev = input("Add meg a neved: ")
    if nev == "Vanda":
        print("Köszönjük, hogy velünk játszol " + nev + "😘🥰❤️")
    else:
        print("Udvozlunk a jatekban " + nev + "!")
    while True:
        tipus = int(input("Kedves " + nev + " add meg a jatekod tipusat (1-10): "))
        if 1 <= tipus <= 10:
            break
        else:
            print("Nem megfelelo a jatek tipusa. Probald ujra!")


# Egyenleg feltoltes
def coin_upload():
    global egyenleg
    value = int(input("Add meg, hogy mennyi Ft-ot szeretnel feltolteni: "))
    egyenleg += value
    # print("A jelenlegi egyenleged:", coin)


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
        else:
            db_talalat = db_talalat
    print("db_talalat:", db_talalat)
    if db_talalat > 0:
        print("Az eltalalt szamaid:", str(eltalalt).strip("[]"))
    else:
        print("Sajnos egyetlen szamot sem talaltal el :(")


def nyerotabla():
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
        [2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print("A nyeremenyed:", matrix[10 - db_talalat][10 - tipus] * egyenleg, "Ft")
    prize = matrix[10 - db_talalat][10 - tipus] * egyenleg
    print("Jelenlegi egyenleged:", prize, "Ft")


# READ TO N
def readton():
    global mynums
    while True:
        jatekmod = input("Add meg, hogy milyen jatekmodban akarsz jatszani (gepi/kezi): ").lower()
        if jatekmod == "gepi":
            mynums = numbers_generate(10, 1, 80)
            print("A gepi szamaid:", str(mynums).strip("{}"))
            break
        elif jatekmod == "kezi":
            while len(mynums) < 10:
                try:
                    n = int(input("Add meg a szamodat (1-80 között): "))
                    if 1 <= n <= 80:
                        if n in mynums:
                            print("A megadott szamot mar korabban megadtad!")
                        else:
                            mynums.append(n)
                    else:
                        print("A számnak 1 és 80 között kell lennie. Próbáld újra.")
                except ValueError:
                    print("Hibás érték! Kérlek, számot adj meg.")
            new_mynums = str(mynums).strip("[]")
            print("Az altalad megadott szamok:", new_mynums)
            break
        else:
            print("Nem megfelelően megadott játékmód! Kérlek, válassz: 'gepi' vagy 'kezi'.")


def main():
    be()
    coin_upload()
    readton()
    print("A gep altal sorsolt szamok:", str(numbers_generate(20, 1, 80)).strip("{}"))
    talalatok()
    nyerotabla()
    # print(numbers_generate(10, 1, 80))


if __name__ == '__main__':
    main()
