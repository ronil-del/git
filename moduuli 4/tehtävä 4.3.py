luvut = []

while (syote := input("Anna luku (tai paina Enter lopettaaksesi): ")):
    luvut.append(float(syote))

if luvut:
    print(f"Pienin luku on {min(luvut)} ja suurin luku on {max(luvut)}.")
else:
    print("Et syöttänyt yhtään lukua.")