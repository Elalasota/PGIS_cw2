plik=open("menu.txt", "r")
lista=[]
tresc=plik.read()
tresc=tresc.replace("\n", " ")
lista=tresc.split(" ")
klucze1=[]
wartosci1=[]
for i in xrange(0, len(lista), 2):
    klucze1.append(lista[i])
    wartosci1.append(float(lista[i+1]))
Menu=dict(zip(klucze1, wartosci1))
plik.close()

def platnosc(zamowienie):
    wartosc=0
    for pozycja in zamowienie:
        if pozycja in Menu.keys():
            wartosc=wartosc+Menu[pozycja]
    napiwek=round(wartosc*0.1, 2)
    print napiwek+wartosc
    return napiwek+wartosc

dania=["Rosol", "Surowka", "Schabowy", "Ogorek"]
platnosc(dania)