#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Urzadzenie(object):
    def __init__(self):
        self.gotowosc=False
    def wlacz(self):
        if (self.gotowosc==True):
            print "Jestem gotowy do pracy! Nie baw się mną!"
        else:
            print "Witaj, w czym mogę pomóc?"
        self.gotowosc=True
    def wylacz(self):
        if (self.gotowosc==True):
            print "Do zobaczenia później!"
        else:
            pass
        self.gotowosc=False
        
komputer=Urzadzenie()
komputer.wlacz()    
komputer.wylacz()

   
class Telefon(Urzadzenie):
    def __init__(self, numer):
        self.numer=numer
        super(Telefon, self).__init__()
    def __str__(self):
        return "Mój numer to: "+self.numer
    def set_numer(self, numer):
        self.__numer=numer
    def get_numer(self):
        return self.__numer
    def set_marka(self, marka):
        self.__marka=marka
    def get_marka(self):
        return self.__marka
    def zadzwon(self, numer):
        print "Dzwonię pod numer: "+numer
    def odbierz(self, numer):
        print "Odbieram połączenie od numeru: "+numer
#===============================================================================
# ja=Telefon("609543191")
# ty=Telefon("543098564")
# ja.marka="Nokia"
# print ja.marka
# moj=ja.numer
# print moj
# ja.wlacz()
#===============================================================================

class Radio(Urzadzenie):
    def __init__(self):
        self.glosnosc=0
        super(Radio, self).__init__()
        self.kanal="Rmf"
    def set_kanal(self, kanal):
        self.__kanal=kanal
    def get_kanal(self):
        return self.__kanal
    def zmien_kanal(self, nazwa_kanalu):
        print "Zmieniłem kanał na: "+nazwa_kanalu
    def glosniej(self, wartosc):
        self.glosnosc=self.glosnosc+wartosc
        return self.glosnosc
    def scisz(self, wartosc):
        self.glosnosc=self.glosnosc-wartosc
        return self.glosnosc
    def get_glosnosc(self):
        return self.__glosnosc
    def set_glosnosc(self, glosnosc):
        self.__glosnosc=glosnosc
        
budzik=Radio()
budzik.glosnosc=10
glos=budzik.glosnosc
print budzik.glosniej(5)
cos=budzik.kanal


class Odtwarzacz_muzyki(Urzadzenie):
    def __init__(self, biblioteka):
        self.numer_piosenki=0
        self.biblioteka=biblioteka
        self.piosenka=biblioteka[0]
        super(Odtwarzacz_muzyki, self).__init__()
    def stop(self):
        print "Zatrzymano odtwarzanie"
    def play(self):
        print "Gram dalej"
    def poprzedni(self):
        if (self.numer_piosenki==0):
            print "Nie ma poprzedniej piosenki"
        else:
            self.numer_piosenki=self.numer_piosenki-1
            self.piosenka=self.biblioteka[self.numer_piosenki]
    def nastepny(self):
        if (self.numer_piosenki==len(self.biblioteka)):
            print "Nie ma następnej piosenki"
        else:
            self.numer_piosenki=self.numer_piosenki+1
            self.piosenka=self.biblioteka[self.numer_piosenki] 
        return self.piosenka 
    def get_piosenka(self):
        return self.__piosenka
    def dodaj(self, piosenka):
        self.biblioteka.append(piosenka)
        return self.biblioteka
    def usun(self, piosenka):
        self.biblioteka.remove(piosenka)
        return self.biblioteka
    def get_biblioteka(self):
        return self.__biblioteka
    def __str__(self):
        return self.piosenka
    def odtwarzaj(self, piosenka):
        if (piosenka in self.biblioteka):
            self.piosenka=piosenka
            self.numer_piosenki=self.biblioteka.index(piosenka)
            print "Odtwarzam: "+piosenka
        else:
            print "Nie ma określonej piosenki w bibliotece"
        return self.piosenka
    def get_numer_piosenki(self):
        return self.__numer_piosenki
    def dodaj_biblioteke(self, biblioteka):
        self.biblioteka=self.biblioteka+biblioteka
        return self.biblioteka
#===============================================================================
# biblioteka=["Korn - Thoughtless", "Seether - Remedy", "Metallica - Enter Sandman", "Iron Maiden - Fear of the Dark", "In Flames - Crawl Through Knives"]
# supcio=Odtwarzacz_muzyki(biblioteka)
# print supcio
# supcio.dodaj("Five Finger Death Punch - Dying Breed")
# print supcio.nastepny()
# supcio.odtwarzaj("Five Finger Death Punch - Dying Breed")
#===============================================================================
class Kalkulator(Urzadzenie):
    pass
class Smartfon(Telefon, Radio, Odtwarzacz_muzyki):
    def __init__(self, numer):
        self.gotowosc=False
        self.numer_piosenki=0
        self.biblioteka=["Wgraj muzykę"]
        self.piosenka=self.biblioteka[0]
        self.numer=numer
    def wczytaj_biblioteke(self, bibl):
        self.biblioteka=bibl
        self.piosenka=self.biblioteka[0]

lumia=Smartfon("6533")
bib=["trololo", "lalala"]
lumia.wczytaj_biblioteke(bib)
print lumia.biblioteka
lumia.dodaj("Linkin Park - Numb")
print lumia.piosenka
lumia.zadzwon("76032042")
lumia.wlacz()
lumia.set_kanal("Radio Zet")