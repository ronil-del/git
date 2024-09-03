luku = [] 

while True:
    ohjelma = input("Anna luku tai lopeta ohjelma syöttämällä tyhjää: ")
    if ohjelma == "":
        break
    luku.append(float(ohjelma))

luku.sort(reverse=True)  
print("Viisi suurinta lukua ovat: ", luku[:5]) 
