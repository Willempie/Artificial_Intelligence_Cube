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

        for x in self.weights:
            print x



    def learn(self, a, b, result):
        self.values = self.calc_all(a, b)

        #print("values")
        #print(self.values)

        self.errors = self.calc_error_all(result)

        #print("errors")
        #print(self.errors)

        self.adjust_weight_all()

        #print("weights")
        #print(self.weights)


        #print(self.weights)
        #print(errors)
        #print("")

        #adjustWeights(weights2, values1, errors2)
        #adjustWeights(weights1, inputs, errors1)

        return

    @staticmethod
    def calc_error_sigmoid(output, B):
        return 0.25 * (output-B) * B * (1-B)

    def calc_error_all(self, result):
        errors = []
        reversed_values = self.reverse_list(self.values)
        reversed_hidden = self.reverse_list(self.hidden)
        reversed_weights = self.reverse_list(self.weights)


        for layer in range(len(reversed_hidden)-1):
            errors.append([])
            total = 0
            for value in range(len(reversed_values[layer])):
                if layer is 0:
                    errors[layer].append(self.calc_error_sigmoid(result, reversed_values[layer][value]))
                else:
                    for weight in range(len(reversed_weights[layer][value])):
                        total += self.weights[layer][weight][value] * errors[layer-1][value]
                    errors[layer].append(total * reversed_values[layer][value] * (1 - reversed_values[layer][value]))

        return self.reverse_list(errors)

    @staticmethod
    def reverse_list(list):
        return [x for x in reversed(list)]


    @staticmethod
    def adjust_weight(weight, input, error):
        return weight + error * input

    def adjust_weight_all(self):
        for layer in range(len(self.hidden)-1):
            for value in range(self.hidden[layer]):
                for next_values in range(self.hidden[layer+1]):
                    weight = self.weights[layer][next_values][value]
                    self.weights[layer][next_values][value] = weight + self.errors[layer][value] * self.values[layer][value]


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
                current_input = values[layer-1]

            for next_input_layer in range(self.hidden[layer+1]):
                set = []
                for weight in range(len(current_input)):
                    set.append(self.weights[layer][weight][next_input_layer])
                values[layer].append(self.calc(set, current_input))

        return values


x = mlp([2, 3], 10)
print(x.weights)
for z in range(50):
    x.learn(0, 0, 1)
    x.learn(0, 1, 0)
    x.learn(1, 0, 0)
    x.learn(1, 1, 1)
    #print(x.weights)
print("---------------------")
print(x.weights)


print(x.calc_all(0,0))
print(x.calc_all(0,1))
print(x.calc_all(1,0))
print(x.calc_all(1,1))



#x.calc_all(1,1,3)

#print(x.calc(x.weights,[1,0]))
#x.learn(0, 1, 1)
