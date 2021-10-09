from Metoda import NeuralNetwork
from Matrix import Matrix
import random
import math
from Problem import Dane


class Sterowanie:

    def Metoda(self):

        MLP = NeuralNetwork(3, 10, 10, 1, 0.004)
        #

        # generowanie danych
        dane = Dane()
        tablicaDanych = dane.generujDaneUczace(100)
        input = tablicaDanych[0]
        target = tablicaDanych[1]


        # # dane podane recznie
        # input = [[1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]]
        # target = [[2], [3], [1], [4]]

        # dane znormalizowane
        # dane = Dane()
        # tablicaDanych = dane.generujDaneUczace(500)
        # input = dane.normalizuj_dane_uczace(tablicaDanych, 3)
        # target = tablicaDanych[1]

        # dane do testu wariancji / sredniej
        # dane_wejsciowe = []
        # a = [[1, 0, 1], [2, 1, 1], [3, 0, 1], [4, 1, 1]]
        # dane_wejsciowe.append(a)

        # print("input")
        # print(input)
        # # # print("target")
        # # # print(target)
        # # #
        for j in range(1000):
            i = random.randint(0, 99)
            MLP.train(input[i], target[i])

        print(MLP.feed_forward([0.5, 0, 0.5]))
        print(MLP.feed_forward([0, 0.5, 0.5]))
        print(MLP.feed_forward([0.5, 0, 0]))
        print(MLP.feed_forward([0.5, 0.5, 0.5]))

    # def test_mlp(self):





K = Sterowanie()
K.Metoda()



