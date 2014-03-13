## Dick Bruin, 25/02/2014
## Perceptron demo

from random import uniform
from math import exp

class mlp:
    def __init__(self):
        self.weights1 = []
        self.weights2 = []
        self.epochs = 50
        self.hidden = 10

    def learn(self):
        if self.hidden <= 0 or self.hidden >= 1000: return
        if len(self.weights1) <> self.hidden:
            self.weights1 = [[uniform(-1, 1) for l in range(1+2)] for k in range(self.hidden)]
            self.weights2 = [[uniform(-1, 1) for l in range(1+self.hidden)] for k in range(3)]
        outputs = [[1, 0], [0, 1]]

        for epoch in range(self.epochs):
            self.train(self.weights1, self.weights2, [0, 0], [0])
            self.train(self.weights1, self.weights2, [0, 1], [1])
            self.train(self.weights1, self.weights2, [1, 0], [1])
            self.train(self.weights1, self.weights2, [1, 1], [0])

        #print(self.weights1)

        values0 = [1,1]
        values1 = self.calc(self.weights1, values0)
        values2 = self.calc(self.weights2, values1)
        #print(values2)
        print[m for maxval in [max(values2)] for m in range(len(values2)) if values2[m] >= maxval][0]

    @staticmethod
    def calc(weights, inputs):
        values = [1] + inputs
        outputs = [1 / (1 + exp(-sum(weights[k][l] * values[l] for l in range(len(values))))) for k in range(len(weights))]
        return outputs

    @staticmethod
    def propagateErrors(weights, outputs, errors):
        return [sum(weights[l][1+k] * errors[l] for l in range(len(errors))) * outputs[k] * (1 - outputs[k]) for k in range(len(outputs))]

    @staticmethod
    def adjustWeights(weights, inputs, errors):
        values = [1] + inputs
        for k in range(len(errors)):
            for l in range(len(values)):
                weights[k][l] = weights[k][l] + errors[k] * values[l]

    def train(self, weights1, weights2, inputs, outputs):
        values1 = self.calc(weights1, inputs)
        values2 = self.calc(weights2, values1)
        errors2 = [0.25 * (outputs[k] - values2[k]) * values2[k] * (1 - values2[k]) for k in range(len(outputs))]
        errors1 = self.propagateErrors(weights2, values1, errors2)
        self.adjustWeights(weights2, values1, errors2)
        self.adjustWeights(weights1, inputs, errors1)

x = mlp()
x.learn()