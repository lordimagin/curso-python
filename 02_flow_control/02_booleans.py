###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# ===================================================
# BOOLEANOS BÁSICOS: TRUE / FALSE
# ===================================================

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# ===================================================
# OPERADORES DE COMPARACIÓN CON INT Y STR
# ===================================================

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True --> Va comparando letra a letra, como cuando ordenas los archivos por nombre.
print("'Hola' == 'hola'", "Hola" == "hola") # False --> Es sensible a las mayus.

# ===================================================
# OPERADORES LÓGICOS: AND, OR, NOT
# ===================================================

print("\nOperadores lógicos:")
print("True and True:", True and True)    # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)              # False
print("not False:", not False)            # True

# ===================================================
# TABLAS DE LA VERDAD 
# ===================================================

# AND
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

# OR
print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

# NOT
print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)