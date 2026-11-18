list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
list_invertida = []
for i in range (len(list_num)-1, -1, -1):
	list_invertida.append(list_num[i])
print(list_invertida)