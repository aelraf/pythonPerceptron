# -*- coding: utf-8 -*-
# RafKac
# 2021_08_19
#
# program realizujący Perceptron do rozpoznawania liczb, na podstawie mojego kodu z C++
# najpierw tworzymy GUI
# później perceptrona
# "liczby" do rozpoznawania są zapisywane 0/1, gdzie 1 <=> czarny, 0 <=> biały

import pygame


pygame.init()
resolution = (800, 600)
window = pygame.display.set_mode(resolution)


class superPixel:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.kwadrat = pygame.Rect(self.x_cord, self.y_cord, 10, 10)
        self.kolor = self.white

    def klik(self):
        if self.kolor == self.white:
            self.kolor == self.black
        else:
            self.kolor == self.white

    def zmianaKoloru(self, kolor):
        self.kolor = kolor

    def draw(self, win, background):
        pygame.draw.rect(win, self.kolor, self.kwadrat)

"""
Zmienne klasowe:
- współrzędne x i y
- obraz wyświtlany normalnie i po najechaniu myszą
- pole pod przyciskiem, przechwytujące akcje myszy

metoda klikPrzycisk() zwraca True, jeśli klinęliśmy LPM
metoda draw(win) kontroluje wyświetlany obraz (w zależności, czy najechaliśmy myszą, czy nie)
"""
class Przycisk:
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


def main():
    run = True
    clock = 0
    black = (0, 0, 0)
    white = (255, 255, 255)

    while run:
        clock += pygame.time.Clock().tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((60, 25, 60))

        pygame.display.update()


if __name__ == '__main__':
    main()

