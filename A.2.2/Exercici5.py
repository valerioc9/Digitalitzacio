paraula = input("Escriu una paraula: ")
comptador = {}

for lletra in paraula.lower():
	comptador[lletra] = comptador.get(lletra, 0) + 1

print(comptador)
