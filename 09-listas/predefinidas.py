cantantes = ['2pac', 'Drake', 'Otro', 'Uno mas']
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar
numeros.sort()
#print(numeros)

#Añadir elementos
cantantes.append('jose jose')
cantantes.insert(2,'Emanuel')

#print(cantantes)

#eliminar elementos
cantantes.pop(2)
cantantes.remove('Drake')
#print(cantantes)

#Revertir la lista
#print(numeros)
numeros.reverse()
#print(numeros)


#buscar en la lista
#print('2pac' in cantantes)

#contar elementos#
#print(cantantes)
#print(len(cantantes))


#Cuantas veces existe un elemento en la lista
numeros.append(8)
print(numeros.count(8))


#Conseguir indice
print(cantantes)
print(cantantes.index('jose jose'))


#unir listas
cantantes.extend(numeros)
print(cantantes)
