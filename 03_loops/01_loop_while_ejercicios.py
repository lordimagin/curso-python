###
# EJERCICIOS (while)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1: Cuenta atrás.")
print("---------------------------------------------\n")

contador = 0
while contador <= 10:
    print(contador)
    contador +=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2: Suma de números pares (while).")
print("---------------------------------------------\n")

contador = 0
suma_pares = 0

while contador <= 20: # Mientras el contador sera igual o menor a 20
    if contador % 2 == 0: # Y si el contador es divisible entre 2
        suma_pares += contador # Añade el contador a 'suma_pares' y lo suma con los anteriores.
    contador +=1 # Incrementa en uno el contador y volvemos a empezar.

print("La suma de los números pares es:", suma_pares)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3: Factorial de un número.")
print("---------------------------------------------\n")

numero = -1 # Inicializamos el numero en -1 para que el bucle se inicie, al menos, una vez.

while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except: # En lugar de enseñarle el error técnico, ponle esto:
    print("Lo que introduces debe ser un número, que si no peta!") # Volvemos a empezar el bucle.

factorial = 1 # Empezamos con 1 (que es el valor neutro de la multiplicación)
contador = 1

while contador <= numero: # Mientras el contador sea menor o igual que el número:
   factorial *= contador # Añade el número al factorial y lo multiplicas.
   contador += 1 # Incrementamos en uno el contador y volvemos a hacer el bucle.

print(f"El factorial del número {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4: Validación de contraseña.")
print("---------------------------------------------\n")

password = "" # Iniciamos la password vacía

while len(password) < 8: # Mientras la longitud de la password sea menor de 8 carácteres:
   password = input("Introduzca una contraseña (debe de contener 8 carácteres mínimo): ")
   if len(password) < 8: # Si la password es más corta de 8:
      print("La contraseña es demasiado corta. Inténtalo de nuevo.")

print("Contraseña válida.")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5: Tabla de multiplicar.")
print("---------------------------------------------\n")

numero = -1

# Validación de que se pone lo que se pide y no otra cosa.
while numero < 0:
   try:
      numero = int(input("Escribe un número: "))
      if numero < 0:
         print("El número debe de ser positivo. Introduce un número correcto.")
   except:
      print("Lo que introduces no es un número!")

multiplicador = 0 # Iniciamos el multiplicador de la tabla a 0 (porque existe el 1 x 0)

while multiplicador <= 10: # Mientras el multiplicador sea menor o igual a 10 (porque la tabla es hasta el 10)
   resultado = numero * multiplicador # Ponemos el resultado de la multiplicación en una variable
   print(f"{numero} x {multiplicador} = {resultado}" ) # Imprime NUMERO x MULTIPLICADOR = RESULTADO
   multiplicador += 1 # Incrementa en 1 el valor del multiplicador y volvemos al bucle.


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.

print("\nEjercicio 6: Números primos hasta N.")
print("---------------------------------------------\n")

n = -1

# Validación de que se pone lo que se pide y no otra cosa.
while n < 0:
   try:
      n = int(input("Escribe un número: "))
      if n < 0:
         print("El número debe de ser positivo. Introduce un número correcto.")
   except:
      print("Lo que introduces no es un número!")

numero = 2 # Iniciamos a 2 porque es el primer número primo.
while numero <= n: # Mientras el número sea menor o igual al número escrito (n):
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    # Este es el truco de optimización:
    # No hace falta comprobar todos los divisores hasta numero - 1.
    # Basta con hacerlo hasta la raíz cuadrada del número, porque si numero tiene un divisor mayor que su raíz, el otro divisor ya habrá sido probado antes.
    # 📘 Ejemplo:
    # Para numero = 36, la raíz cuadrada es 6.
    # Si 36 es divisible por 9, entonces también lo es por 4, y ya lo habrías comprobado antes.
    if numero % divisor == 0: # Comprobación de si el número es primo o no.
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1 # Incrementamos en 1 el divisor y volvemos a empezar.
  if es_primo:
    print(numero)

  numero += 1
