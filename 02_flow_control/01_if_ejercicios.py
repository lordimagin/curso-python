###
# EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nExercicio 1: Determinar el mayor de dos números")
print("---------------------------------------------\n")
num1 = int(input("Introduce el primer número: \n"))
num2 = int(input("Introduce el segundo número: \n"))

def num_mayor(num1, num2):
    if num1 > num2: # Si el num1 es más grande que el num2:
        print(f"El {num1} es más grande que el {num2}")
    elif num1 < num2: # Pero si el num1 es más pequeño que el num2:
        print(f"El {num1} es más pequeño que el {num2}")
    else: # Si no, será:
        print(f"El {num1} es igual que el {num2}")

print(f"Los dos números añadidos son: {num1} y {num2}\n")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEjercicio 2: Calculadora simple")
print("---------------------------------------------\n")

num3 = int(input("Introduce el primer número: \n")) # Pedimos que el usuario nos de un número
num4 = int(input("Introduce el segundo número: \n")) # Pedimos que el usuario nos de otro número
operacion = input("Qué cálculo matemático quieres hacer? \n") # Pedimos que el usuario nos de una operación

def calculadora (num3, num4):
    if operacion == "*": # Si la operación es una multiplicación:
        print(f"El resultado es: {num3} * {num4} = {num3 * num4}")
    elif operacion == "+": # O si la operación es una suma:
        print(f"El resultado es: {num3} + {num4} = {num3 + num4}")
    elif operacion == "-": # O si la operación es una resta: 
        print(f"El resultado es: {num3} - {num4} = {num3 - num4}")
    elif operacion == "/": # O si la operación es una división: 
        if num4 == 0: # Y además el segundo número es un 0:
            print("Error: No se puede dividir entre 0.")
        else: # Si no hazme la división normal.
            print(f"El resultado es: {num3 / num4}")
    else: # Si no es nada de lo anterior:
        print("Algo ha salido mal.")

calculadora(num3, num4)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio 3: Año bisiesto")
print("---------------------------------------------\n")
anio = int(input("Introduce un año: "))

def bisiesto(anio):
# Un año es bisiesto si es divisible por 4 (= 0), excepto si es divisible por 100 (!= 0) pero no por 400 (= 0).
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"{anio} es un año bisiesto.")
    else:
        print(f"{anio} no es un año bisiesto.")

bisiesto(anio)

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4: Categorizar edades")
print("---------------------------------------------\n")
edad = int(input("Introduce una edad: ")) # Introducimos un número int

def edades(edad: int):
    if 0 <= edad <= 2: # Si la edad está entre 0 y 2:
        print("Bebé")
    elif 3 <= edad <= 12: # O si la edad está entre 3 y 12:
        print("Niño")
    elif 13 <= edad <= 17: # O si la edad está entre 13 y 17:
        print("Adolescente")
    elif 18 <= edad <= 64: # O si la edad está entre 18 y 64:
        print("Adulto")
    elif edad >= 65: # O si la edad es más de 65:
        print("Adulto mayor")
    else: # De lo contrario:
        print("Edad no válida.")

edades(edad)