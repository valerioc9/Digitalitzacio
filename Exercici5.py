llista = [2, 7, 4, 2, 1, 6, 3, 7, 8, 7, 4, 2, 1, 6, 3, 7, 6, 10]
llista_nova = []

for element in llista:
	if element not in llista_nova:
		llista_nova.append(element)

print(llista_nova)
