capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}

pais = input("Introdueix el nom d'un país: ")

if pais in capital_pais.keys():
    print(f"La capital de {pais} és {capital_pais[pais]}.")
else:
    print(f"No hi ha informació sobre {pais}.")

capital = capital_pais.get(pais, "No tinc aquest país")
if capital == "No tinc aquest país":
	print(capital)
else:
	print(f"La capital de {pais} és {capital}.")