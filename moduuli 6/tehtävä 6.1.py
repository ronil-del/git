import random

def heitä_noppaa():
    return random.randint(1, 6)

def main():
    while True:
        silmaluku = heitä_noppaa()
        print(f"Heiton tulos: {silmaluku}")
        if silmaluku == 6:
            break

if __name__ == "__main__":
    main()
