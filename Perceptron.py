# RafKac
# 2021_08_26
# na podstawie mojego kodu z 2018
import random
import Przyklady


class Perceptron:
    """
    klasa realizująca Perceptron
    każdy perceptron inicjujemy jako "zgaszony" (czyli 0), 1 interpretujemy jako "zapalony"
    w konstruktorze generujemy losową tablicę wag
    czyPrzykladJestTaLiczba = 1 - jest, -1 - nie jest
    n - cyfra rozpoznawana przez perceptron [0-9]
    wynikDzialaniaSieci {-1,1}
    """

    def __init__(self, n=0, theta=0.01, ERR=0.0, wynik=0.0, stalaU=0.005, czyPrzyklad=-1.0):

        self.tablicaWag = []
        self.n = n
        self.theta = theta
        self.ERR = ERR
        self.wynikDzialaniaSieci = wynik
        self.stalaUczenia = stalaU
        self.czyPrzykladJestTaLiczba = czyPrzyklad

        for i in range(35):
            t = 2.0 * random.random() - 1
            self.tablicaWag.append(t)

        print(self.tablicaWag)

    def wartosc_err(self, T_j):
        """
        :param T_j: to poprawna odpowiedź na rozpatrywany przykład
        :return: ustawia wartość ERR
        """
        pomoc = 0.0
        if T_j == self.n:
            pomoc = 1.0
        else:
            pomoc = -1.0
        self.ERR = pomoc - self.wynikDzialaniaSieci

    def co_jest_na_wyjsciu(self, wektor):
        """
        :param wektor: czyli tablica liczb całkowitych
        :return: wynikDzialaniaSieci (binarnie, tzn nie dopuszczamy wartości pośrednich)
        służy tylko do ustawienia wartości wynikDziałaniaSieci dla danego perceptrona
        """
        suma = -1.0 * self.theta
        for i in range(len(self.tablicaWag)):
            suma += (self.tablicaWag[i]) * wektor[i]
        if suma >= 0.0:
            self.wynikDzialaniaSieci = 1.0
        else:
            self.wynikDzialaniaSieci = -1.0
        return self.wynikDzialaniaSieci

    def aktualizacja_wag(self, przyklad):
        for i in range(35):
            self.tablicaWag[i] += self.stalaUczenia * self.ERR * przyklad.lista[i]
            self.theta = self.theta - self.ERR * self.stalaUczenia

    def wszystkie_akcje(self, przyklad):
        """
        metoda dostaje jako paramter obiekt klasy Przyklad()
        wykonuje wszystkie operacje perceptrona dla danego przykładu, ustawiając odpowiednio wartości
        """
        suma = -1.0 * self.theta
        czyToTaCyfra = 0.0
        cyfraJakaJestPrzyklad = przyklad.cyfra
        for i in range(len(self.tablicaWag)):
            suma += float(self.tablicaWag[i]) * float(przyklad.lista[i])
        if suma >= 0.0:
            self.wynikDzialaniaSieci = 1.0
        else:
            self.wynikDzialaniaSieci = -1.0
        if cyfraJakaJestPrzyklad == self.n:
            czyToTaCyfra = 1.0
        else:
            czyToTaCyfra = -1.0
        self.czyPrzykladJestTaLiczba = czyToTaCyfra
        self.ERR = czyToTaCyfra - self.wynikDzialaniaSieci

    def licz_klasyfikowane_przyklady(self, listaPrzykladow):
        wynik = 0
        for p in listaPrzykladow:
            self.wszystkie_akcje(p)
            if self.ERR == 0:
                wynik += 1
        return wynik
