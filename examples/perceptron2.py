from random import uniform
from math import exp

class mlp:
    def __init__(self, hidden, epochs):
        self.epochs = epochs
        self.hidden = [2] + hidden

        self.weights = []
        for x in range(len(self.hidden)-1):
            self.weights.append([])
            for y in range(self.hidden[x]+1):
                self.weights[x].append([])
                for z in range(self.hidden[x+1]):
                    self.weights[x][y].append(uniform(-1, 1))

    def answer(self, a, b, solid_output=False):
        output = self.calc_all(a, b)
        output.reverse()
        output = output[0]
        output = sum(output)/len(output)

        if solid_output:
            return 1 if output > 0.5 else 0
        else:
            return output


    def learn(self, a, b, result):
        self.input = [a, b]
        self.values = self.calc_all(a, b)
        self.errors = self.calc_error_all(result)
        self.adjust_weight_all()


    @staticmethod
    def calc_error_sigmoid(output, B):
        return 0.05 * (output-B) * B * (1-B)

    def calc_error_all(self, result):
        errors = []
        reversed_values = self.reverse_list(self.values)
        reversed_hidden = self.reverse_list(self.hidden)
        reversed_weights = self.reverse_list(self.weights)

        # first time
        errors.append([])
        for value in range(reversed_hidden[0]):
            errors[0].append(self.calc_error_sigmoid(result, reversed_values[0][value]))

        # next time
        for layer in range(len(reversed_hidden)-2):
            errors.append([])
            for value in range(reversed_hidden[layer+1]):
                total = 0
                for weight in range(len(reversed_weights[layer][value+1])):
                    total += reversed_weights[layer][value+1][weight] * errors[layer][weight]
                errors[layer+1].append(total * reversed_values[layer+1][value] * (1 - reversed_values[layer+1][value]))

        return self.reverse_list(errors)

    @staticmethod
    def reverse_list(list):
        return [x for x in reversed(list)]


    @staticmethod
    def adjust_weight(weight, input, error):
        return weight + error * input

    def adjust_weight_all(self):
        local_input = [self.input] + self.values
        for x in range(len(local_input)):
            local_input[x].insert(0, 1)

        for layer in range(len(self.hidden) - 1):
            for value in range(self.hidden[layer]+1):
                for next_values in range(self.hidden[layer+1]):
                    input = local_input[layer][value]
                    error = self.errors[layer][next_values]
                    weight = self.weights[layer][value][next_values]

                    self.weights[layer][value][next_values] = self.adjust_weight(weight, input, error)

    @staticmethod
    def calc(weights, inputs):
        if len(weights) is not len(inputs):
            raise ValueError(str(len(weights)) + " - "+ str(len(inputs)))

        total = 0
        for i in range(len(weights)):
            total += weights[i] * inputs[i]

        return 1 / (1 + exp(-total))

    def calc_all(self, a, b):
        values = []

        for layer in range(len(self.hidden)-1):
            values.append([])

            if layer is 0:
                current_input = [1, a, b]
            else:
                current_input = [1] + values[layer-1]

            for next_input_layer in range(self.hidden[layer+1]):
                set = []
                for weight in range(len(current_input)):
                    set.append(self.weights[layer][weight][next_input_layer])

                values[layer].append(self.calc(set, current_input))

        return values


x = mlp([3, 1], 10)

for z in range(10000):
    x.learn(0, 0, 1)
    x.learn(0, 1, 0)
    x.learn(1, 0, 0)
    x.learn(1, 1, 1)

print(x.answer(0, 0))
print(x.answer(0, 1))
print(x.answer(1, 0))
print(x.answer(1, 1))

print(x.answer(0, 0, True))
print(x.answer(0, 1, True))
print(x.answer(1, 0, True))
print(x.answer(1, 1, True))
