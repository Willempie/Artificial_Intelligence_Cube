from random import uniform
from math import exp

class mlp:
    def __init__(self, hidden, epochs):
        self.epochs = epochs
        self.hidden = hidden

        self.weights = []
        for x in range(len(self.hidden)):
            for x in range(len(self.hidden)):
                self.weights.append([uniform(-1, 1) for l in range(self.hidden[x])])

    def learn(self, a, b, result):
        count = len(self.hidden)+1

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
    def calc_error(Y, B):
        return 0.25 * (Y-B) * B * (1-B)

    def calc_error_all(self, result):
        reverse_list = []
        for i in reversed(self.values):
            reverse_list.append(i)

        preceptron_list = []
        for i in reversed([2] + self.hidden):
            preceptron_list.append(i)

        errors = []

        for x in range(len(preceptron_list)-1):
            errors.append([])
            for y in range(preceptron_list[x]):
                errors[x].append([])
                for z in range(preceptron_list[x+1]):
                    if x == 0:
                        errors[x][y].append(self.calc_error(result, reverse_list[x]))
                    else:
                        errors[x][y].append(self.calc_error(errors[x-1][y][z], reverse_list[x]))
        '''
        print("errors")
        for x in range(len(errors)):
            print(errors[x])
        print("errors")
        '''
        errors.reverse()

        return errors

    @staticmethod
    def adjust_weight(weight, input, error):
        return weight + error * input

    def adjust_weight_all(self):

        errors = self.errors

        #print(self.values)
        print(self.weights)
        print(self.errors)
        #print(len(self.errors))
        for x in range(len(errors)):
            #print(len(self.errors[x]))
            for y in range(len(errors[x])):
                #print(len(self.errors[x][y]))
                for z in range(len(self.errors[x][y])):
                    pass
                    #self.weights[x][y] = self.adjust_weight(self.weights[x][y], self.values[x], self.errors[x][y][z])



    @staticmethod
    def calc(weights, inputs):
        total = 0
        my_weights = [1] + weights
        for w in range(len(my_weights)):
            for i in range(len(inputs)):
                total += my_weights[w] * inputs[i]

        return 1 / (1 + exp(-total))

    def calc_all(self, a, b):
        values = []
        for x in range(len(self.hidden)+1):
            if x == 0:
                values.append(self.calc(self.weights[x], [a, b]))
            else:
                values.append(self.calc(self.weights[x], [values[x-1]]))
        return values

x = mlp([3, 4], 10)
for z in range(0):
    x.learn(0, 0, 0)
    x.learn(0, 1, 0)
    x.learn(1, 0, 0)
    x.learn(1, 1, 1)
    print(x.weights)
print("---------------------")

x.learn(0,0,0)

#print(x.calc_all(0,0))
#print(x.calc_all(0,1))
#print(x.calc_all(1,0))
#print(x.calc_all(1,1))



#x.calc_all(1,1,3)

#print(x.calc(x.weights,[1,0]))
#x.learn(0, 1, 1)
