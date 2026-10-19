frase = "Hello World"
frase2 = "Hola mon!!!"

coincidencies = 0

for i in range(min(len(frase), len(frase2))):
	if frase[i] == frase2[i]:
		coincidencies += 1

print(coincidencies)
