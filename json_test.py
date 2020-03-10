import requests
import json
from dades import Dades
from horari import Horari

dades = Dades()

assignatures = dades.get_assignatures()
print(len(assignatures))
for i in range(0, len(assignatures)):
    print(assignatures[i])