from random import uniform
from math import exp


class mlp():

    hidden_layers = None
    weights = None

    values = None

    def __init__(self, hidden_layers_array):
        self.hidden_layers = [2] + hidden_layers_array  # input, + hidden layers

        self.weights = []
        # generate weights
        for num_layer in range(len(self.hidden_layers) - 1):
            self.weights.append([])
            for hidden_layer in range(self.hidden_layers[num_layer] + 1):
                self.weights[num_layer].append([])
                for z in range(self.hidden_layers[num_layer+1]):
                    self.weights[num_layer][hidden_layer].append(uniform(-1, 1))


    def calc_values(self, a, b):
        values = []
        print self.weights

        for num_layers in range(len(self.hidden_layers) - 1):
            print num_layers, "num"
            for x in range(len(self.weights[num_layers])):
                set = []
                for y in range(len(self.weights[num_layers][x])):
                    set.append(self.weights[num_layers][x])
                    print self.weights[num_layers][x]





    @staticmethod
    def calc_error_first(output, B):
        return 0.25 * (output-B) * B * (1-B)



    @staticmethod
    def reverse_list(list):
        return [x for x in reversed(list)]


    def learn(self, a, b, result):
        # calc values
        self.calc_values(a,b)

        # calc errors


        # adjust weights


        return

    def print_function(self):

        for num_layers in range(len(self.hidden_layers) - 1):
            print(num_layers)



        print "-----------------------"




multilayerp = mlp([3, 7])
for x in range(1):
    multilayerp.learn(0, 0, 1)
    #multilayerp.learn(0, 1, 0)
    #multilayerp.learn(1, 0, 0)
    #multilayerp.learn(1, 1, 1)

#multilayerp.print_function()


