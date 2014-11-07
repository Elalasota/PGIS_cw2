#!/usr/bin/env python
#-*- coding: utf-8 -*-

import codecs
plik=codecs.open("menu.txt", "r", "utf-8")
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
        if pozycja.decode("utf-8") in Menu.keys():
            wartosc=wartosc+Menu[pozycja.decode("utf-8")]

    napiwek=round(wartosc*0.1, 2)
    print napiwek+wartosc
    return napiwek+wartosc

dania=["Rosół", "Surówka", "Placki", "Pizza", "Pomidorowa", "Schabowy", "Kompot"]
platnosc(dania)