# -*- coding: utf-8 -*-
# RafKac
# 2021_08_19
# 2021_08_23
# 2021_08_25
#
# program realizujący Perceptron do rozpoznawania liczb, na podstawie mojego kodu z C++
# najpierw tworzymy GUI
# później perceptrona
# "liczby" do rozpoznawania są zapisywane 0/1, gdzie 1 <=> czarny, 0 <=> biały

import pygame
import Perceptron
import SuperPixel
import Przyklady
import Wynik
import time


pygame.init()
resolution = (400, 300)
window = pygame.display.set_mode(resolution)
run = True
listaSuperpixeli = []
wynik = Wynik.Wynik(200, 50, 50, 50)


class Przycisk:
    """
    Zmienne klasowe:
     - współrzędne x i y
     - obraz wyświtlany normalnie i po najechaniu myszą
     - pole pod przyciskiem, przechwytujące akcje myszy

    metoda klikPrzycisk() zwraca True, jeśli klinęliśmy LPM
    metoda draw(win) kontroluje wyświetlany obraz (w zależności, czy najechaliśmy myszą, czy nie)

    zmienna "nazwa" kontroluje akcję po wciśnięciu przycisku
    """
    def __init__(self, x, y, nazwaPliku):
        self.x_cord = x
        self.y_cord = y
        self.obrazPrzycisku = pygame.image.load(f"{nazwaPliku}.png")
        self.obrazKlikniety = pygame.image.load(f"{nazwaPliku}klik.png")
        self.polePrzycisku = pygame.Rect(self.x_cord, self.y_cord, self.obrazPrzycisku.get_width(), self.obrazPrzycisku.get_height())
        self.nazwa = nazwaPliku[8:]
        self.status = False

    def klikPrzycisk(self):
        if self.polePrzycisku.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.status = True
                return True
        self.status = False
        return False

    def draw(self, win):
        if self.polePrzycisku.collidepoint(pygame.mouse.get_pos()):
            win.blit(self.obrazKlikniety, (self.x_cord, self.y_cord))
        else:
            win.blit(self.obrazPrzycisku, (self.x_cord, self.y_cord))

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status


def start():
    print("start()")


def stop():
    print("stop()")


def nauka():
    print("nauka()")


def koniec():
    global run
    run = False


def rysuj(przyklad):
    global listaSuperpixeli, wynik
    print(przyklad.lista)
    licznik = 0
    for i in przyklad.lista:
        if i == 1:
            listaSuperpixeli[licznik].zmianaKoloru((0, 0, 0))
        else:
            listaSuperpixeli[licznik].zmianaKoloru((255, 255, 255))
        licznik += 1
    wynik.wynik = str(przyklad.cyfra)
    time.sleep(3)


def main():
    """
    tabP to tablica przycisków kontrolnych (tych z prawej strony okna)
    """
    global run, listaSuperpixeli, wynik
    clock = 0
    black = (0, 0, 0)
    white = (255, 255, 255)

    positionX = 0
    positionY = 0
    tabP = []
    przycisk_nauka = Przycisk(300, 40, "buttons/nauka")
    tabP.append(przycisk_nauka)
    przycisk_start = Przycisk(300, 80, "buttons/start")
    tabP.append(przycisk_start)
    przycisk_stop = Przycisk(300, 120, "buttons/stop")
    tabP.append(przycisk_stop)
    przycisk_koniec = Przycisk(300, 160, "buttons/koniec")
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

    przyklady = Przyklady.Przyklady()
    przykladyTestowe = Przyklady.Przyklady()
    przyklady.dodajPrzyklady()
    przykladyTestowe
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
                        if p.nazwa == "nauka":
                            nauka()
                        elif p.nazwa == "start":
                            start()
                        elif p.nazwa == "stop":
                            stop()
                        elif p.nazwa == "koniec":
                            koniec()

                if pygame.mouse.get_pressed()[0]:
                    positionX, positionY = pygame.mouse.get_pos()
        #print(str(positionX) + " " + str(positionY))

        for p in listaSuperpixeli:
            if p.x_cord <= positionX < p.x_cord + 30 and p.y_cord <= positionY < p.y_cord + 30:
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
