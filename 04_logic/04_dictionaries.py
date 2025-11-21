###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ===================================================
# EJEMPLO TÍPICO DE DICCIONARIO (OBJETOS EN JAVASCRIPT)
# ===================================================

# llave : valor
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# ===================================================
# ACCESO A LOS VALORES
# ===================================================

print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# ===================================================
# MODIFICACIÓN DE LOS VALORES
# ===================================================

persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# ===================================================
# ELIMINACIÓN COMPLETA DE UNA PROPIEDAD (DEL)
# ===================================================

del persona["edad"]
# print(persona)

# De esta manera guardamos el valor eliminado a una variable.
es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}")
print(persona)

# ===================================================
# SOBREESCRIBIR UN DICCIONARIO CON OTRO DICCIONARIO (UPDATE)
# ===================================================

a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

a.update(b) # Quiero que la 'a' se actualice con los datos de la 'b' y los sobreescriba.
print(a)

# ===================================================
# COMPROBACIÓN SI EXISTE UNA PROPIEDAD
# ===================================================

print("name" in persona) # False # Muéstrame si la propiedad 'name' existe dentro de la clase 'persona'
print("nombre" in persona) # True # Muéstrame si la propiedad 'name' existe dentro de la clase 'persona'

# ===================================================
# OBTENCIÓN DE TODAS LAS CLAVES (.KEYS())
# ===================================================

print("\nkeys:")
print(persona.keys()) #las llaves son los atributos, las propiedades

# ===================================================
# OBTENCIÓN DE TODOS LOS VALORES (.VALUES())
# ===================================================

print("\nvalues:")
print(persona.values()) # El valor es eso, el valor de cada propiedad/atributo

# ===================================================
# OBTENCIÓN TANTO DE LA CLAVE COMO EL VALOR (.ITEMS())
# ===================================================

print("\nitems:")
print(persona.items()) # Items equivale a todo, mostrando la llave y el valor

for key, value in persona.items():
  print(f"{key}: {value}")