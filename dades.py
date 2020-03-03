import requests
import json

class Dades:

    def __init__(self):
        self.refresh()
        self.hores = {

            "10" : 10,
            "11" : 11,
            "12" : 12,
            "13" : 13,
            "14" : 14,
            "20" : 20,
            "21" : 21,
            "22" : 22,
            "23" : 23,
            "24" : 24,
            "30" : 30,
            "31" : 31,
            "32" : 32,
            "33" : 33,
            "34" : 34,
            "40" : 40,
            "41" : 41,
            "42" : 42,
            "43" : 43,
            "44" : 44,
            "50" : 50,
            "51" : 51,
            "52" : 52,
            "53" : 53,
            "54" : 54,
        }

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
            
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get_grupos_lab(self, assig, grupo):
        res = self.data_classes['results']
        grups = []
        
        for i in range(0, len(res)):
            if self.is_number(res[i]['grup']):    
                grupo_lab_int = self.hores[res[i]['grup']]
                grupo_teo_int = self.hores[grupo]
                
                if (res[i]['codi_assig'] == assig and res[i]['tipus'] == "L") and (grupo_lab_int < (grupo_teo_int + 10) and grupo_lab_int > grupo_teo_int) and res[i]['grup'] not in grups:
                    grups.append(res[i]['grup'])

        return grups


    def get_clases_lab(self, assig, grupo):
        res = self.data_classes['results']
        clases = []
        for i in range(0, len(res)):
            if res[i]['codi_assig'] == assig and res[i]['tipus'] == "L" and res[i]['grup'] == grupo:
                clases.append(res[i])

        return clases
