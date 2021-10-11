import math
import numpy as np
import scipy.special


class NeuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, hiddenNodes2, outputNodes, learningRate):

        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.hiddenNodes2 = hiddenNodes2
        self.outputNodes = outputNodes
        self.learningRate = learningRate

        # macierze o liczbie wierszy odpowiadajacej ilosci neuronow w warstwie (druga warstwa w nazwie) i liczbie kolumn odpowiadajcej liczbie wejsc
        self.weightsInputHidden = np.random.rand(self.hiddenNodes, self.inputNodes) - 0.5
        self.weightsHiddenHidden = np.random.rand(self.hiddenNodes2, self.hiddenNodes) - 0.5
        self.weightsOutputHidden = np.random.rand(self.outputNodes, self.hiddenNodes2) - 0.5

        # macierze o liczbie wierszy odpowiadajcej ilosci neuronow w warstwie i 1 kolumnie
        self.biasO = np.random.rand(self.outputNodes, 1) - 0.5
        self.biasH = np.random.rand(self.hiddenNodes, 1) - 0.5
        self.biasH2 = np.random.rand(self.hiddenNodes2, 1) - 0.5

        # self.activation_function = lambda x:scipy.special.expit(x)

    def ReLU(self, X):
        return np.maximum(0, X)

    def ReLU_deriv(self, Z):
        return Z > 0

    def feed_a_layer(self, weights, input, bias):
        result = np.dot(weights, input) + bias
        output = self.ReLU(result)
        return output

    def calculate_gradient(self, outputs, output_errors):
        # gradients = Matrix.static_map(outputs, self.disigmoid)
        gradients = self.ReLU_deriv(outputs)
        gradients = np.multiply(gradients, output_errors)
        gradients = gradients * self.learningRate
        return gradients

    def calculate_deltas(self, gradients, neuronOutput):
        neuronOutput_T = np.array(neuronOutput).T
        weights_deltas = np.dot(gradients, neuronOutput_T)
        return weights_deltas

    def calculate_layer_error(self, output_weights, next_layer_error):
        weights_t = output_weights.T
        layer_error = np.dot(weights_t, next_layer_error)
        return layer_error

    def feed_forward(self, input_array):

        input = np.array(input_array, ndmin=2).T

        # tworzy wektory zawierajace sumy wag po aktywacji o ilosci wierszy odpowiadajacej ilosc neuronow w warstwie i 1 kolumnie
        hidden1 = self.feed_a_layer(self.weightsInputHidden, input, self.biasH)
        hidden2 = self.feed_a_layer(self.weightsHiddenHidden, hidden1, self.biasH2)
        output = self.feed_a_layer(self.weightsOutputHidden, hidden2, self.biasO)

        return output

    def train(self, input_array, targets_array):
        # feed forward
        input = np.array(input_array, ndmin=2).T

        hidden1 = self.feed_a_layer(self.weightsInputHidden, input, self.biasH)
        hidden2 = self.feed_a_layer(self.weightsHiddenHidden, hidden1, self.biasH2)
        outputs = self.feed_a_layer(self.weightsOutputHidden, hidden2, self.biasO)

        # ERROR = TARGET - OUTPUT
        # blad to moze byc takze blad sredniokwadratowy (output - target)^2
        # bledy warstwy wyjsciowej (ilosc neuronow na wyjsciu X 1 kolumna)
        output_errors = targets_array - outputs

        # mnozenie wartosci wyjsciowych przez: wartosci bledow, pochodna aktywacji oraz wspolczynnik uczenia ( neurony w warstwie X 1 kolumna)
        gradients = self.calculate_gradient(outputs, output_errors)

        # Calculate deltas
        # wagi pomiedzy warstwami ( ilosc neuronow w warstwie wyjsciowej X ilosc neuronow w warstwie wejsciowej)
        weights_h2o_deltas = self.calculate_deltas(gradients, hidden2)

        # zmiana wag
        self.weightsOutputHidden = self.weightsOutputHidden + weights_h2o_deltas
        # zmiana biasu
        self.biasO = self.biasO + gradients


        # Calculate the hidden 2 layer errors
        hidden2_errors = self.calculate_layer_error(self.weightsOutputHidden, output_errors)

        # Calculate gradient h2 -> h
        hidden2_gradient = self.calculate_gradient(hidden2, hidden2_errors)

        # # Calculate hidden to hidden2 deltas
        # macierz o ilosci wierszy odpowiadajacej neuronom w warstwie wejsciowej i ilosci kolumn odpowiadajacej ilosci neuronow w warstwie wyjsciowej
        weights_hh2_deltas = self.calculate_deltas(hidden2_gradient, hidden1)

        # adjust the weights by deltas
        self.weightsHiddenHidden = self.weightsHiddenHidden + weights_hh2_deltas

        # adjust the bias by its deltas (which is just the gradient)
        self.biasH2 = self.biasH2 + hidden2_gradient

        # # Calculate the hidden layer errors
        hidden_errors = self.calculate_layer_error(self.weightsHiddenHidden, hidden2_errors)

        # Calculate gradient h -> i
        hidden_gradient = self.calculate_gradient(hidden1, hidden_errors)

        # Calculate input to hidden deltas
        weights_ih_deltas = self.calculate_deltas(hidden_gradient, input)


        # adjust the weights by deltas
        self.weightsInputHidden = self.weightsInputHidden + weights_ih_deltas
        # adjust the bias by its deltas (which is just the gradient)
        self.biasH = self.biasH + hidden_gradient




