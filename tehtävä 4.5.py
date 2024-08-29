oikea_tunnus = "Pertti"
oikea_salasana = "Petteri"
yritykset = 5

for _ in range (yritykset):
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana.")
else:
    print("pääsy evätty.")