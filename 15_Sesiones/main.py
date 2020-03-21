import requests
import os
import json



if __name__ == '__main__':

    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('jaisenberafel@gmail.com','xxxx')

    response = session.get(url)
    if response.ok:
        response = session.get('https://github.com/jaisenbe58r')
        if response.ok:
            print(response.cookies)

    else:
        print("Fallo de acceso\n")
        print(response.content)




