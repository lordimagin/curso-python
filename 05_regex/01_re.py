##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# =================================================================================================
# 1r PASO - IMPORTAR EL MÓDULO DE EXPRESIONES REGULARES "re".
# =================================================================================================

import re

# =================================================================================================
# 2do PASO - CREAR UN PATRÓN, QUE ES UNA CADENA DE TEXTO QUE DESCRIBE LO QUE QUEREMOS ENCONTRAR.
# =================================================================================================

pattern = "Hola" 

# =================================================================================================
# 3r PASO - EL TEXTO DONDE QUEREMOS BUSCAR.
# =================================================================================================

text = "Me llamo Marc. Hola mundo."

# =================================================================================================
# 4to PASO - USAR LA FUNCIÓN DE BÚSQUERA DE "re".
# =================================================================================================

result = re.search(pattern, text)

if result:
  print("He encontrado el patrón en el texto")
else:
  print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start()) # En este caso empieza en la posición 15, ya que es el inicio del texto en sí.

# .end() devolver la posición final de la coincidencia
print(result.end()) # Contamos letra a letra y te indica el final (19).

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")

# =================================================================================================
# ENCONTRAR TODAS LAS COINCIDENCIAS DE UN PATRÓN. (.findall())
# =================================================================================================

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text) # Cuántas veces sale? Devuelve una lista.

print(len(matches))
print(matches)

# =================================================================================================
# ENCONTRAR TODA LA INFORMACIÓN ANTERIOR. (.finditer())
# =================================================================================================

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# =================================================================================================
# MODIFICADORES
# =================================================================================================

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE) # Te paso el patrón y el texto PERO me ignoras si son mayus o minus.

if found: print(found)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

matches = re.findall(pattern, text, re.IGNORECASE)
#matches2 = re.finditer(pattern, text, re.IGNORECASE)

#for match in matches2:
#  print(match.group(), match.start(), match.end())

if matches: print(matches)

# =================================================================================================
# REEMPLAZAR EL TEXTO
# =================================================================================================

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
# re.sub(patrón, el remplazo que quiero modificar, el texto, flags -> modificadores (ej. ignorar las mayus y minus))
print(new_text)