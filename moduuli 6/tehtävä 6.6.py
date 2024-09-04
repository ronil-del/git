import math

def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2 / 10000
    return hinta / pinta_ala

def main():
    halkaisija1, hinta1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): ")), float(input("Anna ensimmäisen pizzan hinta (euroa): "))
    halkaisija2, hinta2 = float(input("Anna toisen pizzan halkaisija (cm): ")), float(input("Anna toisen pizzan hinta (euroa): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)
    
    print(f"Ensimmäisen pizzan yksikköhinta on: {yksikkohinta1:.2f} €/m²")
    print(f"Toisen pizzan yksikköhinta on: {yksikkohinta2:.2f} €/m²")
    print("Ensimmäinen pizza antaa paremman vastineen rahalle." if yksikkohinta1 < yksikkohinta2 else "Toinen pizza antaa paremman vastineen rahalle." if yksikkohinta1 > yksikkohinta2 else "Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")

if __name__ == "__main__":
    main()
