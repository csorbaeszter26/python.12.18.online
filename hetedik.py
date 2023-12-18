import renszarvas

def beolvas():
    lista = []
    beFajl = open("fajlok/mikulaszan.txt", "r", encoding = "utf-8")
    adatokListaja = beFajl.readlines()
    # print(adatokListaja)
    for index in range(1, len(adatokListaja), 1):
        if not ("Santa Claus" in adatokListaja[index]):
            daraboltSor = adatokListaja[index].split("@")
            # print(daraboltSor)
            szarvas = renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            # print(szarvas)
            lista.append(szarvas)
            # print(lista)

    beFajl.close()
    return lista

def angolMegfelelo(nev, lista):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        if lista[index].nevMagyar == nev:
            # print(szarvas.nevAngol)
            # print(szarvas.nevAngol)
            talalat = False
        index += 1

    if not (talalat):
        print(f"A szarvas angol neve: {lista[index - 1].nevAngol}.")
    else:
        print("Nincsen ilyen rénszarvas")

def mikulasSzam(lista:list):
    db = 0
    index = 0
    while index < len(lista):
        daraboltLeiras = lista[index].leiras.split(" ")
        print(daraboltLeiras)
        index2 = 0
        while index2 < len(daraboltLeiras):
            if daraboltLeiras[index2] == "Mikulás":
                db += 1
            index2 += 1
        index += 1
    print(f"A Mikulás szó előfordulásának száma: {db}.")

def atlagMagassag(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].magassag
        index += 1
    if len(lista) == 0:
        print("A szarvasok átlagmagassága: 0.")
    else:
        atlag = osszeg/len(lista)
        print(f"A szarvasok átlag magassága: {atlag}.")

def parosHelyenRepulokNevvel(lista):
    print("A páros helyen repülő rénszarvasok nevei: ", end="")
    index = 0
    while index < len(lista):
        if lista[index].hely%2==0:
            print(lista[index].nevMagyar + ", ", end="")
        index += 1
    print("")

def leghosszabbLeiras(lista):
    maxErtek = len(lista[0].leiras)
    maxIndex = 0
    index = 1
    while index < len(lista):
        if len(lista[index].leiras) > maxErtek:
            maxErtek = len(lista[index].leiras)
            maxIndex = index
        index += 1
    print(f"A leghosszabb laírása {lista[index].nev} van (hossza: {maxErtek} karakter.")


def hetes():
    # a feladat
    szarvasokListaja = beolvas()
    # b feladat
    for szarvas in szarvasokListaja:
        print(szarvas.kiir())
    # c feladat
        print(f"A rénszarvasok száma: {len(szarvasokListaja)}.")
    # d feladat
    angolMegfelelo("Pompás", szarvasokListaja)
    # e
    mikulasSzam(szarvasokListaja)
    # f
    atlagMagassag(szarvasokListaja)
    # g
    parosHelyenRepulokNevvel(szarvasokListaja)
    # h
    leghosszabbLeiras(szarvasokListaja)



    """
    index = 0
    talalat = True
    while index < len(szarvasokListaja) and talalat:
        if szarvasokListaja[index].nevMagyar == "Pompás":
            # print(szarvas.nevAngol)
            # print(szarvas.nevAngol)
            talalat = False
        index += 1

    if not(talalat):
        print(f"A szarvas angol neve: {szarvasokListaja[index-1].nevAngol}.")
    else:
        print("Nincsen ilyen rénszarvas")

    
    for szarvas in szarvasokListaja:
        if szarvas.nevMagyar == "Pompás":
            print(szarvas.nevAngol)
"""

