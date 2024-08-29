hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C, Ö): ").upper()

if hyttiluokka == "LUX":
    print ("LUX on Parvekkeellinen hytti ylimmällä kannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolelella.")
elif hyttiluokka == "B":
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print ("C on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka == "Ö":
    print ("Ö luokan hytti on sikaosastolla autokannen alapuolella")
else:
    print ("Virheellinen hyttiluokka.")