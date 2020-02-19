import urllib, requests
import json
from bs4 import BeautifulSoup
from horari import Horari

class Generador:
    

    def __init__(self):
        self.asignaturas = []
        self.nomes_matins = False
        self.nomes_tardes = False
        self.horaris = []
        self.grups = [[]]

        data = requests.get('https://api.fib.upc.edu/v2/assignatures/places/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.info_places_lliures = json.loads(data.text)
        
        data = requests.get('https://api.fib.upc.edu/v2/quadrimestres/2019Q2/classes/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
        self.info_classes = json.loads(data.text)

    def insertarAsignaturas(self):
        
        n_asignaturas = int(input("¿Cuantas asignaturas quieres cursar? : "))

        for i in range(0, n_asignaturas):
            asignatura = input()
            self.asignaturas.append(asignatura)

    
    def ajustes_adicionales(self):
        matins = input("¿Quieres un horario solo de mañanas? : ")
        if matins == "si":
            self.nomes_matins = True
            self.nomes_tardes = False
        else:
            tardes = input("¿Quieres un horario solo de tardes? : ")
            if tardes == "si":
                self.nomes_matins = False
                self.nomes_tardes = True

    def prova_grups(self):
        print(self.info_places_lliures.keys)
        
