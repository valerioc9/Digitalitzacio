def ordena_cercant_minims(nombres):
	pendents = nombres.copy()
	ordenats = []
	while pendents:
		minim = min(pendents)
		ordenats.append(minim)
		pendents.remove(minim)
	return ordenats

def selection_sort(nombres):
	resultat = nombres.copy()
	for i in range(len(resultat)):
		index_minim = i
		for j in range(i + 1, len(resultat)):
			if resultat[j] < resultat[index_minim]:
				index_minim = j
		resultat[i], resultat[index_minim] = resultat[index_minim], resultat[i]
	return resultat

def insertion_sort(nombres):
	resultat = nombres.copy()
	for i in range(1, len(resultat)):
		valor = resultat[i]
		j = i - 1
		while j >= 0 and resultat[j] > valor:
			resultat[j + 1] = resultat[j]
			j -= 1
		resultat[j + 1] = valor
	return resultat

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print("Cercant els mínims:", ordena_cercant_minims(list_num))
print("Selection Sort:", selection_sort(list_num))
print("Insertion Sort:", insertion_sort(list_num))
