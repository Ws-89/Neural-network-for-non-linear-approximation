from Metoda import NeuralNetwork
import random
from Problem import Dane


class Sterowanie:

    def Metoda(self):

        MLP = NeuralNetwork(3, 10, 10, 1, 0.05)
        #

        # generowanie danych
        dane = Dane()
        tablicaDanych = dane.generujDaneUczace(100)
        input = tablicaDanych[0]
        target = tablicaDanych[1]

        for j in range(10000):
            i = random.randint(0, 99)
            MLP.train(input[i], target[i])

        print(MLP.feed_forward([0.5, 0, 0.5]))
        print(MLP.feed_forward([0, 0.5, 0.5]))
        print(MLP.feed_forward([0.5, 0, 0]))
        print(MLP.feed_forward([0.5, 0.5, 0.5]))


if __name__ == "__main__":
    K = Sterowanie()
    K.Metoda()



