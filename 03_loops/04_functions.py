###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
  # docstring
  # cuerpo de la función
  return valor_de_retorno # opcional

"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
  print("¡Hola!")

# Ejemplo de una función con parámetro
def saludar_a(nombre):
  print(f"¡Hola {nombre}!")

saludar_a("midudev")
saludar_a("madeval")
saludar_a("pheralb")
saludar_a("felixicaza")
saludar_a("Carmen Ansio")

# Funciones con más parámetros
def sumar(a, b):
  suma = a + b
  return suma

result = sumar(2, 3)
print(result)

# ===================================================
# DOCUMENTAR LAS FUNCIONES CON DOCSTRING
# ===================================================v

def restar(a, b):
  """ Resta dos números y devuelve el resultado """ # Sirve para documentar qué hace el método, también aparece cuando pasas el ratón por encima del nombre del método.
  return a - b

# ===================================================
# PARÁMETROS POR DEFECTO
# ===================================================

def multiplicar(a, b = 2):
  """ Si solamente determinados el parámetro 'a', el valor de 'b' será el que hayamos puesto en el método al llamarlo, 
   sino, también podemos decirle qué valor debe de tener. """
  return a * b

print(multiplicar(2))
print(multiplicar(2, 3))

# ===================================================
# ARGUMENTOS POR POSICIÓN
# ===================================================

def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
# Colocas las variables en un orden determinado, pero si tú varías ese orden, rompes el método:
describir_persona(1, 25, "gato") # ❌
describir_persona("midudev", 25, "gato") # ✅
describir_persona("hombre", "madeval", 39) # ❌

# ===================================================
# ARGUMENTOS POR CLAVE
# ===================================================

# parámetros nombrados
# De esta manera, ya exiges que el valor de los parámetros sean esos, independientemente del orden que se establezca:
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# ===================================================
# ARGUMENTOS DE LONGITUD DE VARIABLE (*args)
# ===================================================

def sumar_numeros(*args):
  """ Sumará los números con un valor indefinido de parámetros, que se sabrá una vez se llame al método """
  suma = 0 # Determinamos la variable con valor 0
  for numero in args: # Para todos los números dentro de 'args' (que son toooooodos los valores)
    suma += numero # Cógelos y ves sumándolos
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# ===================================================
# ARGUMENTOS DE CLAVE-VALOR VARIABLE (**kwargs)
# ===================================================

def mostrar_informacion_de(**kwargs): # kwargs -> K words 
  """ Podemos introducirle tantos parámetros nombrados como queramos """
  for clave, valor in kwargs.items(): # Para cada 'clave' (nombre de la variable) y 'valor' (valor de la variable) dentro de todos los parámetros de **kwargs
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora