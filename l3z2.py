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
klasa strategiaAtaku jest abstrakcyjną klasą, która definiuje ogólny interfejs dla różnych strategii ataku.  Konkretne strategie (klasy atakOgniem, atakLodem, atakPiorunem): Są to konkretne implementacje strategii ataku. Każda strategia reprezentuje inny rodzaj ataku (ogniem, lodem, piorunem), więc każda strategia jest inna. Klasa Gracz reprezentuje obiekt, który korzysta z różnych strategii ataku. Posiada pole rodzajAtaku, które przechowuje obiekt strategii. Metoda atak w tej klasie wywołuje metodę atak na obiekcie strategii, realizując odpowiedni atak.
"""
#####################################################################################################################################################
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
Klasa polecenie jest abstrakcyjną klasą, która definiuje ogólny nterfejs dla różnych poleceń. W tym przypadku zawiera jedną metodę wykonaj, która będzie implementowana przez konkretne polecenia.
Konkretne polecenia (klasy wstaw i usun): Są to konkretne implementacje poleceń. Każda z tych klas dziedziczy po klasie polecenie i implementuje metodę wykonaj na różne sposoby.
Klasa edytor reprezentuje obiekt, na którym wykonywane są operacje. W tym przypadku, klasa edytor przechowuje tekst i udostępnia metody wstaw_tekst i usun_tekst do manipulacji tekstem.
"""
#####################################################################################################################################################
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

print()

napojHerbata = herbata()
napojHerbata.przygotuj()


"""
Klasa napoj jest klasą abstrakcyjną, która definiuje szablonową metodę przygotuj(). Ta metoda określa ogólny algorytm przygotowywania napoju, składający się z kroków: zagotowanie wody, parzenie, nalewanie do filiżanki i dodawanie składników. Niektóre z tych kroków są zdefiniowane jako puste metody, które zostaną zaimplementowane w klasach dziedziczących.
Klasy pochodne kawa i herbata: Są to konkretne implementacje napojów. Dziedziczą one po klasie bazowej napoj i dostarczają implementacje konkretnych kroków takich jak parz() i dodajSkladniki(). Każda z tych klas dostosowuje algorytm ogólny do swoich potrzeb.
Metoda przygotuj(): Jest to szablonowa metoda, która definiuje ogólny algorytm przygotowania napoju. Wywołuje ona odpowiednie kroki w odpowiedniej kolejności, korzystając z metod zdefiniowanych w klasach pochodnych. Ta metoda jest wspólna dla wszystkich napojów, ale konkretne implementacje poszczególnych kroków mogą się różnić w zależności od napoju.
"""
#####################################################################################################################################################
"""
Podobieństwa i różnice między wzorcami:

-Wszystkie trzy wzorce projektowe dają możliwosć elastycznego dostosowania zachowań oraz separacji kodu(tj. różnych funkcji)
-Wzorce te pozwalają stworzyć ogólny szkielet algorytmów
-Metoda szablonowa bazuje na mechanizmie dziedziczenia (pozwala zmienić część algorytmu w podklasach), a metoda strategii bazuje na kompozycji- możliwa jest zmiana części zachowania obiektu poprzez nadanie mu różnych strategii, nawet w trakcie działania programu- w przeciwieństwie do metody szablonowej. Natomiast metoda polecenia polega na umieszczeniu różnych poleceń, zadań w różne obiekty.
-Metoda strategii tak samo jak metoda polecenia umożliwia zmianę algorytmu w czasie jego wykonywania, bez zmiany struktury

-Podsumowująć wszystkie te metody dają możliwość elastycznego dostosowywania zachowań programu zależnie od potrzeby, ale realizują to założnie na różne sposoby, choć można znaleźć pomiędzy nimi pewne podobieństwa.

"""