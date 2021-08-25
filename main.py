# -*- coding: utf-8 -*-
# RafKac
# 2021_08_19
# 2021_08_23
#
# program realizujący Perceptron do rozpoznawania liczb, na podstawie mojego kodu z C++
# najpierw tworzymy GUI
# później perceptrona
# "liczby" do rozpoznawania są zapisywane 0/1, gdzie 1 <=> czarny, 0 <=> biały

import pygame


pygame.init()
resolution = (800, 600)
window = pygame.display.set_mode(resolution)


class SuperPixel:
    """
     zmienne klasowe
     - współrzędne lewego górnego rogu superpiksela
     - kolor piksela (z pomocniczymi kolorami czarnym i białym)
     - kwadrat kontrolujący superpixel

     metoda klik() zmienia kolor superpixela po kliknięciu na niego
     metoda zmianaKoloru(kolor) zmienia aktualny kolor na zadany
     metoda draw() rysuje superpixel
    """
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.kwadrat = pygame.Rect(self.x_cord, self.y_cord, 30, 30)
        self.kolor = self.white

    def klik(self):
        if self.kolor == self.white:
            self.kolor = self.black
        else:
            self.kolor = self.white

    def zmianaKoloru(self, kolor):
        self.kolor = kolor

    def draw(self, win):
        pygame.draw.rect(win, self.kolor, self.kwadrat)


class Przycisk:
    """
    Zmienne klasowe:
     - współrzędne x i y
     - obraz wyświtlany normalnie i po najechaniu myszą
     - pole pod przyciskiem, przechwytujące akcje myszy

    metoda klikPrzycisk() zwraca True, jeśli klinęliśmy LPM
    metoda draw(win) kontroluje wyświetlany obraz (w zależności, czy najechaliśmy myszą, czy nie)
    """
    def __init__(self, x, y, nazwaPliku):
        self.x_cord = x
        self.y_cord = y
        self.obrazPrzycisku = pygame.image.load(f"{nazwaPliku}.png")
        self.obrazKlikniety = pygame.image.load(f"{nazwaPliku}klik.png")
        self.polePrzycisku = pygame.Rect(self.x_cord, self.y_cord, self.obrazPrzycisku.get_width(), self.obrazPrzycisku.get_height())

    def klikPrzycisk(self):
        if self.polePrzycisku.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, win):
        if self.polePrzycisku.collidepoint(pygame.mouse.get_pos()):
            win.blit(self.obrazKlikniety, (self.x_cord, self.y_cord))
        else:
            win.blit(self.obrazPrzycisku, (self.x_cord, self.y_cord))


class Perceptron:
    """
    klasa realizująca Perceptron
    każdy perceptron inicjujemy jako "zgaszony" (czyli 0), 1 interpretujemy jako "zapalony"
    """

    def __init__(self):
        self.value = 0

    def nauka(self):
        pass

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v


def main():
    run = True
    clock = 0
    black = (0, 0, 0)
    white = (255, 255, 255)
    positionX = 0
    positionY = 0
    przycisk_start = Przycisk()
    przycisk_koniec = Przycisk()
    przycisk_nauka = Przycisk()
    przycisk_koniec = Przycisk()

    x = 10
    y = 10

    listaSuperpixeli = []
    for i in range(7):
        for j in range(5):
            superP = SuperPixel(x, y)
            x += 30
            listaSuperpixeli.append(superP)
        x = 10
        y += 30

    while run:
        clock += pygame.time.Clock().tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    positionX, positionY = pygame.mouse.get_pos()
        print(str(positionX) + " " + str(positionY))

        for p in listaSuperpixeli:
            if p.x_cord <= positionX < p.x_cord + 30 and p.y_cord <= positionY < p.y_cord + 30:
                p.klik()
                positionX = 0
                positionY = 0
                break

        window.fill((60, 25, 60))
        for p in listaSuperpixeli:
            p.draw(window)

        pygame.display.update()


if __name__ == '__main__':
    main()
