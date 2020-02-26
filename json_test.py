import requests
import json
from dades import Dades
from horari import Horari

dades = Dades()
horari = Horari()

horari.print_horari()
res = dades.get_grupos_teoria("IC")

horari.ponerTeoria("IC", res[0])
