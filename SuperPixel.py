# RafKac
# 2021_08_26
#
import pygame


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
#        print("metoda klik()")

    def zmianaKoloru(self, kolor):
        self.kolor = kolor
#        print("zmieniono kolor na " + str(self.kolor))

    def draw(self, win):
        pygame.draw.rect(win, self.kolor, self.kwadrat)
#        print("superPixel.draw()" + str(self.x_cord) + " " + str(self.y_cord))
