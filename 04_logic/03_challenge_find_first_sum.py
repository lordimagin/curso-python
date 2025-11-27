"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system
if system("clear") != 0: system("cls")

# def find_first_sum(nums, goal):
#   # early return, una validación rápida
#   if len(nums) == 0: return None # Si la lista está vacía (osea el leng que sea 0), devuélveme un "None"

#   for i in range(len(nums)): # Bucle para ir en vertical, donde 'i' es la posición de la lista.
#     for j in range(i + 1, len(nums)): # Bucle para ir en horizontal, donde nunca compara un número consigo mismo y tampoco repite combinaciones ya probadas.
#       # | i | j valores | pares que compara |
#       # | - | --------- | ----------------- |
#       # | 0 | 1, 2      | (3,5), (3,7)      |
#       # | 1 | 2         | (5,7)             |
#       # | 2 | —         | no entra          | 

#       # Lista: [4, 5, 6, 2]

#       # i = 0  → elemento 4
#       #   j = 1  → compara 4 con 5
#       #   j = 2  → compara 4 con 6
#       #   j = 3  → compara 4 con 2

#       # (Es decir: desde i = 0, j recorre todos los elementos a la derecha)
#       # Así con los demás.

#       # Lista: [4, 5, 6, 2]

#       # i = 1  → elemento 5
#       #   j = 2  → compara 5 con 6
#       #   j = 3  → compara 5 con 2

#       # Lista: [4, 5, 6, 2]

#       # i = 2  → elemento 6
#       #   j = 3  → compara 6 con 2

#       if nums[i] + nums[j] == goal:
#         return [i, j]

#   return None # no se encontró ninguna combinación

def find_first_sum(nums, goal):
  seen = {} # Creamos un diccionario para guardar el número y su índice

  for index, value in enumerate(nums): # Enumérame todos los elementos de 'nums' mediante su índice {0, 1, 2, etc} y el valor de cada uno.
    missing = goal - value # Cuál es el número que me falta? (missing)
    # Goal es el número objetivo = 8
    # Missing es el número que nos hace falta para la suma hasta llegar al 8 con los de la lista.
    # Value es el número obtenido de la lista según la lista.
    if missing in seen: return [seen[missing], index] 
    # El número que nos falta está en los revisados? Si es así, devuélveme una lista donde el primer valor sea el índice del valor que ya hemos revisado.
    seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación.

  return None

# Iteración paso a paso:

# 1️⃣ value = 4 (índice 0)
# missing = 8 - 4 = 4
# 4 no está en seen
# Guardamos: seen = {4: 0}

# 2️⃣ value = 5 (índice 1)
# missing = 8 - 5 = 3
# 3 no está en seen
# Guardamos: seen = {4: 0, 5: 1}

# 3️⃣ value = 6 (índice 2)
# missing = 8 - 6 = 2
# 2 NO está en seen aún
# Guardamos: seen = {4: 0, 5: 1, 6: 2}

# 4️⃣ value = 2 (índice 3)
# missing = 8 - 2 = 6
# 6 SÍ está en seen, en el índice 2
# → Devolvemos [2, 3]

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) # [2, 3] 
print(result)