import array as arr
from horari import Horari

class Generador:

    def __init__(self):
        self.asignaturas = []
        self.nomes_matins = False
        self.nomes_tardes = False
        self.horaris = []


    def insertarAsignaturas(self):
        
        n_asignaturas = int(input("¿Cuantas asignaturas quieres cursar? : "))

        for i in range(0, n_asignaturas):
            asignatura = input()
            self.asignaturas.append(asignatura)

        print(self.asignaturas[2])