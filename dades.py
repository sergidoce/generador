import requests
import json

class Dades:

    def __init__(self):
        self.refresh()

    def refresh(self):
        data = requests.get('https://api.fib.upc.edu/v2/assignatures/places/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.data_places_lliures = json.loads(data.text)
        data = requests.get('https://api.fib.upc.edu/v2/quadrimestres/2019Q2/classes/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.data_classes = json.loads(data.text)

    def get_grupos_teoria(self, assig):
        res = self.data_classes['results']
        grups = []
        for i in range(0, len(res)):
            if res[i]['codi_assig'] == assig and res[i]['tipus'] == "T" and res[i]['grup'] not in grups:
                grups.append(res[i]['grup'])

        return grups


    def get_clases_teoria(self, assig, grup):
        res = self.data_classes['results']
        clases = []
        for i in range(0, len(res)):
            if res[i]['codi_assig'] == assig and res[i]['tipus'] == "T" and res[i]['grup'] == grup:
                clases.append(res[i])

        return clases
            

    def get_grupos_lab(self, assig, grupo):
        res = self.data_classes['results']
        grups = []
        for i in range(0, len(res)):
            if res[i]['codi_assig'] == assig and res[i]['tipus'] == "L" and (int(res[i]['grup']) < (grupo + 10) and int(res[i]['grup']) > grupo):
                grups.append(res[i])

        return grups