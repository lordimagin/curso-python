"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system
if system("clear") != 0: system("cls")

def find_first_sum(nums, goal):
  # early return, una validación rápida
  if len(nums) == 0: return None # Si la lista está vacía (osea el leng que sea 0), devuélveme un "None"

  for i in range(len(nums)): # Bucle para ir en vertical, donde 'i' es la posición de la lista.
    for j in range(i + 1, len(nums)): # Bucle para ir en horizontal, donde nunca compara un número consigo mismo y tampoco repite combinaciones ya probadas.
      # | i | j valores | pares que compara |
      # | - | --------- | ----------------- |
      # | 0 | 1, 2      | (3,5), (3,7)      |
      # | 1 | 2         | (5,7)             |
      # | 2 | —         | no entra          | 

      # Lista: [4, 5, 6, 2]

      # i = 0  → elemento 4
      #   j = 1  → compara 4 con 5
      #   j = 2  → compara 4 con 6
      #   j = 3  → compara 4 con 2

      # (Es decir: desde i = 0, j recorre todos los elementos a la derecha)
      # Así con los demás.

      # Lista: [4, 5, 6, 2]

      # i = 1  → elemento 5
      #   j = 2  → compara 5 con 6
      #   j = 3  → compara 5 con 2

      # Lista: [4, 5, 6, 2]

      # i = 2  → elemento 6
      #   j = 3  → compara 6 con 2

      if nums[i] + nums[j] == goal:
        return [i, j]

  return None # no se encontró ninguna combinación

# def find_first_sum(nums, goal):
#   seen = {} # diccionario para guardar el numero y su índice

#   for index, value in enumerate(nums):
#     missing = goal - value
#     if missing in seen: return [seen[missing], index]
#     seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación

#   return None

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) # [2, 3] 
print(result)