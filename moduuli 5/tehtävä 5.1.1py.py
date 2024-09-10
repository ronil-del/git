import random

n = int(input("montako arpakuutiota heitetään? "))

summa = 0

for i in range (n):
    heitto = random.randint(1, 6)

    summa += heitto 

print(f"Silmälukujen summa: {summa}")