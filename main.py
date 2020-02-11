
import urllib, requests
import json
from bs4 import BeautifulSoup
from generador import Generador
#This URL is the page you actually want to pull down with requests.
request_url = 'https://api.fib.upc.edu/v2/assignatures/places/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781'










def main():

    generador = Generador()
    generador.insertarAsignaturas()




if __name__ == "__main__":
    main()







