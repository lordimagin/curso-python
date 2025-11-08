###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

# ===================================================
# BUCLE CON UNA SIMPLE CONDICIÓN
# ===================================================

contador = 0 # Creamos un contador 

while contador <= 5: # Mientras el contador sea menor o igual a 5:
  print(contador) # Ve mostrándome el valor del contador.
  contador += 1 # Con esto vamos incrementando en 1 el valor del contador hasta llegar a la menta || es super importante para evitar un bucle infinito

# ===================================================
# UTILIZANDO LA PALABRA 'BREAK', PARA ROMPER EL BUCLE
# ===================================================

print("\n Bucle while con break:")
contador = 0

while True: # Mientras sea verdad (osea, siempre):
  print(contador) # muéstrame el valor del contador
  contador += 1 # súmame 1 al valor del contador
  if contador == 5: # Pero ojito, si el valor del contador = 5:
    break # párame el bucle

# ===================================================
# UTILIZANDO LA PALABRA 'CONTINUE' 
# ===================================================

# 'Continue', que lo hace es saltar esa iteración en concreto y continuar con el bucle
# Puede usarse como filtro
print("\n Bucle con continue")
contador = 0
while contador < 10: # Mientras el contador sea menor a 10:
  contador += 1 # vamos incrementando el valor del contador en 1

  if contador % 2 == 0: # pero ojito, si el valor del contador es divisible entre 2
    continue # procedemos a seguir con la siguiente iteración (que volvamos a empezar el bucle, independientemente de todo lo que haya debajo)

  print(contador)

# ===================================================
# BUCLE CON EL 'ELSE'
# ===================================================
# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5: # Mientras el valor del contador sea menor a 5:
  print(contador) # imprime el valor del contador
  contador += 1 # ve aumentando el valor del contador
  # break --> cuando hay un 'break' en el bucle y se ejecuta, no pasamos al 'else' y no se inicia. || Único caso donde el 'else' no se ejecuta.
else: # Cuando el valor del contador llegue a 5, hazme lo siguiente:
  print("El bucle ha terminado")

# ===================================================
# CASOS PRÁCTICOS
# ===================================================

# pedirle al usuario un número que tiene que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0: # Mientras el valor del número sea menor a 0:
  numero = int(input("Escribe un número positivo: ")) # Le pedimos al usuario que introduzca un número (al escribir, es una cadena, con lo que lo transformamos en INT)
  if numero < 0: # Si el número es menor a 0, me imprimirá lo de abajo y volveremos a empezar el bucle.
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}") # Si el valor del número es mayor a 0, escribe esto.

# El único problema es que si escribe alguna letra, el programa peta, por eso haremos el siguiente punto.

# ===================================================
# BUCLES CON 'TRY - EXCEPT'
# ===================================================

# Lo que conseguimos con el try-except es controlar el error que salga
# para que no le aparezca al usuario y determinar qué es lo que queremos que 
# el usuario vea por pantalla.
numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except: # En lugar de enseñarle el error técnico, ponle esto:
    print("Lo que introduces debe ser un número, que si no peta!") # Volvemos a empezar el bucle.

print(f"El número que has introducido es {numero}")

