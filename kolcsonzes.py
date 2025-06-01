def beolvas_fajl():
    ingatlanok = []
    with open("ingatlanok.txt", "r", encoding="utf-8") as f:
        f.readline() 
        for sor in f:
            adat = [x.strip() for x in sor.strip().split(";")]
            ingatlan = {
                "szám": adat[0],
                "Cím": adat[1],
                "Típus": adat[2],
                "Alapterület": int(adat[3]),
                "Ár": int(adat[4]),
                "Állapot": adat[5],
                "Erkély": adat[6],
                "Elérhető": adat[7]
            }
            ingatlanok.append(ingatlan)
    return ingatlanok


def kiir_ingatlan(ingatlan):
    print(f"\nKiválasztott ingatlan:")
    for kulcs, ertek in ingatlan.items():
        print(f"{kulcs}: {ertek}")


def kereses_szam_alapjan(ingatlanok):
    szam = input("Add meg az ingatlan számát (1-6): ")
    for i in ingatlanok:
        if i["szám"] == szam:
            kiir_ingatlan(i)
            return
    print("Nincs ilyen számú ingatlan!")


def kereses_tulajdonsag_alapjan(ingatlanok):
    print("Keresés tulajdonság alapján:")
    print("1 - Minimum alapterület")
    print("2 - Maximum ár")
    print("3 - Típus (lakás/családi ház)")
    valasztas = input("Választás (1/2/3): ")

    if valasztas == "1":
        min_ter = int(input("Minimum alapterület (m²): "))
        szurt = [i for i in ingatlanok if i["Alapterület"] >= min_ter]

    elif valasztas == "2":
        max_ar = int(input("Maximum ár (Ft): "))
        szurt = [i for i in ingatlanok if i["Ár"] <= max_ar]

    elif valasztas == "3":
        tipus = input("Típus (lakás/családi ház): ").lower()
        szurt = [i for i in ingatlanok if i["Típus"].lower() == tipus]

    else:
        print("Érvénytelen választás.")
        return

    if not szurt:
        print("Nincs találat.")
        return

    print("\nTalált ingatlanok:")
    for index, i in enumerate(szurt, 1):
        print(f"{index}. {i['Cím']} - {i['Típus']}, {i['Alapterület']} m², {i['Ár']} Ft")

    valasztott = int(input("Válassz egyet a sorszám alapján: "))
    if 1 <= valasztott <= len(szurt):
        kiir_ingatlan(szurt[valasztott - 1])
    else:
        print("Érvénytelen sorszám.")


def main():
    ingatlanok = beolvas_fajl()
    print("Ingatlan kereső")
    print("1 - Keresés szám alapján")
    print("2 - Keresés tulajdonság alapján")
    valasztas = input("Válassz, my nigga: ")

    if valasztas == "1":
        kereses_szam_alapjan(ingatlanok)
    elif valasztas == "2":
        kereses_tulajdonsag_alapjan(ingatlanok)
    else:
        print("vro nincs ilyen opció :broken_heart_emoji:.")


main()

