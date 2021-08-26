# RafKac
# 2021_08_26
# na podstawie mojego kodu z 2018
import random


class Perceptron:
    """
    klasa realizująca Perceptron
    każdy perceptron inicjujemy jako "zgaszony" (czyli 0), 1 interpretujemy jako "zapalony"
    w konstruktorze generujemy losową tablicę wag
    """

    def __init__(self, n=0, theta=0.1, ERR=0, wynik=0, stalaU=0.1, czyPrzyklad=0):

        self.tablicaWag = []
        self.n = n
        self.theta = theta
        self.ERR = ERR
        self.wynikDzialaniaSieci = wynik
        self.stalaUczenia = stalaU
        self.czyPrzykladJestTaLiczba = czyPrzyklad

        for i in range(35):
            t = random.randint(0, 1)
            self.tablicaWag.append(t)

        print(self.tablicaWag)

    def wartosc_err(self, T_j):
        pomoc = 0
        if T_j == self.n:
            pomoc = 1
        else:
            pomoc = -1
        self.ERR = pomoc - self.wynikDzialaniaSieci

    def co_jest_na_wyjsciu(self, wektor):
        suma = -1 * self.theta
        for i in range(len(self.tablicaWag)):
            suma += self.tablicaWag[i] * wektor[i]
        if suma >= 0:
            self.wynikDzialaniaSieci = 1
        else:
            self.wynikDzialaniaSieci = -1
        return self.wynikDzialaniaSieci

    def aktualizacja_wag(self):
        for i in range(35):
            wpis = self.tablicaWag[i]
            wpis += self.stalaUczenia * self.ERR * self.czyPrzykladJestTaLiczba.
