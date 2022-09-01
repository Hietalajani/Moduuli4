while True:
    try:
        tuumat = float(input('Anna tuumat: '))
    except ValueError:
        print('Laita ny joku oikee numero hei')
        continue
    if tuumat >= 0:
        cm = tuumat * 2.54
        print(cm)
    else:
        print('Lol XD')
        break
