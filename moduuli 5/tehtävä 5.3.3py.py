luku = int(input("Anna kokonaisluku: "))

if luku > 1:
    for i in range (2, luku):
        if luku % i == 0:
            print(f"Luku {luku} ei ole alkuluku")
            break
    else:
        print(f"luku {luku} on alkuluku")
else:
    print(f"luku {luku} ei ole alkuluku")