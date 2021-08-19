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
resolution = (1280, 720)
window = pygame.display.set_mode(resolution)


def main():
    run = True
    clock = 0

    while run:
        clock += pygame.time.Clock().tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == '__main__':
    main()

