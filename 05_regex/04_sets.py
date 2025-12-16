import re

# =================================================================================================
# [:] - COINCIDE CON CUALQUIER CARÁCTER DENTRO DE LOS CORCHETES.
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

# =================================================================================================
# [^] - COINCIDE CON CUALQUIER CARÁCTER QUE NO ESTÉ DENTRO DE LOS CORCHETES.
# =================================================================================================

text = "Hola mundo"
pattern = r"[^aeiou]"
# Devuélveme todo aquello que no coincida con lo que hay dentro de los corchetes.
matches = re.findall(pattern, text)
print(matches)

# =================================================================================================
# EJERCICIO FINAL.
# =================================================================================================

# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

### /[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}/
# [\w._%+-] -> Cualquier cosa que esté aquí:
#   - Carácteres alfanuméricos.
#   - Un punto.
#   - Una barra baja.
#   - Un %.
#   - Un +.
#   - Un -.
# +@ -> Tantas veces como sea posible antes de la '@'.
# [\w.-] -> Cualquier cosa que esté aquí:
#   - Carácteres alfanuméricos.
#   - Un punto.
#   - Un guión.
# +\. -> Tantas veces como sea posible antes del '.'.
# [a-zA-Z]{2,4} -> Extensión (.es, .com, .org, etc):
#   - Carácteres alfanuméricos.
#   - Un punto.
#   - Una barra baja.

## Buscar corner cases que no pasa y arreglarlo:
text = "lo.que+sea@shopping.online"
#text2 = "marc.gomis07@gmail.com"
pattern = r'^[\w._%+-]+@[\w.-]+\.[a-zA-Z.]+$'
matches = re.findall(pattern, text)
print(matches)

text = "michael@gov.co.uk"
pattern = r"^[\w._%+-]+@[\w-]+(?:\.[\w-]+)+$"
matches = re.findall(pattern, text)
print(matches)

# Si hay un () -> capturará solamente lo que hay en su interior.
# Con el .findall, solamente mostrará lo capturado: ['.uk']
# Si no queremos que se capture, añadimos '?:' dentro del () para decirle que ignore la captura.

# 🧠 Regla de oro
#   - Validar → re.search o re.match
#   - Extraer texto → re.findall
#   - Usas findall + paréntesis → devuelve SOLO los grupos, lo que hay entre ()
#   - No quieres capturar → (?: ...)