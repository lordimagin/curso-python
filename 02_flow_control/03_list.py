###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# ===================================================
# CREACIÓN DE LISTAS
# ===================================================

print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de int
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# ===================================================
# ACCESO A ELEMENTOS POR ÍNDICE
# ===================================================

print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# ===================================================
# SLICING (REBANADO) DE LISTAS
# ===================================================

lista1 = [1, 2, 3, 4, 5]

# print(lista1[desde:hasta]) -> Desde dónde quiero empezar, hasta dónde quiero llegar, si no hay nada que sea uno a uno.
print(lista1[1:4]) # [2, 3, 4] Quiero que me devuelvas desde la posición 1 hasta el inicio de la posición 4, por lo tanto no llegará al 5, porque se queda delante.
print(lista1[:3]) # [1, 2, 3] Quiero que me devuelvas todos los números hasta el inicio de la posición 3.
print(lista1[3:]) # [4, 5] Quiero que me devuelvas, desde el inicio de la posición 3, todo lo que lleve detrás.
print(lista1[:]) # [1, 2, 3, 4, 5] Me devuelve una copia de la misma lista entera.

# ===================================================
# EL TERCER PARÁMETRO ES EL PASO (STEP)
# ===================================================

# print(lista1[desde:hasta:paso])
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares // Aquí da los pasos de dos en dos, empezamos por el índice 0 y luego saltamos de 2 en 2.
print(lista1[::-1]) # para devolver índices inversos // Revertimos la lista al decirle que vaya de 1 en 1 pero al revés.

# ===================================================
# MODIFICAR UNA LISTA
# ===================================================

# lista1[índice] = valor nuevo
lista1[0] = 20 # Le decimos que en la posición 0 de la lista, lo modifique por 20
print(lista1)

# ===================================================
# AÑADIR ELEMENTOS A UNA LISTA
# ===================================================

lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# ===================================================
# RECUPERAR LONGITUD DE UNA LISTA
# ===================================================

print("Longitud de la lista", len(lista1))

