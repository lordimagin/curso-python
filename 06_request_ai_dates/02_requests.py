### =========================================================================================== ###
### =========================================================================================== ###
#                                 PETICIONES EN API'S CON PYTHON                                  #
### =========================================================================================== ###
### =========================================================================================== ###

# =================================================================================================
# 1. SIN DEPENDENCIAS (DIFÍCIL).
# =================================================================================================

import urllib.request
import json

DEEPSEEK_API_KEY = "xxx"

api_posts = "https://jsonplaceholder.typicode.com/posts/" # API con la que trabajaremos.

try:
  response = urllib.request.urlopen(api_posts) # Quiero que vayas a esa URL y la abras.
  data = response.read() # Una vez abierta la URL tenemos que leer esos datos
  json_data = json.loads(data.decode('utf-8')) # Pero qué pasa? Python no ha podido decodificar tocavía
  # Así que le tenemos que decir que cargue un json de los datos que tenemos que decodificar en 'utf-8':
  # Vamos a decodificar los datos y cargarlos en un JSON.
  print(json_data) # Mostramos lo que hay en el JSON.
  response.close() # Cerramos la pestaña de la URL.
except urllib.error.URLError as e: # Usamos un 'try-except' por si nos diera un error que no pete, 
  # simplemente que aparezca un error escrito.
  print(f"Error en la solicitud: {e}")

# =================================================================================================
# 2. CON DEPENDENCIAS (REQUESTS/PETICIONES).
# =================================================================================================

import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
json = response.json()
print(json[2])

# =================================================================================================
# 3. POST.
# =================================================================================================

print("\nPOST:")
try:
  response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# =================================================================================================
# 4. PUT.
# =================================================================================================

print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1,
    })

  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# =================================================================================================
# 5. USANDO API'S.
# =================================================================================================

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "sk-XXXXXXXX"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])