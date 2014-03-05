
input1 = [10, 5, -6, -8, 2]
input1_a = True
input2 = [10, -5, -8, -9, 16]
input2_a = False
input3 = [1, 1, 1, 1, -4]
input3_a = True
input4 = [2, 3, -8, -1, -1]
input4_a = False
input5 = [4, 4, 4, -8, -5]
input5_a = True

weights = [1000, 1000, 1000, 1000, 1000]


def predict(input_array, result, ref_weights):

    while True:
        count = 0

        for x in xrange(5):
            count += input_array[x] * ref_weights[x]

        answer = count >= 0

        if result is answer:
            return True
        else:
            adjust_weights(input_array, result, ref_weights)


def adjust_weights(input_array, result, ref_weights):
    for x in xrange(5):
        if int(result) > 0:
            if input_array[x] >= 0:
                ref_weights[x] += 1
            else:
                ref_weights[x] -= 1
        else:
            if input_array[x] < 0:
                ref_weights[x] += 1
            else:
                ref_weights[x] -= 1

print(predict(input1, input1_a, weights))
print(weights)
print(predict(input2, input2_a, weights))
print(weights)
print(predict(input3, input3_a, weights))
print(weights)
print(predict(input4, input4_a, weights))
print(weights)
print(predict(input5, input5_a, weights))
print(weights)

print(predict(input1, input1_a, weights))
print(weights)
print(predict(input2, input2_a, weights))
print(weights)
print(predict(input3, input3_a, weights))
print(weights)
print(predict(input4, input4_a, weights))
print(weights)
print(predict(input5, input5_a, weights))
print(weights)




