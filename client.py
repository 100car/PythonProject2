from http.client import responses

from colorama import init
init()  # <-- оце і є "перед логами"


import requests


response = requests.post("http://localhost:8000/hello/Mary")
print(response.json())

name_data = {
    "name": 'John'
}

response1 = requests.post("http://localhost:8000/hello_json", json=name_data)
print(response1.json())


