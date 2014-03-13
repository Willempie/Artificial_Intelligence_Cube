from random import uniform
from math import exp

class Preceptron:

    def __init__(self):
        self.weights = [uniform(-1, 1) for l in range(3)]

    def train(self, a, b, result, print_this=False):
        values = [0] + [a, b]
        total = 0
        for x in range(3):
            total += values[x] * self.weights[x]

        Y = None
        if total > 0:
            Y = 1
        else:
            Y = 0

        Z = 1 / (1 + exp(-total))

        fout = 0.25 * (Y-Z)
        if fout < 0:
            fout *= -1

        for x in range(3):
            self.weights[x] = self.weights[x] + values[x] * fout

        if print_this:
            print(Y)
            print(result)
            print(100-fout)
        #print(Y)
        #print(result)

x = Preceptron()
for z in range(0):
    x.train(0,0,0)
    x.train(1,0,1)
    x.train(0,1,1)
    x.train(1,1,1)

x.train(0,0,0,True)
x.train(1,0,1,True)
x.train(0,1,1,True)
x.train(1,1,1,True)

'''
class mlp:

    def __init__(self, input_layer, hidden_layers, output_layer):
        self.input_layer = input_layer
        self.hidden_layers = hidden_layers
        self.output_layer = output_layer
        self.input_weights = []
        self.hidden_weights = []

        self.generate_weights()

        #print(self.input_weights)
        #print(self.hidden_weights)


    def train(self, input_array, result):
        result_output = self.calc_layer(self.input_weights, input_array)
        result_hidden = []
        for x in range(len(self.hidden_layers)):
            result_hidden.append(self.calc_layer(self.hidden_weights[x], input_array))

        errors_hidden = []
        for x in range(len(self.hidden_layers)):
            errors_hidden.append([])
            for y in range(self.hidden_layers[x]):
                y = result
                b = result_hidden[x][y]
                errors_hidden[x].append(0.05 * (y - b) * b * (1-b))

        errors_output = []
        for x in range(self.output_layer):
            for y in range(len(errors_hidden)):
                total = 0
                for z in range(len(errors_hidden[y])):
                    total += self.hidden_weights[y][x] * errors_hidden[y][x]
                errors_output.append(total * result * (1-result))

        for x in range(self.input_layer):
            self.input_weights[x] = self.input_weights[x] + errors_output[x] * result

        for x in range(len(self.hidden_layers)):
            for y in range(self.hidden_layers[x]):
                self.hidden_weights[x][y] = self.hidden_weights[x][y]+ errors_hidden[x][y] * result

        print(result_output)
        #print(errors_hidden)


    @staticmethod
    def calc_layer(weights, inputs):
        return [1 / (1 + exp(-sum(weights[k] * inputs[l] for l in range(len(inputs))))) for k in range(len(weights))]

    def generate_weights(self):
        self.input_weights = [uniform(-1, 1) for l in range(self.input_layer)]
        for x in xrange(len(self.hidden_layers)):
            self.hidden_weights.append([uniform(-1, 1) for l in range(self.hidden_layers[x])])

    def my_print(self):
        print(self.input_weights)
        print(self.hidden_weights)

pr = mlp(2, [2, 5], 1)

for i in range(500):
    pr.train([0, 0], 0)
    pr.train([1, 0], 1)
    pr.train([0, 1], 1)
    pr.train([1, 1], 0)

#pr.my_print()


def learn(self):
    hidden = int(self.hidden.get())
    if hidden <= 0 or hidden >= 1000: return
    if len(self.weights1) <> hidden:
        self.weights1 = [[uniform(-1, 1) for l in range(1+2)] for k in range(hidden)]
        self.weights2 = [[uniform(-1, 1) for l in range(1+hidden)] for k in range(3)]
    outputs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    epochs = int(self.epochs.get())
    for epoch in range(epochs):
        for k in range(self.size):
            for l in range(self.size):
                if self.rects[k][l].color in [1, 2, 3]:
                    train(self.weights1, self.weights2, [k / (1.0 * self.size), l / (1.0 * self.size)], outputs[self.rects[k][l].color-1])
    for k in range(self.size):
        for l in range(self.size):
            if not(self.rects[k][l].color in [1, 2, 3]):
                values0 = [k / (1.0 * self.size), l / (1.0 * self.size)]
                values1 = calc(self.weights1, values0)
                values2 = calc(self.weights2, values1)
                self.rects[k][l].color = 4 + [m for maxval in [max(values2)] for m in range(len(values2)) if values2[m] >= maxval][0]
    display(self)

def calc(weights, inputs):
    values = [1] + inputs
    outputs = [1 / (1 + exp(-sum(weights[k][l] * values[l] for l in range(len(values))))) for k in range(len(weights))]
    return outputs

def propagateErrors(weights, outputs, errors):
    return [sum(weights[l][1+k] * errors[l] for l in range(len(errors))) * outputs[k] * (1 - outputs[k]) for k in range(len(outputs))]

def adjustWeights(weights, inputs, errors):
    values = [1] + inputs
    for k in range(len(errors)):
        for l in range(len(values)):
            weights[k][l] = weights[k][l] + errors[k] * values[l]

def train(weights1, weights2, inputs, outputs):
    values1 = calc(weights1, inputs)
    values2 = calc(weights2, values1)
    errors2 = [0.25 * (outputs[k] - values2[k]) * values2[k] * (1 - values2[k]) for k in range(len(outputs))]
    errors1 = propagateErrors(weights2, values1, errors2)
    adjustWeights(weights2, values1, errors2)
    adjustWeights(weights1, inputs, errors1)
'''
