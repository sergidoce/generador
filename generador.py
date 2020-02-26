#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        dades = Dades()


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

    def i_generar_horarios(self, horari, assig, grupo, cont_assig):
        res = horari.ponerLab(assig, grupo)
        if res:
            if cont_assig == Len(self.asignaturas) - 1:
                self.horarios.append(horari)
                return

            cont_assig = cont_assig + 1
            assig = self.asignaturas[cont_assig]
            grupos_teoria = dades.get_grupos_teoria(assig)

            for i in range(0, Len(grupos_teoria)):
                if horari.ponerTeoria(assig, grupos_teoria[i]):
                    grupos_lab = dades.get_grupos_lab(assig, grupos_teoria[i])
                    for p in range(0, Len(grupos_lab)):
                        i_generar_horarios(self, horari, assig, grupos_lab[p], cont_assig)

                    horari.eliminarTeoria(assig, grupos_teoria[i])
        else:
            return

    def generar_horarios(self):

        horari = Horari()
        assig = self.asignaturas[0]
        cont_assig = 0

        grupos_teoria = dades.get_grupos_teoria(assig)
        for i in range(0, Len(grupos_teoria)):
            if horari.ponerTeoria(assig, grupos_teoria[i]):
                grupos_lab = dades.get_grupos_lab(assig, grupos_teoria[i])
                for p in range(0, Len(grupos_lab)):
                    i_generar_horarios(self, horari, assig, grupos_lab[p], cont_assig + 1)

                horari.eliminarTeoria(assig, grupos_teoria[i])


    
