import random
numeros = []
for i in range (100):
    aleatorio = random.randint(100,1000)
numeros.append(aleatorio)

suma = 0
for i in numeros:
    suma += i


#Otra forma de hacerlo:

import random 
numeros = []
suma = 0 
for i in numeros:
    suma += i
for i in range(len(numeros)):
    suma += numeros [i]

