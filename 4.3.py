lista = []

while True:
    luku = input('Anna luku: ')

    if luku == "":
        lista.sort()
        print(f'Listan pienin luku on {lista[0]} ja suurin {lista[-1]}')
        break

    else:
        try:
            luku = float(luku)
        except ValueError:
            print('Ei luku')
            continue
        lista.append(luku)