# -*- coding: utf-8 -*-
# RafKac

import unittest
from unittest import TestCase

import pygame.mouse

from Perceptron import Perceptron
from Przycisk import Przycisk
from Przyklady import Przyklad, Przyklady


def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 3
        tmp[pressed_key] = 1
        return tmp

    return helper


def create_Przyklad():
    p = Przyklad()
    p.dodajStringDoListy("01110100011000110001100011000101110", 0)
    return p


class TestsPrzycisk(TestCase):
    def test_klik_przycisk(self):
        """if self.polePrzycisku.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.status = True
                return True
        self.status = False
        return False"""
        key = Przycisk(300, 40, "buttons/nauka")
        pygame.mouse.get_pressed = create_key_mock([0])
        self.assertEqual(key.klikPrzycisk(), True)


class TestsPrzyklady(TestCase):
    def test_dodajStringDoListy(self):
        p = create_Przyklad()
        self.assertEqual(p.lista,
                         [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0,
                          1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0])
        self.assertIsInstance(p, Przyklad)

    def test_zaburzPrzyklad(self):
        p = create_Przyklad()
        self.assertIsNot(p.zaburzPrzyklad(), p)

    def test_czyscListePrzykladow(self):
        p = create_Przyklad()
        p.czyscListePrzykladow()
        self.assertEqual(p.lista, [])

    def test_dodajPrzyklady(self):
        list = Przyklady()
        list.dodajPrzyklady()
        self.assertIsNot(list, [])

        p = create_Przyklad()
        self.assertEqual(list.listaPrzykladow[0].lista, p.lista)
        self.assertIsInstance(list, Przyklady)

    def test_dodajPrzykladyTestowe(self):
        list = Przyklady()
        list.dodajPrzykladyTestowe()
        self.assertIsNot(list, [])

        p = Przyklad()
        p.dodajStringDoListy("01110100011000110001100011000101111", 0)
        self.assertEqual(list.listaPrzykladow[0].lista, p.lista)
        self.assertIsInstance(list, Przyklady)


def give_perceptron(n=2):
    theta = 0.01
    ERR = 0.0
    wynik = 0.345
    stalaU = 0.005
    czyPrzyklad = -1.0
    return Perceptron(n=n, theta=theta, ERR=ERR, wynik=wynik, stalaU=stalaU, czyPrzyklad=czyPrzyklad)


class TestsPerceptron(TestCase):
    def test_wartosc_err(self):
        perceptron = give_perceptron()
        tj1 = 2
        tj2 = 5
        wynik = perceptron.wartosc_err(T_j=tj1)
        self.assertEqual(perceptron.ERR, 1.0-0.345)

        wynik2 = perceptron.wartosc_err(T_j=tj2)
        self.assertEqual(perceptron.ERR, -1.0-0.345)

    def test_co_jest_na_wejsciu(self):
        perceptron = give_perceptron()


if __name__ == "__main__":
    unittest.main()
