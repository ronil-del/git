kanta_str = input("Anna suorakulmion kanta: ")

korkeus_str = input("Anna suorakulmion korkeus: ")

kanta = float(kanta_str)
korkeus = float(korkeus_str)
piiri = 2 * (kanta + korkeus)

pinta_ala = kanta * korkeus

print("Suorakulmion piiri on: " + str(piiri))
print("Suorakulmion pinta-ala on: " + str(pinta_ala))
