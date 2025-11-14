###
# EJERCICIOS (range)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1: Imprimir números del 1 al 10 (inclusive)")
print("---------------------------------------------\n")

for num in range(1, 11):
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2: Imprimir números impares del 1 al 20 (inclusive)")
print("---------------------------------------------\n")

for num in range(1, 21, 2):
    print(num)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3: Imprimir múltiplos de 5")
print("---------------------------------------------\n")

for num in range(5, 51, 5):
    print(num)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4: imprimir números en orden inverso")
print("---------------------------------------------\n")

for num in range(10, 0, -1):
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5: Suma de números en un rango")
print("---------------------------------------------\n")

suma = 0
for num in range(1, 101):
    suma += num
    
print(f"La suma total es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6: Tabla de multiplicar")
print("---------------------------------------------\n")

numero = -1
while numero < 0:
   try:
      numero = int(input("Escribe un número: "))
      if numero < 0:
         print("El número debe de ser positivo. Introduce un número correcto.")
   except:
      print("Lo que introduces no es un número!")


for num in range(0, 11):
    print(f"{numero} x {num} = {numero*num}")