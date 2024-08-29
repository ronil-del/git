leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogrammat = int(grammat // 1000)
jäljellä_olevat_grammat = grammat % 1000

print(f"Massa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {jäljellä_olevat_grammat:.2f} grammaa.")