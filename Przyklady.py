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
        p0 = Przyklad()
        p0.dodajStringDoListy("01110100011000110001100011000101110", 0)
        self.listaPrzykladow.append(p0)
        p1 = Przyklad()
        p1.dodajStringDoListy("00001000110010101001100010000100001", 1)
        self.listaPrzykladow.append(p1)
        p2 = Przyklad()
        p2.dodajStringDoListy("01110100010001000100010001000011111", 2)
        self.listaPrzykladow.append(p2)
        p3 = Przyklad()
        p3.dodajStringDoListy("11110000010000101111000010000111110", 3)
        self.listaPrzykladow.append(p3)
        p4 = Przyklad()
        p4.dodajStringDoListy("00001000110010101001111110000100001", 4)
        self.listaPrzykladow.append(p4)
        p5 = Przyklad()
        p5.dodajStringDoListy("11111100001000011110000010000111110", 5)
        self.listaPrzykladow.append(p5)
        p6 = Przyklad()
        p6.dodajStringDoListy("11111100001000011111100011000111110", 6)
        self.listaPrzykladow.append(p6)
        p7 = Przyklad()
        p7.dodajStringDoListy("11111000010001000100010001000010000", 7)
        self.listaPrzykladow.append(p7)
        p8 = Przyklad()
        p8.dodajStringDoListy("01110100011000101110100011000101110", 8)
        self.listaPrzykladow.append(p8)
        p9 = Przyklad()
        p9.dodajStringDoListy("11111100011000101111000010000101111", 9)
        self.listaPrzykladow.append(p9)

    def dodajPrzykladyTestowe(self):
        p0 = Przyklad()
        p0.dodajStringDoListy("01110100011000110001100011000101111", 0)
        self.listaPrzykladow.append(p0)
        p1 = Przyklad()
        p1.dodajStringDoListy("00001100110010101001101010000100001", 1)
        self.listaPrzykladow.append(p1)
        p2 = Przyklad()
        p2.dodajStringDoListy("01110100010001000100011000000011111", 2)
        self.listaPrzykladow.append(p2)
        p3 = Przyklad()
        p3.dodajStringDoListy("01110100010000101110010011000101110", 3)
        self.listaPrzykladow.append(p3)
        p4 = Przyklad()
        p4.dodajStringDoListy("00001000100010001001111110000100001", 4)
        self.listaPrzykladow.append(p4)
        p5 = Przyklad()
        p5.dodajStringDoListy("11111100001000010000111100000111110", 5)
        self.listaPrzykladow.append(p5)
        p6 = Przyklad()
        p6.dodajStringDoListy("01111100001000011110100011000111111", 6)
        self.listaPrzykladow.append(p6)
        p7 = Przyklad()
        p7.dodajStringDoListy("11111000010001011111001000100010000", 7)
        self.listaPrzykladow.append(p7)
        p8 = Przyklad()
        p8.dodajStringDoListy("01110100011000101110100011000111111", 8)
        self.listaPrzykladow.append(p8)
        p9 = Przyklad()
        p9.dodajStringDoListy("01110100011000101110000010000101110", 9)
        self.listaPrzykladow.append(p9)
        p10 = Przyklad()
        p10.dodajStringDoListy("00010001010100110100000100000111111", -1)
        self.listaPrzykladow.append(p10)
        p11 = Przyklad()
        p11.dodajStringDoListy("00100010111000101010001000101010101", -1)
        self.listaPrzykladow.append(p11)

