###
# EJERCICIOS (for)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1: Imprimir números pares.")
print("---------------------------------------------\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for pares in numbers:
    if (pares % 2 == 0):
        print(pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2: Calcular la media de una lista.")
print("---------------------------------------------\n")

numeros = [10, 20, 30, 40, 50]
suma = 0

for numero in numeros: 
    suma += numero # Me cogerás todos los números y los irás sumando
media = suma / len(numeros) # Cogemos la suma total y lo dividimos entre la longitud de la lista.
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3: Buscar el máximo de una lista.")
print("---------------------------------------------\n")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0] # Creamos una lista nueva para usarla en la comparación de número más grande.

for numero in numeros:
    if numero > maximo: # Si el número cogido de la lista es mayor a su anterior:
        maximo = numero # el número pasará a ser el introducido a la nueva lista
print(f"El número máximo de la lista es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4: Filtrar cadenas por longitud.")
print("---------------------------------------------\n")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
# Crea una lista con cada "palabra" en "palabras[]" solo si la longitud (len(palabra)) es mayor que 5.
# El código filtra una lista de palabras y crea otra lista solo con las que tienen más de 5 letras.
print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5: Contar palabras que empiezan con una letra.")
print("---------------------------------------------\n")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()  # Pedimos al usuario que ponga una letra y ésta, la convertimos en minúscula
contador = 0 # Guardaremos las palabras que cumplan con la condición.
for palabra in palabras:
  if palabra.lower().startswith(letra):
    # Convertimos la palabra en minúscula y miramos si empieza por la letra seleccionada por el usuario.
    # Si coincide, incrementamos el contador en 1 y repetimos el proceso.
    contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")