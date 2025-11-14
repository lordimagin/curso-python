###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

# ===================================================
# GENERANDO UNA SECUENCIA DE NÚMEROS DEL 0 AL 9
# ===================================================v

for num in range(10): # Con un solo valor, le estamos diciendo hasta dónde queremos que haga el rango, donde por defecto será 0
  print(num)

# ===================================================
# RANGE(INICIO, FIN)
# ===================================================

for num in range(5, 10):
  print(num)

# ===================================================
# RANGE(INICIO, FIN, PASO)
# ===================================================

for num in range(0, 1000, 5): # Dame un rango de números entre el 0 y 1000 contando de 5 en 5
  print(num)

for num in range(-5, 0):
  print(num)

for num in range(10, 0, -1): # Genera un rango 'restanto' de 1 en 1 del 10 al 0
  print(num)

for num in range(0, 444):
  print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# ===================================================
# REPETICIONES
# ===================================================

# seria para hacerlo cinco veces
for _ in range(5):
  print("hacer cinco veces algo")