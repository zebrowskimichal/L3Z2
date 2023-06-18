"""
Wzorce Projektowe
1.Strategia:
Wzorzec Strategii pozwala na zdefiniowanie różnych algorytmów i umożliwia wymienne ich wykorzystanie. Wzorzec ten jest przydatny, gdy mamy wiele możliwych sposobów wykonania pewnego zadania i chcemy umożliwić elastyczne wybieranie jednego z nich w trakcie działania programu.
Przykład:
Prosta gra, w której mamy do wyboru 3 możliwości ataku. Wykorzystamy wzorzec Strategii, aby w łątwy sosób było można wybierać dany rodzaj ataku.
"""

class strategiaAtaku():
    def atak(self):
        pass

class atakOgniem(strategiaAtaku):
    def atak(self):
        print("Atak ogniem!")

class atakLodem(strategiaAtaku):
    def atak(self):
        print("Atak lodem!")

class atakPiorunem(strategiaAtaku):
    def atak(self):
        print("Atak piorunem!")

class Gracz:
    def __init__(self, imie, rodzajAtaku):
        self.imie = imie
        self.rodzajAtaku = rodzajAtaku

    def zmien_rodzajAtaku(self, rodzajAtaku):
        self.rodzajAtaku = rodzajAtaku

    def atak(self):
        print(f"{self.imie} wykonuje atak:")
        self.rodzajAtaku.atak()

# Użycie wzorca Strategii
gracz = Gracz("Gracz 1", atakOgniem())
gracz.atak()  
# Atak ogniem!

gracz.zmien_rodzajAtaku(atakLodem())
gracz.atak()  
# Atak lodem!

gracz.zmien_rodzajAtaku(atakPiorunem())
gracz.atak()  
# Atak piorunem!

print()

"""
2.Polecenie:
Wzorzec Polecenia pozwala zamienić żądanie w samodzielny obiekt. Wzorzec ten umożliwia parametryzację klientów (obiektów wydających polecenia) różnymi żądaniami, umożliwia kolejkowanie i rejestrowanie żądań oraz obsługę operacji odłożonych w czasie.
"""

# Przykladowa Implementacja

class polecenie:
       def wykonaj(self):
           raise NotImplementedError

class wstaw(polecenie):
    def __init__(self, edytor, tekst):
        self.edytor = edytor
        self.tekst = tekst
    def wykonaj(self):
        self.edytor.wstaw_tekst(self.tekst)

class usun(polecenie):
    def __init__(self, edytor):
        self.edytor = edytor
    def wykonaj(self):
        self.edytor.usun_tekst()

class edytor:
    def __init__(self):
        self.tekst = ""
    def wstaw_tekst(self, tekst):
        self.tekst += tekst
    def usun_tekst(self):
        self.tekst = ""


obiekt = edytor()
polecenia = []

polecenia.append(wstaw(obiekt, "Hello, "))
polecenia.append(wstaw(obiekt, "world! "))
polecenia.append(usun(obiekt))

for polecenie in polecenia:
    polecenie.wykonaj()
    print(obiekt.tekst)

print()

"""
3.Metoda Szablonowa:
Wzorzec Metody Szablonowej definiuje ogólny szkielet algorytmu,pozostawia, więc konkretne implementacje poszczególnych operacji do podklas. Pozwala to na modyfikowanie niektórych, poszczególnych kroków algorytmu,zachowując przy tym strukturę ogólną.
"""

# Przykladowa Implementacja

class napoj():
    def przygotuj(self):
        self.zagotujWode()
        self.parz()
        self.nalej()
        self.dodajSkladniki()

    def zagotujWode(self):
        print("Gotowanie wody")

    def parz(self):
        pass

    def nalej(self):
        print("Nalewanie do filiżanki")

    def dodajSkladniki(self):
        pass


class kawa(napoj):
    def parz(self):
        print("Parzenie kawy")

    def dodajSkladniki(self):
        print("Dodawanie mleka")


class herbata(napoj):
    def parz(self):
        print("Parzenie herbaty")

    def dodajSkladniki(self):
        print("Dodawanie cytryny")



napojKawa = kawa()
napojKawa.przygotuj()
"""
Gotowanie wody
Parzenie kawy
Nalewanie do filiżanki
Dodawanie mleka
"""

print()

napojHerbata = herbata()
napojHerbata.przygotuj()
"""
Gotowanie wody
Parzenie herbaty
Nalewanie do filiżanki
Dodawanie cytryny
"""
"""
Podobieństwa i różnice między wzorcami:

-Wszystkie trzy wzorce projektowe dają możliwosć elastycznego dostosowania zachowań oraz separacji kodu(różnych funkcji)
-Wzorce te pozwalają stworzyć ogólny szkielet algorytmów
-Metoda szablonowa bazuje na mechanizmie dziedziczenia (pozwala zmienić część algorytmu w podklasach), a metoda strategii bazuje na kompozycji- możliwa jest zmiana części zachowania obiektu poprzez nadanie mu różnych strategii, nawet w trakcie działania programu- w przeciwieństwie do metody szablonowej

"""