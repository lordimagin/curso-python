###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# =================================================================================================
# * (PUEDE APARECER 0 Ó MÁS VECES)
# =================================================================================================

text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

text = "dddd aaa ccc a bb aa casa aaba"
pattern = "\ba*b\b"
matches = re.findall(pattern, text)
print(matches)
print(len(matches))

# | Palabra                 | ¿Coincide? | Motivo          |
# | ----------------------- | ---------- | --------------- |
# | dddd                    |    ❌      | no hay b        |
# | aaa                     |    ❌      | no hay b        |
# | ccc                     |    ❌      | no hay b        |
# | a                       |    ❌      | no hay b        |
# | bb                      |    ❌      | dos b           |
# | aa                      |    ❌      | no hay b        |
# | casa                    |    ❌      | no termina en b |
# | aaba                    |    ❌      | termina en a    |
# | ab (si existiera)       |    ✅      | a* + b          |
# | b                       |    ✅      | 0 a + b         |

# 🧠 Regla clave (apúntala)

# Si el ejercicio habla de “palabras”, necesitas \b
# Si no, el regex te engaña.

# =================================================================================================
# + (UN CARÁCTER QUE APARECE MÁS VECES)
# =================================================================================================

text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# =================================================================================================
# ? (CERO O UNA VEZ)
# =================================================================================================

text = "aaabacb"
pattern = "a?b" # La 'a' puede estar delante de la 'b' o no.
# En al caso de que exista una 'a' delante de la 'b', quiero que me la devuelvas, no solamente que me la cuentes.
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"(?:\+34)?\d{9}"
matches = re.findall(pattern, phone) 
# El .findall devuelve solo los grupos capturados (si existen).
# (\+34)? -> estoy capturando el +34.
# (?:\+34)? -> Le estoy diciendo que NO quiero que me capture esto, simplemente que tenga en cuenta el grupo.
print(matches)

# =================================================================================================
# {n} (EXACTAMENTE n VECES)
# =================================================================================================

text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
# Es como si tuviera un puntero y va hacia delante, al encontrar las primeras 3 'a' el puntero se detiene y dice:
# "Eh, aquí hay 3 'a', pues lo devuelvo, voy a seguir", hasta que encuentre otras 3 'a' o no.
matches = re.findall(pattern, text)

print(matches)

# =================================================================================================
# {n, m} (DE 'n' A 'm' VECES)
# =================================================================================================

text = "u uu uuu u"
pattern = r"\w{2,3}"
# Aquí trabaja similar al anterior, busca con el puntero cadenas de letras que sean de 2 ó 3 veces.
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# 🧠 Regla clave
# Si el ejercicio habla de “palabras”, necesitas \b
# Si no, el regex te engaña.

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b" 
# Carácteres alfanuméricos que se repitan 6 veces o más que tengan 6 letras o más) dentro de una palabra.
matches = re.findall(pattern, words)
print(matches)