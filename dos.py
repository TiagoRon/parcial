from pila import Stack
from dino import dinosaurios

especies = set()
for dino in dinosaurios:
    especies.add(dino['especie'])
print(f"Hay {len(especies)} especies diferentes")

descubridores = set()
for dino in dinosaurios:
    descubridores.add(dino['descubridor'])
print(f"Hay {len(descubridores)} descubridores diferentes")

print("Dinosaurios que empiezan con T:")
for dino in dinosaurios:
    if dino['nombre'].startswith('T'):
        print(dino['nombre'])

print("Dinosaurios que pesan menos de 275 kg:")
for dino in dinosaurios:
    peso = int(dino['peso'].split()[0])
    if peso < 275:
        print(dino['nombre'])

pila = Stack()
for dino in dinosaurios:
    if dino['nombre'][0] in ['A', 'Q', 'S']:
        pila.push(dino)
print(f"Se han apilado {pila.size()} dinosaurios que comienzan con A, Q, S")
