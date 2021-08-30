# RafKac
# 2021_08_26
# na podstawie mojego kodu z 2018
import random


class Perceptron:
    """
    klasa realizująca Perceptron
    każdy perceptron inicjujemy jako "zgaszony" (czyli 0), 1 interpretujemy jako "zapalony"
    w konstruktorze generujemy losową tablicę wag
    czyPrzykladJestTaLiczba = 1 - jest, -1 - nie jest (albo 0)
    """

    def __init__(self, n=0, theta=0.1, ERR=0.0, wynik=0.0, stalaU=0.1, czyPrzyklad=0.0):

        self.tablicaWag = []
        self.n = n
        self.theta = theta
        self.ERR = ERR
        self.wynikDzialaniaSieci = wynik
        self.stalaUczenia = stalaU
        self.czyPrzykladJestTaLiczba = czyPrzyklad

        for i in range(35):
            t = random.random()
            self.tablicaWag.append(t)

        print(self.tablicaWag)

    def wartosc_err(self, T_j):
        pomoc = 0.0
        if T_j == self.n:
            pomoc = 1.0
        else:
            pomoc = -1.0
        self.ERR = pomoc - self.wynikDzialaniaSieci
        if self.ERR != 0:
            print("nowa wartość ERR: {}, czyPrzyklad: {}, stalauczenia: {}".format(self.ERR, self.czyPrzykladJestTaLiczba,self.stalaUczenia))

    def co_jest_na_wyjsciu(self, wektor):
        """
        :param wektor: czyli tablica liczb całkowitych
        :return: wynikDzialaniaSieci (binarnie, tzn nie dopuszczamy wartości pośrednich)
        służy tylko do ustawienia wartości wynikDziałaniaSieci dla danego perceptrona
        """
        suma = -1.0 * self.theta
        for i in range(len(self.tablicaWag)):
            suma += (self.tablicaWag[i]) * wektor[i]
        if suma >= 0:
            self.wynikDzialaniaSieci = 1.0
        else:
            self.wynikDzialaniaSieci = -1.0
        return self.wynikDzialaniaSieci

    def aktualizacja_wag(self):
        print("wagi przed aktualizacją: ")
        print(self.tablicaWag)
#        print("aktualizacja wag dla perceptrona {}".format(self.n))
        for i in range(35):
#            print(self.stalaUczenia * self.ERR * self.czyPrzykladJestTaLiczba)
            self.tablicaWag[i] += self.stalaUczenia * self.ERR * self.czyPrzykladJestTaLiczba
            self.theta -= float(self.ERR) * float(self.stalaUczenia)
#        for zaw in self.tablicaWag:
#            zaw += self.stalaUczenia * self.ERR * self.czyPrzykladJestTaLiczba
#            self.theta -= float(self.ERR) * float(self.stalaUczenia)
        print("wagi po aktualizacji: ")
        print(self.tablicaWag)