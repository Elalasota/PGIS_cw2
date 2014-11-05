#!/usr/bin/env python
#-*- coding: utf-8 -*-
plik=open("plik.txt", "r")
tresc=plik.read()
tresc=tresc.lower()
tresc=tresc.replace("\n", " ")
punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', '-', "'",]
for i in punctuation:
    tresc=tresc.replace(i, "")
slowa=tresc.split(" ")
print slowa
lista=[]
for slowo in slowa:
    lista.append((slowo, str(slowa.count(slowo))))
zbior=set(lista)
lista=list(zbior)
sortowane=sorted(lista, key=lambda wartosc:wartosc[1], reverse=True)
plik.close()
plik2=open("statystyki.txt", "w")
for linia in sortowane:
    plik2.writelines(str(linia[0])+" "+str(linia[1])+"\n")
plik2.close()