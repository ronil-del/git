tuumat = 0 

while tuumat >= 0:
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))
    
    if tuumat < 0:
        print("Ohjelma lopetettu.")
    else:
        sentit = tuumat * 2.54
        print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä.")
