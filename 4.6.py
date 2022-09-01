import random

N = int(input('Anna pisteiden kokonaismäärä: '))
kerta = 1
n = 0

while kerta <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1
        kerta += 1
    else:
        kerta += 1

print(f'Piin likiarvo: {4*n/N}')