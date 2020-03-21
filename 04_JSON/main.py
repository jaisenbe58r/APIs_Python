import requests
import os
import json

if __name__ == '__main__':
    url = "https://httpbin.org/get"
    args = {'nombre':'Jaime', 'curso':'python', 'nivel':'intermedio'}
    
    response = requests.get(url, params = args)

    if response.status_code == 200:
        # response_json = response.json() #Diccionario
        # origin = response_json['origin']
        # print(origin)

        response_json = json.loads(response.text)
        origin = response_json["origin"]
        print(origin)
