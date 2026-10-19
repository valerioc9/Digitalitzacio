text = "atggatcattta"
lletra = "a"
comptador = 0

for posicio, caracter in enumerate(text):
	if caracter == lletra:
		comptador += 1
		print("La lletra", lletra, "es troba a la posició", posicio)

print("La lletra", lletra, "apareix", comptador, "vegades")
