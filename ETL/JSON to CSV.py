# Importar las librerías correspondientes.
import json 
import pandas as pd

# Guardamos la ruta del archivo.
ruta = 'taylor_swift_spotify.json'

# Guardamos la información del archivo en un DataFrame.
dataset_to_transform = pd.read_json(ruta)

# Guardamos el contenido del DataFrame en un nuevo archivo con extensión CSV.
dataset_to_transform.to_csv('dataset.csv', index = False)