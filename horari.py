
import array as arr
from dades import Dades
from posicio import Posicio
class Horari:

    def __init__(self):
        self.horari = [[None for x in range(5)]  for x in range(13)]
        self.hores = {

            "08:00" : 0,
            "09:00" : 1,
            "10:00" : 2,
            "11:00" : 3,
            "12:00" : 4,
            "13:00" : 5,
            "14:00" : 6,
            "15:00" : 7,
            "16:00" : 8,
            "17:00" : 9,
            "18:00" : 10,
            "19:00" : 11,
            "20:00" : 12,
        }

        self.dies = {

            0 : "Dilluns",
            1 : "Dimarts",
            2 : "Dimecres",
            3 : "Dijous",
            4 : "Divendres",

        }
        self.dades = Dades()

    def ponerTeoria(self, assig, grupo):

        clases = self.dades.get_clases_teoria(assig, grupo)
        
        for i in range(0, len(clases)):

            assig = clases[i]['codi_assig']
            grupo = clases[i]['grup']
            dia = clases[i]['dia_setmana']
            hora = clases[i]['inici']
            durada = clases[i]['durada']
            hora_int = self.hores[hora]

            if self.horari[hora_int][dia-1] is not None:
                return False    
            else:
                posicio = Posicio(assig, grupo)
                self.horari[hora_int][dia-1] = posicio
                if durada == 2:
                    self.horari[hora_int + 1][dia - 1] = posicio
                
        return True

    def eliminar(self, assig, grupo):
        for i in range(0, 13):
            for p in range(0, 5):
                if self.horari[i][p] is not None:
                    if self.horari[i][p].get_assig() == assig and self.horari[i][p].get_grupo() == grupo:
                        self.horari[i][p] = None
                        print("He eliminado una posicion de " + assig + " del grupo " + grupo)


    def ponerLab(self, assig, grupo):
        clases = self.dades.get_clases_lab(assig, grupo)

        for i in range(0, len(clases)):
            dia = clases[i]['dia_setmana']
            hora = clases[i]['inici']
            durada = clases[i]['durada']
            hora_int = self.hores[hora]

            if self.horari[hora_int][dia-1] is not None:
                return False    
            else:
                posicio = Posicio(assig, grupo)
                self.horari[hora_int][dia-1] = posicio
                if durada == 2:
                    self.horari[hora_int + 1][dia - 1] = posicio   
        return True



    def print_horari(self):
        for i in range(0, 5):
            for p in range(0, 13):
                print(self.dies[i], end=" ")
                print(p, end=" ")
                if self.horari[p][i] == None:
                    print("None")
                else:
                    self.horari[p][i].print_posicio()