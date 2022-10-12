

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

squares = []

for x in range(10):
    squares.append(x**2)
print(squares)

