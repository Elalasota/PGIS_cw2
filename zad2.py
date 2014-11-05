plik=open("plik.txt", "r")
tresc=plik.read()
Menu={"Rosol":3.50, "Placki":6.80, "Schabowy":12.20, "Pomidorowa":3.50, "Pizza":19.20, "Surowka":3.50}
plik.close()
def platnosc(zamowienie):
    wartosc=0
    for pozycja in zamowienie:
        if pozycja in Menu.keys():
            wartosc=wartosc+Menu[pozycja]
    napiwek=wartosc*0.1
    print napiwek+wartosc
    return napiwek+wartosc

dania=["Rosol", "Pomidorowa", "Pizza", "Surowka"]
platnosc(dania)