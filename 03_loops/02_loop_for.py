###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

# ITERAR ->  Ejecutar un bloque de código repetidamente, recorriendo una secuencia de elementos como una lista, un string o un diccionario.

from os import system
if system("clear") != 0: system("cls")

print("\nBucle for:")

# ===================================================
# ITERAR UNA LISTA
# ===================================================

frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas: # Por cada fruta que haya en la lista de frutas:
  print(fruta) # Muéstrame las frutas.

# ===================================================
# ITERAR SOBRE CUALQUIER COSA QUE SEA ITERABLE
# ===================================================

cadena = "midudev"
for caracter in cadena:
  print(caracter)

# ===================================================
# ENUMERATE()
# ===================================================

# enumerate() -> Con esto podemos recoger la posición (index) y el valor de una lista.
# De esta manera creamos dos variables para que se guarden ahí y las mostramos.
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
  print(f"El índice es {idx} y la fruta es {value}")

# ===================================================
# BUCLES ANIDADOS
# ===================================================

# anidar -> meter uno dentro de otro.
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

# ===================================================
# BREAK
# ===================================================

print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales): # Me vas buscando el índice y el animal de la lista:
  print(animal)
  if animal == "loro": # Cuando el animal sea el loro:
    print(f"El loro está escondido en el índice {idx}") # Imprime esto y:
    break # Termina el bucle.

# ===================================================
# CONTINUE
# ===================================================

print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": continue # Cuando el animal sea "loro", sáltate el siguiente código que haya a continuación (en este caso volverá a empezar el for).
  
  print(animal)

# ===================================================
# COMPRENSIÓN DE LISTAS (LIST COMPREHENSION)
# ===================================================

# Hacer en una linea el bucle del for.
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
# [lo que queremos hacer PARA cada uno de los elementos DENTRO de la lista X]
animales_mayus = [animal.upper() for animal in animales] # Quiero que cada uno de los animales de la lista hagas que sus letras me las pases a mayus.
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

