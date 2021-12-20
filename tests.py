# -*- coding: utf-8 -*-
# RafKac

import unittest
from unittest import TestCase

import pygame.mouse

from Przycisk import Przycisk


def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 3
        tmp[pressed_key] = 1
        return tmp
    return helper


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
        self.assertRaises(key.klikPrzycisk(), True)


if __name__ == "__main__":
    unittest.main()
