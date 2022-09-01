tunnus = "python"
salasana = "rules"

while True:
    tun = input('Anna käyttäjätunnus: ')
    sal = input('Anna salasana: ')

    if tun == tunnus and sal == salasana:
        print('Tervetuloa.')
    else:
        print('Pääsy evätty.')