import requests
import os
import json

"""
Descargar archivos pesados
"""

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form', offset=0):

    args = {'offset':offset} if offset else {}

    response = requests.get(url, params=args)
    if response.status_code == 200:

        payload = response.json()
        result = payload.get('results', [])

        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)

        next = input("Continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)

if __name__ == '__main__':

    url = 'https://pokeapi.co/api/v2/pokemon-form'
    offset = 0
    get_pokemons(url, offset=offset)