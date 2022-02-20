import requests
import json

url = "https://prueba-4797.restdb.io/rest/prueba"

headers = {
    'content-type': "application/json",
    'x-apikey': "18f57b35a362d92d5d92b28a124fef7fe4eb1",
    'cache-control': "no-cache"
}

nombre = input("¿A quien quieres buscar? \n") + '"}'

question = '?q={"Nombre":"' + nombre

peti = url + question

print(peti)

response = requests.request("GET", peti, headers=headers)
print(type(response.text))
final = json.load(response.text)
