import requests
import json

r = requests.get('https://api.fib.upc.edu/v2/assignatures/places/?format=json&client_id=bhKgd1HVmIPOjVZOBJZomwj8I1q7W2Hq8y2Fj781')
print(type(r.text))

data = json.loads(r.text)

resultados = data['results']

asignaturas = []

for i in range(0, len(resultados) - 1):
    if resultados[i]['assig'] == "A":
        asignaturas.append(resultados[i])

print(asignaturas)
