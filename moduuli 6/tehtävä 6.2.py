import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def main():
    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))
    
    while True:
        silmaluku = heita_noppaa(tahkojen_maara)
        print(f"Heiton tulos: {silmaluku}")
        if silmaluku == tahkojen_maara:
            break

if __name__ == "__main__":
    main()
