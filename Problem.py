# generowanie danych
import random
import math

class Dane:

    # def __init__(self, #liczbaArgumentow):
    #     #self.liczbaArgumentow = liczbaArgumentow

    def generujDaneUczace(self, iloscDanych):
        dane = []
        a = []
        b = []
        for i in range(iloscDanych):
            x1 = random.randint(0, 1)
            x2 = random.randint(0, 1)
            x3 = random.randint(0, 1)
            wejscia = [x1, x2, x3]
            wynik = [round((self.funkcja_3argumentowa_1(x1, x2, x3)), 5)]




            a.append(wejscia)
            b.append(wynik)
        dane.append(a)
        dane.append(b)
        return dane

        # return round(random.uniform(0, x), 2)

    # def normalizuj_dane_uczace(self, dane_wejsciowe, ilosc_argumentow):
    #     data = []
    #     a = []
    #
    #     for i in range(ilosc_argumentow):
    #         for i in range(len(dane_wejsciowe[0])):
    #             srednia = self.oblicz_srednia_arytmetyczna(dane_wejsciowe, i)
    #             wariancja = self.oblicz_wariancje(dane_wejsciowe, i)
    #             wejscia = []
    #             znormalizowany_argument = 0
    #             for j in range(len(dane_wejsciowe.a)):
    #                     znormalizowany_argument += (dane_wejsciowe[0][j][i] - srednia)
    #                     znormalizowany_argument /= math.sqrt(wariancja)
    #     return data

    def normalizuj_dane_uczace(self, dane_wejsciowe, ilosc_argumentow):
        data = []
        a = []
        data.append(a)
        for i in range(len(dane_wejsciowe[0])-1):
            x = []
            data.append(x)


        for i in range(ilosc_argumentow):
            for j in range(len(dane_wejsciowe[0])):
                srednia = self.oblicz_srednia_arytmetyczna(dane_wejsciowe, i-1)
                wariancja = self.oblicz_wariancje(dane_wejsciowe, i-1)
                argument = self.normalizuj_argument(dane_wejsciowe[0][j][i], srednia, wariancja)
                data[j].append(argument)

        return data

    def normalizuj_argument(self, wartosc_argumentu, srednia, wariancja):
        return (wartosc_argumentu - srednia)/(math.sqrt(wariancja) + 0.5)

    def oblicz_wariancje(self, dane_wejsciowe, ktory_argument):
        srednia = self.oblicz_srednia_arytmetyczna(dane_wejsciowe, ktory_argument)
        suma_argumentow = 0
        for i in range(len(dane_wejsciowe[0])):
            suma_argumentow += ((dane_wejsciowe[0][i][ktory_argument] - srednia) ** 2)
        return suma_argumentow/len(dane_wejsciowe[0])

    def oblicz_srednia_arytmetyczna(self, dane_wejsciowe, ktory_argument):
        suma_argumentow = 0
        for i in range(len(dane_wejsciowe[0])):
            suma_argumentow += dane_wejsciowe[0][i][ktory_argument]
        return suma_argumentow/len(dane_wejsciowe[0])

    def funkcja_3argumentowa_1(self, x1, x2, x3):
        return (x1 ** 2) + (2*x2) + x3

    def funkcja_3argumentowa_2(self, x1, x2, x3):
        return x1 + 2*x2 ** 2 + x3 ** 3

    def funkcja_3argumentowa_3(self, x1, x2, x3):
        return x1 ** 3 + 3*x2 + x3 ** 2


    #
    # def funkcja2(self, x1, x2, x3, x4, x5):
    #
    #
    # def funkcja3(self, x1, x2, x3, x4, x5, x6, x7):
    #     return x1 + x2 ** 2 + x3 + x4 ** 2 + x5 + x6 ** 2 + x7





    # def pobierz(self):
