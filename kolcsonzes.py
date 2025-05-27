INGATLANOK_FILE = 'ingatlanok.txt'
KOLCSONZOTTEK_FILE = 'kolcsonzottek.txt'
MEZOK = ["ID", "Cím", "Típus", "Alapterület", "Ár/hó", "Állapot", "Erkély", "Elérhető"]

def betolt_ingatlanok():
    try:
        with open(INGATLANOK_FILE, 'r', encoding='utf-8') as f:
            sorok = f.readlines()
        ingatlanok = []
        for sor in sorok:
            adat = sor.strip().split('|')
            if len(adat) == len(MEZOK):
                ingatlan = dict(zip(MEZOK, adat))
                ingatlanok.append(ingatlan)
        return ingatlanok
    except FileNotFoundError:
        return []

def mentes_ingatlanok(ingatlanok):
    with open(INGATLANOK_FILE, 'w', encoding='utf-8') as f:
        for ingatlan in ingatlanok:
            sor = '|'.join([ingatlan[m] for m in MEZOK])
            f.write(sor + '\n')

def keres_ingatlan(helyszin=None, tipus=None, max_ar=None):
    ingatlanok = betolt_ingatlanok()
    eredmenyek = []
    for ingatlan in ingatlanok:
        if ingatlan['Elérhető'] != 'igen':
            continue
        if helyszin and helyszin.lower() not in ingatlan['Cím'].lower():
            continue
        if tipus and tipus.lower() != ingatlan['Típus'].lower():
            continue
        if max_ar:
            try:
                if int(ingatlan['Ár/hó']) > int(max_ar):
                    continue
            except ValueError:
                continue
        eredmenyek.append(ingatlan)
    return eredmenyek

def kolcsonzes(ingatlan_id, kolcsonzo_nev):
    ingatlanok = betolt_ingatlanok()
    uj_lista = []
    kolcsonzott = None

    for ingatlan in ingatlanok:
        if ingatlan['ID'] == str(ingatlan_id) and ingatlan['Elérhető'] == 'igen':
            kolcsonzott = ingatlan
        else:
            uj_lista.append(ingatlan)

    if not kolcsonzott:
        print(" Nincs ilyen elérhető ingatlan.")
        return
    sor = '|'.join([kolcsonzott[m] for m in MEZOK]) + f"|{kolcsonzo_nev}"
    with open(KOLCSONZOTTEK_FILE, 'a', encoding='utf-8') as f:
        f.write(sor + '\n')
    mentes_ingatlanok(uj_lista)
    print(f" Kikölcsönözve: {kolcsonzott['Cím']} -> {kolcsonzo_nev}")
