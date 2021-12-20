# -*- coding: utf-8 -*-
# RafKac

import unittest
from unittest import TestCase

import pygame.mouse

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

        p = Przyklad()
        p.dodajStringDoListy("01110100011000110001100011000101110", 0)
        self.assertIn(list.listaPrzykladow, [p])

    def test_dodajPrzykladyTestowe(self):
        list = Przyklady()
        list.dodajPrzykladyTestowe()


if __name__ == "__main__":
    unittest.main()
