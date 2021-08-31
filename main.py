# -*- coding: utf-8 -*-
# RafKac
# 2021_08_19-27
#
# program realizujący Perceptron do rozpoznawania liczb, na podstawie mojego kodu z C++
# najpierw tworzymy GUI
# później perceptrona
# "liczby" do rozpoznawania są zapisywane 0/1, gdzie 1 <=> czarny, 0 <=> biały
# w trybie nauki nie możemy klikać superpiskeli, tylko "stop" i "koniec" są aktywne

import pygame
import random
import Perceptron
import SuperPixel
import Przyklady
import Wynik
import Przycisk


pygame.init()
resolution = (400, 300)
window = pygame.display.set_mode(resolution)
run = True
trybNauki = False
listaSuperpixeli = []
listaPerceptronow =[]
wynik = Wynik.Wynik(200, 50, 50, 50)
przyklady = Przyklady.Przyklady()
przykladyTestowe = Przyklady.Przyklady()

ilosc_powtorzen_nauki = 10000


def wczytaj_przyklad():
    if trybNauki:
        return
    p = Przyklady.Przyklad()
    for sp in listaSuperpixeli:
        if sp.kolor == (0, 0, 0):
            p.lista.append(1)
        else:
            p.lista.append(0)
    return p


def start():
    """
    metoda ma za zadanie sprawdzić wyklikany na superpikselach obrazek - czyli jaką cyfrę tam widzi?
    ustawia odpowiednią wartość wyniku
    """
    global wynik
    w = ""
    print("start()")
    przyklad = wczytaj_przyklad()
    for per in listaPerceptronow:
        if per.co_jest_na_wyjsciu(przyklad.lista) > 0.0:
            print("na wyjściu mamy: {}".format(per.co_jest_na_wyjsciu(przyklad.lista)))
            print("przykład to: {}".format(przyklad.cyfra))
            w += str(per.n)
    if w == "":
        w = "?"
    wynik.set_wynik(w)


def stop():
    """
    zatrzymuje naukę w danym momencie, zmienia wyświetlany wynik na "-"
    czyści listę superpikseli (żeby wyświetlało cały biały "ekran")
    """
    global trybNauki, wynik, listaSuperpixeli
    print("stop()")
    trybNauki = False
    wynik.set_wynik("-")
    for sp in listaSuperpixeli:
        sp.kolor = (255, 255, 255)


def nauka():
    """
    metoda odpowiada za nauczenie perceptronów,
    jeśli sieć jeszcze nie istenieje, to ją tworzy,
    następnie w pętli po perceptronach uczy każdy z nich zgodnie ze wzorem
    """
    global trybNauki, listaPerceptronow
#    print("nauka()")
    trybNauki = True
    l = 0
    licznik = 0
    iloscNierozpoznanych = 0
    czyJeszczeSprawdzamy = True
    zakres = len(przykladyTestowe.listaPrzykladow) - 1
    numerPrzykladu = random.randint(0, zakres)
    if len(listaPerceptronow) == 0:
        print("pusta lista perceptronów")
        for i in range(10):
            per = Perceptron.Perceptron(i)
            listaPerceptronow.append(per)
#            print("dodajemy {} perceptron, czyli numer {}".format(per.n, i))
    print("\nLista perceptronów ma {} elementów\n".format(len(listaPerceptronow)))
    for p in listaPerceptronow:
        print("uczymy {} perceptron, ma on numer {}".format(l, p.n))
        print("Początkowa tablica wag: ")
        print(p.tablicaWag)
        l += 1
        while czyJeszczeSprawdzamy:
            rozpatrywany = przykladyTestowe.listaPrzykladow[numerPrzykladu]
            coNaWyjsciu = p.co_jest_na_wyjsciu(rozpatrywany.lista)
            if rozpatrywany.cyfra == p.n:
                p.czyPrzykladJestTaLiczba = 1
            else:
                p.czyPrzykladJestTaLiczba = -1
            p.wartosc_err(rozpatrywany.cyfra)
            if p.ERR == 0:
                licznik += 1
                numerPrzykladu = random.randint(0, zakres)
            else:
                if rozpatrywany.cyfra == p.n:
                    iloscNierozpoznanych += 1
                p.aktualizacja_wag()
                licznik += 1
                numerPrzykladu = random.randint(0, zakres)
            if licznik % 1000 == 0:
                blad = funkcja_bledow(p)
                print("Nie rozpoznano: {} cyfr: {}".format(blad, p.n))
            if licznik == ilosc_powtorzen_nauki:
                print("koniec uczenia {} perceptrona".format(p.n))
                czyJeszczeSprawdzamy = False
        licznik = 0
        czyJeszczeSprawdzamy = True
        print("Końcowa tablica wag: ")
        print(p.tablicaWag)
    trybNauki = False


