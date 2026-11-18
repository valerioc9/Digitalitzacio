list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

valor_maxim = list_num[0]
valor_minim = list_num[0]

for numero in list_num:
	if numero > valor_maxim:
		valor_maxim = numero
	if numero < valor_minim:
		valor_minim = numero

print(f"El valor màxim de la llista és: {valor_maxim} i el valor mínim és: {valor_minim}")
