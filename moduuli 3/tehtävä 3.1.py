pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Kuha Pyyntimitat koko maassa vähintään 42 cm. Kalastuslain (379/2015) 88 §:ssä
alamitta = 42.0

if pituus < alamitta:
    puuttuva_mitta = alamitta - pituus 
    print (f"Kuha on alamittainen, laske kuha takaisin veteen.")
    print(f"Kuha on {puuttuva_mitta:.1f} cm liian lyhyt")

else:
    print (" Kuha on sallittua pyyntimittaa pidempi.")