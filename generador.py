import requests
import json
from horari import Horari

class Generador:
    

    def __init__(self):
        self.asignaturas = []
        self.nomes_matins = False
        self.nomes_tardes = False
        self.horaris = []
        self.grups = [[]]


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

    def generar_horarios(self):

        horari = Horari()
        for i in range(0, Len(self.asignaturas)):
            trobat = buscar_grup(self.asignaturas[i], horari)
            if trobat == 0:
                break
            





        
