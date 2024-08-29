import random

pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))


ympyran_sisalla = sum(
    1 for _ in range(pisteiden_maara)
    if (random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2) < 1
)


pi_likiarvo = 4 * ympyran_sisalla / pisteiden_maara
print(f"Piin likiarvo on noin {pi_likiarvo:.6f}.")
