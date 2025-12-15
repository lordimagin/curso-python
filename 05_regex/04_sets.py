import re


# =================================================================================================
# [:] - COINCIDE CON CUALQUIER CARÁCTER DENTRO DE LOS CORCHETES
# =================================================================================================

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"
# De principio a fin (^[...]$)debe contener TODO lo que le pongamos entre corchetes y que se repita varias veces (por el +):
# [\w._%+-]+
#   - Carácteres alfanuméricos.
#   - Un punto.
#   - Una barra baja.
#   - Un %.
#   - Un +.
#   - Un -.

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido.")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
# print(matches)
print("Se han encontrado", len(matches), "vocales:", matches)

# Una Regex para encontrar las palabras man, fan y ban, pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"
# Búscame todas las palabras que empiezan por [m, f o b] seguido de 'an'.
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
#pattern = r'\w+\b[mfb]an|[mfb]an|[mfb]an\w+\b'
pattern = r'[mfb]an'
# Encuentra cualquier aparición de "man, fan o ban", esté donde esté dentro de la palabra
matches = re.findall(pattern, text)
print(matches)


text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)