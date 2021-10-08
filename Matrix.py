import random
import math


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for i in range(rows):
            l = []
            for j in range(cols):
                l.append(0)
            self.data.append(l)

    def normalise(self):
        for i in range(self.cols):
            suma = self.sumuj_kolumne(self, i)
            for j in range(self.rows):
                self.data[j][i] /= suma

    def minus1(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= -1


    @staticmethod
    def sumuj_kolumne(a, numer_kolumny):
        suma = 0
        for i in range(a.rows):
            suma += a.data[i][numer_kolumny]
        return suma

    def multiply(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n

    def multiply_element_wise(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n.data[i][j]

    @staticmethod
    def static_multiply_element_wise(self, n):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * n.data[i][j]
        return result

    @staticmethod
    def static_multiply(a, n):
        for i in range(a.rows):
            for j in range(a.cols):
                a.data[i][j] *= n
        return a

    @staticmethod
    def transpose(a):
        result = Matrix(a.cols, a.rows)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[j][i] = a.data[i][j]
        return result

    @staticmethod
    def static_matrix_product(a, b):
        if a.cols == b.rows:
            matrix = Matrix(a.rows, b.cols)

            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    sum = 0
                    for k in range(a.cols):
                        sum += a.data[i][k] * b.data[k][j]
                    matrix.data[i][j] = sum

            return matrix

        else:
            print("nie mozna wykonac mnozenia macierzy")

    def matrix_product(self, n):

        if self.cols == n.rows:
            a = self
            b = n
            matrix = Matrix(self.rows, n.cols)

            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    sum = 0
                    for k in range(a.cols):
                        sum += a.data[i][k] * b.data[k][j]
                    matrix.data[i][j] = sum

            return matrix

        else:
            print("nie mozna wykonac mnozenia macierzy2")

    def add_number(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += n

    def add_matrix(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += n.data[i][j]

    @staticmethod
    def static_add_matrix(a, b):
        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[i][j] = a.data[i][j] + b.data[i][j]

    @staticmethod
    def substract(a, b):
        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    def substract2(self, a):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] -= a.data[i][j]

    def randomize3(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = round(random.uniform((-1/math.sqrt(n)), (1/math.sqrt(n))), 5)

    def randomize2(self, n, s):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = round(random.uniform(-1, 1), 2)*math.sqrt(2/s ** (n - 1))
                # self.data[i][j] = random.randint(0, 1) * 2 - 1

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = round(random.uniform(-1, 1), 5)
                # self.data[i][j] = random.randint(0, 1) * 2 - 1

    def set_weights1(self):
        self.data[0][0] = 1
        self.data[1][0] = -1
        self.data[2][0] = -1
        self.data[0][1] = -1
        self.data[1][1] = 1
        self.data[2][1] = 1
        self.data[0][2] = 1
        self.data[1][2] = 1
        self.data[2][2] = -1

    def set_weights2(self):
        self.data[0][0] = 1
        self.data[1][0] = -1
        self.data[2][0] = 1
        self.data[0][1] = -1
        self.data[1][1] = 1
        self.data[2][1] = 1
        self.data[0][2] = 1
        self.data[1][2] = 1
        self.data[2][2] = -1

    def set_weights3(self):
        self.data[0][0] = 1
        self.data[0][1] = -1
        self.data[0][2] = 1

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=' ')
            print('\n')

    def map(self, fn):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = fn(val)

    def lrelu(self):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                if val >= 0:
                    self.data[i][j] = val
                if val < 0:
                    self.data[i][j] = val*(0.01)

    @staticmethod
    def static_dilrelu(matrix):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val = matrix.data[i][j]
                if val >= 0:
                    result.data[i][j] = 1
                if val < 0:
                    result.data[i][j] = 0.01
        return result

    @staticmethod
    def static_map(matrix, fn):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val = matrix.data[i][j]
                result.data[i][j] = fn(val)
        return result

    @staticmethod
    def fromArray(array):
        m = Matrix(len(array), 1)
        for i in range(len(array)):
            m.data[i][0] = array[i]
        return m

    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr