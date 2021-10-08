from Matrix import Matrix
import math


class NeuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, hiddenNodes2, outputNodes, learningRate):

        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.hiddenNodes2 = hiddenNodes2
        self.outputNodes = outputNodes
        self.learningRate = learningRate

        # macierze o liczbie wierszy odpowiadajacej ilosci neuronow w warstwie (druga warstwa w nazwie) i liczbie kolumn odpowiadajcej liczbie wejsc
        self.weightsInputHidden = Matrix(hiddenNodes, inputNodes)
        self.weightsInputHidden.randomize()

        self.weightsHiddenHidden = Matrix(hiddenNodes2, hiddenNodes)
        self.weightsHiddenHidden.randomize()

        self.weightsOutputHidden = Matrix(outputNodes, hiddenNodes2)
        self.weightsOutputHidden.randomize()



        # macierze o liczbie wierszy odpowiadajcej ilosci neuronow w warstwie i 1 kolumnie
        self.biasO = Matrix(self.outputNodes, 1)
        self.biasO.randomize()

        self.biasH = Matrix(self.hiddenNodes, 1)
        self.biasH.randomize()

        self.biasH2 = Matrix(self.hiddenNodes2, 1)
        self.biasH2.randomize()




    # funkcje aktywacji
    def sigmoid(self, x):
        return 1 / (1 + math.e ** -x)

    def disigmoid(self, y):
        return y * (1 - y)

    def sigmoid2(self, x, derivative):
        if derivative == True:
            return x * (1 - x)
        return 1 / (1 + math.e ** -x)

    def tanh(self, x):
        return math.tanh(x)

    def ditanh(self, y):
        return 1 - (y ** 2)

    def lrelu(self, x):
        if x >= 0:
            return x
        else:
            return x*0.01

    def dilrelu(self, y):
        # czy pochodna z 0 to 1 ?
        if y >= 0:
            return 1
        else:
            return 0.01

    def feed_a_layer(self, weights, input, bias):
        result = Matrix.static_matrix_product(weights, input)
        result.add_matrix(bias)
        # result.add_number(1)
        # result.map(self.sigmoid)
        result.map(self.lrelu)
        return result

    def feed_an_output(self, weights, input, bias):
        result = Matrix.static_matrix_product(weights, input)
        result.map(self.lrelu)
        result.add_matrix(bias)
        # result.map(self.sigmoid)
        return result

    def calculate_gradient(self, outputs, output_errors):
        # gradients = Matrix.static_map(outputs, self.disigmoid)
        gradients = Matrix.static_map(outputs, self.dilrelu)
        gradients.multiply_element_wise(output_errors)
        gradients.multiply(self.learningRate)
        return gradients

    def calculate_gradient_output(self, outputs, output_errors):
        # gradients = Matrix.static_map(outputs, self.disigmoid)
        gradients = Matrix.static_map(outputs, self.dilrelu)
        gradients.multiply_element_wise(output_errors)
        gradients.multiply(self.learningRate)
        return gradients

    @staticmethod
    def calculate_deltas(gradients, neuronOutput):
        neuronOutput_T = Matrix.transpose(neuronOutput)
        weights_deltas = Matrix.static_matrix_product(gradients, neuronOutput_T)
        return weights_deltas

    @staticmethod
    def calculate_layer_error(output_weights, next_layer_error):
        weights_t = Matrix.transpose(output_weights)
        weights_t.normalise()
        layer_error = Matrix.static_matrix_product(weights_t, next_layer_error)
        return layer_error

    def feed_forward(self, input_array):

        input = Matrix.fromArray(input_array)

        # tworzy wektory zawierajace sumy wag po aktywacji o ilosci wierszy odpowiadajacej ilosc neuronow w warstwie i 1 kolumnie
        hidden1 = self.feed_a_layer(self.weightsInputHidden, input, self.biasH)
        hidden2 = self.feed_a_layer(self.weightsHiddenHidden, hidden1, self.biasH2)
        output = self.feed_a_layer(self.weightsOutputHidden, hidden2, self.biasO)

        return output.toArray()

    def train(self, input_array, targets_array):

        # feed forward
        input = Matrix.fromArray(input_array)


        hidden1 = self.feed_a_layer(self.weightsInputHidden, input, self.biasH)
        hidden2 = self.feed_a_layer(self.weightsHiddenHidden, hidden1, self.biasH2)
        outputs = self.feed_a_layer(self.weightsOutputHidden, hidden2, self.biasO)

        targets = Matrix.fromArray(targets_array)

        # ERROR = TARGET - OUTPUT
        # blad to moze byc takze blad sredniokwadratowy (output - target)^2
        # bledy warstwy wyjsciowej (ilosc neuronow na wyjsciu X 1 kolumna)
        output_errors = Matrix.substract(targets, outputs)
        print("output errors")
        output_errors.draw()

        # mnozenie wartosci wyjsciowych przez: wartosci bledow, pochodna aktywacji oraz wspolczynnik uczenia ( neurony w warstwie X 1 kolumna)
        gradients = self.calculate_gradient(outputs, output_errors)

        # Calculate deltas
        # wagi pomiedzy warstwami ( ilosc neuronow w warstwie wyjsciowej X ilosc neuronow w warstwie wejsciowej)
        weights_h2o_deltas = self.calculate_deltas(gradients, hidden2)

        # zmiana wag
        self.weightsOutputHidden.add_matrix(weights_h2o_deltas)
        # zmiana biasu
        self.biasO.add_matrix(gradients)


        # Calculate the hidden 2 layer errors
        hidden2_errors = self.calculate_layer_error(self.weightsOutputHidden, output_errors)

        # Calculate gradient h2 -> h
        hidden2_gradient = self.calculate_gradient(hidden2, hidden2_errors)

        # # Calculate hidden to hidden2 deltas
        # macierz o ilosci wierszy odpowiadajacej neuronom w warstwie wejsciowej i ilosci kolumn odpowiadajacej ilosci neuronow w warstwie wyjsciowej
        weights_hh2_deltas = self.calculate_deltas(hidden2_gradient, hidden1)

        # adjust the weights by deltas
        self.weightsHiddenHidden.add_matrix(weights_hh2_deltas)

        # adjust the bias by its deltas (which is just the gradient)
        self.biasH2.add_matrix(hidden2_gradient)

        # # Calculate the hidden layer errors
        hidden_errors = self.calculate_layer_error(self.weightsHiddenHidden, hidden2_errors)

        # Calculate gradient h -> i
        hidden_gradient = self.calculate_gradient(hidden1, hidden_errors)

        # Calculate input to hidden deltas
        weights_ih_deltas = self.calculate_deltas(hidden_gradient, input)


        # adjust the weights by deltas
        self.weightsInputHidden.add_matrix(weights_ih_deltas)
        # adjust the bias by its deltas (which is just the gradient)
        self.biasH.add_matrix(hidden_gradient)




