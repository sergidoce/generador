import requests
import json

class Dades:

    def __init__(self):
        refresh()

    def refresh():
        data = requests.get('https://api.fib.upc.edu/v2/assignatures/places/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.data_places_lliures = json.loads(data.text)
        data = resquests.get('https://api.fib.upc.edu/v2/quadrimestres/2019Q2/classes/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.data_classes = json.loads(data.text)