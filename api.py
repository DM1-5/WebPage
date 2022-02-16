import requests
import os

# Peticion http a la api de randomfox
response = requests.get("https://randomfox.ca/floof")

# Se imprime el json
print(response.json())

fox = response.json()

# Se guarda el value de la key image
fox_image = fox["image"]

# Se abre la url en una nueva pestaña usando firefox
os.system(f"firefox {fox_image}")
