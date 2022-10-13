

'''[ ]'''

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

# list.append
numbers.append('10')

#list.extend
numbers.extend(['11', '12'])

#lint.insert
numbers.insert(4, '3.5')
print(numbers)

#list.remove
numbers.remove('3.5')
print(numbers)

#list.pop
numbers.pop(12)
print(numbers)

#list.index
print(numbers.index('10'))

#list.count
print(numbers.count('4'))

#list.sort
numbers.sort()
print(numbers)

#list.reverse
numbers.reverse()
print(numbers)

#list.copy
numbers.copy()
print(numbers)

'''listas como pilas'''

family = ['nikol', 'sandra', 'matilde']
family.append('Conny')
family.append('paul')
family.pop()

print(family)

'''listas como colas'''

from collections import deque
queue = deque(["Alexs", "Nikol", "Sandra"])
queue.append("Matilde")
queue.append("Alexander")
queue.append("Estefania")
queue.popleft()
queue.popleft()

'''Comprension de listas'''
squares = [(x*5)/2 for x in range(10)]
print(squares)

'''Listas por compresion anidadas'''

primos = [
    [2, 3, 5, 7],
    [11, 13, 17, 19],
    [23, 29, 31, 37],
]

[[row[i] for row in primos] for i in range(3)]

'''La instruccion del'''

Rectas = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
del Rectas[0:5]
print(Rectas)

'''Tuplas y secuencias'''

presentacion = 'Hola', 'me', 'llamo', 'Alexs ', ',tengo', 18, 'años.'
nuevo = presentacion, ('un placer')
print(nuevo)

'''Conjuntos'''

canasta_familiar = {'leche', 'huevos', 'pan', 'queso', 'fruta y verduras', 'carnes', 'cereales'}
'fritos' in canasta_familiar
'huevos' in canasta_familiar

'''Diccionarios'''

ventas = {'carlos': 300, 'jessica': 600, 'alfredo': 100}
ventas['pedro'] = 200
del ventas['alfredo']
list(ventas)
print(ventas)
'carlos' in ventas
'alfredo' in ventas

'''Tecnicas de iteración'''

