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


pygame.init()
resolution = (400, 300)
window = pygame.display.set_mode(resolution)
run = True


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


class Przyklad:
    """
    klasa ma dwie zmienne - listę 35 cyfr oznaczających piksele (0, 1)
    oraz wartość wyniku do porównywania (zaczynamy od -1, oznaczającą stan nierozpoznany)
    """
    def __init__(self, cyfra=-1):
        self.lista = []
        self.cyfra = cyfra

    def dodajStringDoListy(self, napis, cyfra):
        """
        bierzemy stringa i dodajemy do tablicy intów
        """
        for s in napis:
            self.lista.append(int(s))
        self.cyfra = cyfra

    def czyscListePrzykladow(self):
        self.lista.clear()


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


class Wynik:
    """
    klasa ma za zadanie wyświetlić wynik wraz z podpisem, co to jest
    czyli na górze ma pole tekstowe "Wynik", a na dole pole wyświetlające rozpoznaną cyfrę
    -      oznacza nierozpoznany
    0 - 9  czyli reszta cyfr
    """
    def __init__(self, x, y, w, h):
        self.x_cord = x
        self.y_cord = y
        self.x_wyn = x
        self.y_wyn = y + 30
        self.width = w
        self.height = h
        self.wynik = "-"

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.tekst = self.font.render("Wynik", False, [255, 255, 255])
        self.tekstW = self.font.render(self.wynik, False, [255, 255, 255])

    def draw(self, win):
        self.tekstW = self.font.render(self.wynik, False, [255, 255, 255])
        win.blit(self.tekst, [self.x_cord, self.y_cord])
        win.blit(self.tekstW, [self.x_wyn + 30, self.y_wyn])

    def set_wynik(self, wynik):
        self.wynik = wynik

    def get_wynik(self):
        return self.wynik


def start():
    print("start()")


def stop():
    print("stop()")


def nauka():
    print("nauka()")


def koniec():
    global run
    run = False


def main():
    global run
    clock = 0
    black = (0, 0, 0)
    white = (255, 255, 255)
    wynik = Wynik(200, 50, 50, 50)
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
        print(str(positionX) + " " + str(positionY))

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
