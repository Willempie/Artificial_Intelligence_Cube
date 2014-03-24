## Dick Bruin, 25/02/2014
## Perceptron demo

from random import uniform
from math import exp

class mlp:
    def __init__(self, hidden, epochs):
        self.epochs = epochs
        self.hidden = hidden

        self.weights = []
        self.weights.append([uniform(-1, 1), uniform(-1, 1)])
        for x in range(len(self.hidden)):
            self.weights.append([uniform(-1, 1) for l in range(self.hidden[x])])

    def learn(self, a, b, result):
        count = len(self.hidden)+1
        '''
        values = []
        for x in range(count):
            if x == 0:
                values.append(self.calc(self.weights[x], [a, b]))
            else:
                values.append(self.calc(self.weights[x], [values[x-1]]))
        '''

        values = self.calc_all(a, b)

        errors = []
        for x in range(count):
            if x == 0:
                errors.append(0.05 * (result - values[count-1]) * values[count-1] * (1 - values[count-1]))
            else:
                errors.append(0.05 * (result - errors[x-1]) * errors[x-1] * (1 - errors[x-1]))


        for x in range(count):
            if x == count-1:
                self.adjustWeights(self.weights[count-x-1],[result], errors[x])
            else:
                self.adjustWeights(self.weights[count-x-1],[values[count-1-x]], errors[x])


        #print(self.weights)
        #print(errors)
        #print("")

        #adjustWeights(weights2, values1, errors2)
        #adjustWeights(weights1, inputs, errors1)

        return

    def calc_all(self, a, b):
        values = []
        for x in range(len(self.hidden)+1):
            if x == 0:
                values.append(self.calc(self.weights[x], [a, b]))
            else:
                values.append(self.calc(self.weights[x], [values[x-1]]))
        return values

    @staticmethod
    def adjustWeights(weights, inputs, errors):
        values = [1] + inputs
        for l in range(len(values)):
            weights[l] = weights[l] + errors * values[l]

    @staticmethod
    def calc(weights, inputs):
        total = 0
        my_weights = [1] + weights
        for w in range(len(my_weights)):
            for i in range(len(inputs)):
                total += my_weights[w] * inputs[i]

        return 1 / (1 + exp(-total))


x = mlp([2,2], 10)
for z in range(5000):
    x.learn(0, 0, 0)
    x.learn(0, 1, 0)
    x.learn(1, 0, 0)
    x.learn(1, 1, 1)
print("---------------------")


print(x.calc_all(0,0))
print(x.calc_all(0,1))
print(x.calc_all(1,0))
print(x.calc_all(1,1))
#x.calc_all(1,1,3)

#print(x.calc(x.weights,[1,0]))
x.learn(0, 1, 1)
