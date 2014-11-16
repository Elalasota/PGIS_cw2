
class liczba_zespolona:
    def get_rzeczywista(self):
        return self.__rzeczywsita
    def get_urojona(self):
        return self.__urojona
    def set_rzeczywista(self):
        return self.__rzeczywsita
    def set_urojona(self):
        return self.__urojona
    def __init__(self, rzeczywista, urojona):
        self.rzeczywista=rzeczywista
        self.urojona=urojona
    def dodaj(self, liczba_zespolona):
        suma=(self.rzeczywista+liczba_zespolona.rzeczywista,self.urojona+liczba_zespolona.urojona )
        print suma
        return suma
    def odejmij(self, liczba_zespolona):
        roznica=(self.rzeczywista-liczba_zespolona.rzeczywista,self.urojona-liczba_zespolona.urojona )
        print roznica
        return roznica
    def modul(self):
        modul=(self.rzeczywista**2+self.urojona**2)**(0.5)
        print modul
        return modul
    def __str__(self):
        return str(self.rzeczywista)+" + "+str(self.urojona)+"i"
    pass
liczba1=liczba_zespolona(5,4)
liczba2=liczba_zespolona(4,3)
liczba1.dodaj(liczba2)
liczba1.odejmij(liczba2)
liczba1.modul()
print liczba1