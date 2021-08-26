# RafKac
# 2021_08_26
import pygame


class Wynik:
    """
    klasa ma za zadanie wyświetlić wynik wraz z podpisem, co to jest,
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