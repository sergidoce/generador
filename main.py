
import urllib, requests
import json
from generador import Generador
#This URL is the page you actually want to pull down with requests.


def main():

    generador = Generador()
    generador.insertarAsignaturas()
    generador.ajustes_adicionales()
    generador.generar_horarios()
    

if __name__ == "__main__":
    main()







