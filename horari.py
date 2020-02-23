
import array as arr
from dades import Dades
from posicio import Posicio
class Horari:

    def __init__(self):
        self.horari = [[None] * 13] * 5
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
        self.dades = Dades()

    def set_hora(asignatura, grup):
        grup_lab = grup
        grup_teo = (grup / 10) * 10

        hores_teo = dades.buscar_hores(asignatura, grup_teo)
        hores_lab = dades.buscar_hores(asignatura, grup_lab)

        for i in range(0, Len(hores_teo)):
            posicio = Posicio(asignatura, grup_teo)
            x = hores_teo[i]['inici']
            hora = self.hores[x]
            dia = hores_teo[i]['dia_setmana'] - 1
            self.horari[hora][dia] = posicio

        for i in range(0, Len(hores_lab)):
            posicio = Posicio(asignatura, grup_lab)
            x = hores_lab[i]['inici']
            hora = self.hores[x]
            dia = hores_lab[i]['dia_setmana'] - 1
            self.horari[hora][dia] = posicio

