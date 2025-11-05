###
# EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("Ejercicio 1: El mensaje secreto")
print("------------------------------\n")
mensaje =["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje2 = print(mensaje[7:])

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\nEjercicio 2: Intercambio de posiciones")
print("------------------------------\n")
numeros = [10, 20, 30, 40, 50]
numeros[0] = 50
numeros[4] = 0
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\nEjercicio 3: El sándwich de listas")
print("------------------------------\n")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

# sandwich += pan
# sandwich += ingredientes
# sandwich += pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\nEjercicio 4: Duplicando la lista")
print("------------------------------\n")

lista = [1, 2, 3]
lista2 = lista + lista[:] 
print(lista2)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\nEjercicio 5: Extrayendo el centro")
print("------------------------------\n")

lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2 # Cogemos la longitud de la lista y la dividimos entre 2 para determinar el centro.
print(f"El centro de la lista es -> {lista[centro]}" )

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("\nEjercicio 6: Reversa parcial")
print("------------------------------\n")

lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2 # Determinamos el centro de la lista
# lista[:mitad] --> Cógeme todos los elementos hasta la mitad.
# lista[mitad:] --> Cógeme todos los elementos a partir de la mitad.
# lista[:mitad][::-1] --> Inviérteme la primera mitad.
# lista[:mitad][::-1] + lista[mitad:] --> Úneme las dos mitades.
lista_invertida = lista[:mitad][::-1] + lista[mitad:] 
print(lista_invertida)