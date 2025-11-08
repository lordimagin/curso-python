###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd'] # lista1 = [0, 1, 2, 3]

# ===================================================
# AÑADIR O INSERTAR ELEMENTOS A LA LISTA
# ===================================================

# AÑADIR
lista1.append('e') # Añade un elemento al final
print(lista1)

# INSERTAR
# lista1.insert(posición en la que queramos insertar, elemento a insertar)
lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

# extend = extender el elemento con lo indicado
lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1)

# ===================================================
# ELIMINAR ELEMENTOS DE LA LISTA
# ===================================================

# lista1.remove() -> Eliminará la primera "@" que se encuentre, no todas, de la lista.
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

# lista1.pop() -> Elimina el último elemento de la lista o el del índice que le indiques.
ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve (te guarda el valor en el propio método)
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# ===================================================
# MÁS MÉTODOS ÚTILES
# ===================================================

print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort() # Coge la lista original y ordena sus posiciones PERO sin crear una nueva lista.
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers) # Crea una copia la lista original, ordena sus posiciones y te crea otra lista nueva.
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas) # Ordena la lista según la posición de las letras basándose en el abecedario
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula) por defecto")
frutas = ['manzana', 'Pera', 'limón', 'manzana', 'pera', 'Limón']
sorted_frutas = sorted(frutas) # El problema que tenemos es cuando se mezclan MAYUS y MINUS, que prioriza las mayúsculas.
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula) de la mejor manera")
frutas = ['manzana', 'Pera', 'Limón', 'Manzana', 'pera', 'limón']
frutas.sort(key=str.lower) # Con este método, le obligamos a ordenarlo como si todo estuviera en minúsculas.
print(frutas)

# ===================================================
# MÁS COSAS ÚTILES
# ===================================================

animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False
