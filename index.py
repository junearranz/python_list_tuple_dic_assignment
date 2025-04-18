# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

ciudades_lista = ['Bilbao', 'Vitoria', 'San Sebastian']
ciudades_tupla = ('Bilbao', 'Vitoria', 'San Sebastian')
diccionario = {"nombre":"June", "edad":39}
numero_flotante = 25.50
numero_entero = 1000

from decimal import Decimal
numero_decimal = Decimal(20.99)

# Exercise 2: Round your float up.

import math

flotante_roundedup = math.ceil(numero_flotante)
print (flotante_roundedup)

# Exercise 3: Get the square root of your float.

flotante_squareroot = math.sqrt(numero_flotante)
print(flotante_squareroot)

# Exercise 4: Select the first element from your dictionary.

# Sin almacenar en variable: 
print(diccionario["nombre"])

#Almacenando en variable:
nombre_completo = diccionario["nombre"]
print(nombre_completo)

# Exercise 5: Select the second element from your tuple.

print(ciudades_tupla[1])

# Exercise 6: Add an element to the end of your list.

ciudades_lista.append('Burgos')
print(ciudades_lista)

# Exercise 7: Replace the first element in your list.

ciudades_lista[0] = 'Valladolid'
print(ciudades_lista)

# Exercise 8: Sort your list alphabetically.

ciudades_lista.sort()
print(ciudades_lista)

# Exercise 9: Use reassignment to add an element to your tuple.

ciudades_tupla += ('Burgos',)
print(ciudades_tupla) 
