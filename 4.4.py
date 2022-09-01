import random
correct = random.randint(1, 10)

while True:
    try:
        arvaus = int(input('Arvaa kokonaisluku: '))
    except ValueError:
        print('LOOOOOOOOL')
        continue
    if arvaus == correct:
        print('Oikein.')
        break
    elif arvaus > 10:
        print('Hei tää on sit 1-10 välillä urpo')
    elif arvaus > correct:
        print('Liian suuri arvaus.')
    else:
        print('Liian pieni arvaus.')