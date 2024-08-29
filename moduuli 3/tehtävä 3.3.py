sukupuoli = input("Anna sukupuolesi (mies / nainen): ").lower()

hemoglobiini = float(input("Anna hemoglobiini (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print ("Hemoglobiinisi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print ("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print ("Hemoglobiinisi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print ("Hemoglobiinisi on normaali.")
    else:
        print ("Hemoglobiinisi on korkea.")

else:
    print("Virheellinen sukupuoli.")