def koniec():
    global run
    run = False


def funkcja_bledow(per):
    """
    :param per z klasy Perceptron
    :return: wartość funkcji błędów
    jest wykorzystywana tylko podczas uczenia sieci, dlatego korzystamy z przykładów testowych
    """
    licznik = 0
    for p in przykladyTestowe.listaPrzykladow:
        print(p.cyfra)
        print(p.lista)
        print(per.tablicaWag)
        per.co_jest_na_wyjsciu(p.lista)
        per.wartosc_err(p.cyfra)
        if per.ERR != 0:
            licznik += 1
    return licznik


def rysuj(przyklad):
    """
    :param przyklad:
    metoda pilnuje wydruku cyfry na superpikselach,
    ingeruje w zastany stan listySuperpikseli, zmieniając kolory na odpowiednie
    ustawia także wyświetlany wynik
    """
    global listaSuperpixeli, wynik
    print(przyklad.lista)
    licznik = 0
    if not trybNauki:
        for i in przyklad.lista:
            if i == 1:
                listaSuperpixeli[licznik].zmianaKoloru((0, 0, 0))
            else:
                listaSuperpixeli[licznik].zmianaKoloru((255, 255, 255))
            licznik += 1
        wynik.wynik = str(przyklad.cyfra)


def main():
    """
    tabP to tablica przycisków kontrolnych (tych z prawej strony okna)
    """
    global run, listaSuperpixeli, wynik, przyklady, przykladyTestowe
    clock = 0
    black = (0, 0, 0)
    white = (255, 255, 255)

    positionX = 0
    positionY = 0
    tabP = []
    przycisk_nauka = Przycisk.Przycisk(300, 40, "buttons/nauka")
    tabP.append(przycisk_nauka)
    przycisk_start = Przycisk.Przycisk(300, 80, "buttons/start")
    tabP.append(przycisk_start)
    przycisk_stop = Przycisk.Przycisk(300, 120, "buttons/stop")
    tabP.append(przycisk_stop)
    przycisk_koniec = Przycisk.Przycisk(300, 160, "buttons/koniec")
    tabP.append(przycisk_koniec)

    x = 10
    y = 10

    for i in range(7):
        for j in range(5):
            superP = SuperPixel.SuperPixel(x, y)
            x += 30
            listaSuperpixeli.append(superP)
        x = 10
        y += 30

    przyklady.dodajPrzyklady()
    przykladyTestowe.dodajPrzykladyTestowe()
#    for p in przyklady.listaPrzykladow:
#        rysuj(p)

    while run:
        clock += pygame.time.Clock().tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for p in tabP:
                    if p.klikPrzycisk():
                        if p.nazwa == "nauka" and not trybNauki:
                            nauka()
                        elif p.nazwa == "start" and not trybNauki:
                            start()
                        elif p.nazwa == "stop":
                            stop()
                        elif p.nazwa == "koniec":
                            koniec()

                if pygame.mouse.get_pressed()[0]:
                    positionX, positionY = pygame.mouse.get_pos()
        #print(str(positionX) + " " + str(positionY))

        for p in listaSuperpixeli:
            if p.x_cord <= positionX < p.x_cord + 30 and p.y_cord <= positionY < p.y_cord + 30 and not trybNauki:
                p.klik()
                break
        positionX = 0
        positionY = 0

        window.fill((60, 25, 60))
        for p in listaSuperpixeli:
            p.draw(window)

        for p in tabP:
            p.draw(window)
        wynik.draw(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
