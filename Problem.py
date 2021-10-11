# generowanie danych
import random
import math
import numpy as np

class Dane:

    def generujDaneUczace(self, iloscDanych):
        dane = []
        a = []
        b = []
        for i in range(iloscDanych):
            x1 = random.uniform(0.01, 0.5)
            x2 = random.uniform(0.01, 0.5)
            x3 = random.uniform(0.01, 0.5)
            wejscia = np.array([x1, x2, x3])
            wynik = np.array([round((self.funkcja_3argumentowa_1(x1, x2, x3)), 5)])

            a.append(wejscia)
            b.append(wynik)
        dane.append(a)
        dane.append(b)
        return dane

    def funkcja_3argumentowa_1(self, x1, x2, x3):
        return (x1 ** 2) + (2*x2) + x3

    def funkcja_3argumentowa_2(self, x1, x2, x3):
        return x1 + 2*x2 ** 2 + x3 ** 3

    def funkcja_3argumentowa_3(self, x1, x2, x3):
        return x1 ** 3 + 3*x2 + x3 ** 2




