# <h1 align="center">**`Data Quality Report`**</h1>

## Analizando el Dataset

### **Paso N°1:**

En el dataset nos encontramos con los 27 discos existentes hasta la actualidad en la plataforma de Spotify, de la artista musical llamada Taylor Swift.
Se puede ver el 'ID' perteneciente a cada uno de los albums, el 'Nombre del artista', y la 'Popularidad del artista'; y que no hay fallos visibles en estos datos.

### **Paso N°2:**

En el nuevo DataFrame que contiene la información desanidada de la columna 'Albums', ya podemos encontrar las primeras anomalías:
- En la columna 'Nombre del album' podemos encontrar un valor nulo, y también un valor duplicado.
- En la columna 'Total de canciones en el album' podemos encontrar un valor no numérico, y también que que el tipo de dato no es el adecuado.

### **Paso N°3:**

