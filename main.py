import random

coin = 0
numbers = [0] * 20
mynums = []
db_talalat = 0
tipus = 0


# Nev es jatektipus bekerese
def be():
    global tipus
    nev = input("Add meg a neved: ")
    print("Udvozlunk a jatekban " + nev + "!")
    while True:
        tipus = int(input("Add meg a jatek tipusat (1-10): "))
        if 1 <= tipus <= 10:
            print("A jatekod tipusa:", tipus)
            break
        else:
            print("Nem megfelelo a jatek tipusa. Probald ujra!")


# READ TO N
def readton():
    global mynums
    while len(mynums) < 10:
        try:
            n = int(input("Add meg a szamodat (1-80 között): "))
            if 1 <= n <= 80:
                mynums.append(n)
            else:
                print("A számnak 1 és 80 között kell lennie. Próbáld újra.")
        except ValueError:
            print("Hibás érték! Kérlek, számot adj meg.")
    new_mynums = str(mynums).strip("[]")
    print("Az altalad megadott szamok:", new_mynums)


# Egyenleg feltoltes
def coin_upload():
    global coin
    value = int(input("Add meg, hogy mennyi Coin-t szeretnel feltolteni: "))
    coin += value
    print("A jelenlegi egyenleged:", coin)


# Sorsolas szamok random generalasa
def numbers_generate(size, min_val, max_val):
    global numbers
    numbers = set()
    while len(numbers) < size:
        numbers.add(random.randint(min_val, max_val))
    print("A sorsolt szamok:", str(list(numbers)).strip("[]"))


# A szamok egyezosegenek vizsgalata
def talalatok():
    print("Az eltalalt szamaid: ", end="")
    for i in mynums:
        if i in numbers:
            print(i, end=" ")


def nyerotabla():
    nyerotabla = [
        [1000000, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8000, 100000, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print("A nyeremenyed: ", nyerotabla[])


def main():
    pass


if __name__ == '__main__':
    # readton()
    # numbers_generate(len(numbers), 1, 80)
    # talalatok()
    nyerotabla()
