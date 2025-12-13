###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re

# =================================================================================================
# 1. EL PUNTO (.)
# =================================================================================================

# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la
# En la posición del punto, puede haber CUALQUIER cosa, cualquier caracter normal o especial.

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------------

# r = Expresión Regular.

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\." # La \ eliminar el significado especial y lo convierte en un punto normal.

matches = re.findall(pattern, text)

print(matches)

# =================================================================================================
# \d (COINCIDE CON CUALQUIER DÍGITO (0-9))
# =================================================================================================

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{9}', text) # Encuéntrame un grupo de 9 dígitos juntos.
found2 = re.findall(r'\d', text) # Encuéntrame dígito a dígito.

print(found)
print(found2)

# =================================================================================================
# # EJERCICIO DE REEMPLAZO
# =================================================================================================

# Alterna entre "NOMBRE" y "EDAD" para cada coincidencia
# contador = 0
 
# def reemplazar_alternado(match):
#    global contador
#    contador = contador + 1
#    return "NOMBRE" if contador % 2 == 1 else "EDAD"
 
# texto = "Hola, mi nombre es Juan y tengo 30 años."
# resultado = re.sub(r"\b\w+\b", reemplazar_alternado, texto)
 
# print(resultado)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}" # +34 XXXXXXXXX
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# =================================================================================================
# \w (COINCIDE CON CUALQUIER CARÁCTER ALFANUMÉRICO ((a-z, A-Z, 0-9, _))
# =================================================================================================

text = "el_rubius_69"
pattern = r"\w" # Encuentra todos los carácteres que no sean especiales.
found = re.findall(pattern, text)
print(found)

# =================================================================================================
# \s (COINCIDE CON CUALQUIER ESPACIO EN BLANCO (ESPACIO, TABULACIÓN, SALTO DE LÍNEA))
# =================================================================================================

text = "Hola mundo\n¿Cómo estás?\t" # \n -> Salto de página \t -> tabulación
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# =================================================================================================
# ^ (COINCIDE CON EL PRINCIPIO DE UNA CADENA)
# =================================================================================================

username = "423_name%22" 
pattern = r"^\w" # validar nombre de usuario
# Mírame si el comienzo empiece por un carácter alfanumérico.

valid = re.search(pattern, username)

if valid: print("El nombre de usuario es válido.")
else: print("El nombre de usuario no es válido.")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} " # Mírame que lo introducido empiece por "+" seguido de 1 a 3 números.

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido.")
else: print("El número de teléfono no es válido.")

# =================================================================================================
# $ (COINCIDE CON EL FINAL DE UNA CADENA)
# =================================================================================================

text = "Hola mundo."
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail válido")
else: print("El correo no es válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b[\w-]+\.txt\b"
# Empieza por cualquier alfanumérico o guión (todas la veces que quiera -> +), seguido de un punto y que termine en txt.

valid = re.findall(pattern, files)
# 🧠 Explicación rápida del patrón

# \b → Principio de la palabra

# [\w-]+ → letras, números, _ y -

# \. → punto literal

# txt → extensión

# \b → fin de palabra

print(valid)


# =================================================================================================
# \b (COINCIDE CON EL PRINCIPIO O FINAL DE UNA PALABRA)
# =================================================================================================

text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b" # El principio de la palabra que empiece por "c" y el final sea "a"

found = re.findall(pattern, text)
print(found)

# =================================================================================================
# | (COINCIDIR CON UNA OPCIÓN U OTRA)
# =================================================================================================

fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)