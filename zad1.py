#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs, tkFileDialog, Tkinter
root = Tkinter.Tk()
root.withdraw()
podaj_plik=tkFileDialog.askopenfilename()
plik=codecs.open(podaj_plik, "r", "utf-8")
tresc=plik.read()
tresc=tresc.lower()

tresc=tresc.replace("\n", " ")
punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', '-', "'",]
for i in punctuation:
    tresc=tresc.replace(i, "")

slowa=tresc.split(" ")

lista=[]
for slowo in slowa:
    lista.append((slowo, str(slowa.count(slowo))))
    
zbior=set(lista)
zbior.discard(" ")
lista=list(zbior)
sortowane=sorted(lista, key=lambda wartosc:wartosc[1], reverse=True)

    
plik2=codecs.open("statystyki.txt", "w", "utf-8")
plik2.writelines(("Statystyki uzyskane na podstawie podanego pliku:"+"\r\n").decode("utf-8"))
for linia in sortowane:
    linijka="Słowo ".decode("utf-8")+linia[0]+" wystąpiło: ".decode("utf-8")+str(linia[1])+" raz/y. "+'\r\n'
    plik2.writelines(linijka)
plik2.close()

plik.close()

