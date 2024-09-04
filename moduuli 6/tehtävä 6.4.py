def laske_summa(luvut):
    return sum(luvut)

def main():
    luvut = [1, 2, 3, 4, 5]
    summa = laske_summa(luvut)
    
    print(f"Listan lukujen summa on: {summa}")

if __name__ == "__main__":
    main()
