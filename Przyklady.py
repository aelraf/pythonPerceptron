# RafKac
# 2021_08_26

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


class Przyklady:
    """
    ta klasa odpowiada za stworzenie listy przykładów, którą robimy "ręcznie" - coby nie zaśmiecać
    niepotrzebnym kodem głównej klasy
    na podstawie pomysłu wykorzystanego już przeze mnie w kodzie w C++ w 2018 roku
    """

    def __init__(self):
        self.listaPrzykladow = []

    def dodajPrzyklady(self):
        p1 = Przyklad()
        p1.dodajStringDoListy("01110100011000110001100011000101110", 0)
        self.listaPrzykladow.append(p1)