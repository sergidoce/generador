import requests
import json
from dades import Dades
from horari import Horari

dades = Dades()
grupos = dades.get_grupos_lab("IC", "10")
print(grupos)