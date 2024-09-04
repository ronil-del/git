def karsi_parittomat(luvut):
    parilliset = [luku for luku in luvut if luku % 2 == 0]
    return parilliset

def main():
    
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
    karsitut_luvut = karsi_parittomat(luvut)
    
   
    print("Alkuperäinen lista:", luvut)
    
    
    print("Karsittu lista:", karsitut_luvut)

if __name__ == "__main__":
    main()
