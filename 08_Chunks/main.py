import requests
import os
import json

"""
Descargar archivos pesados
"""

if __name__ == '__main__':
    url = 'https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/03/16/15843437408247_310x174.jpg'

    response = requests.get(url, stream=True) #Realizando la peticion dejando la peticion abierta sin descargar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)

    response.close() #Cerrar la conexion


