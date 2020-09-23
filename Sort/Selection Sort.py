import random

def make_list(listSize, lowerBound, upperBound):
    values = []
    for _ in range(listSize):
        num = random.randint(lowerBound, upperBound)
        values.append(num)
    return values


def swap_places(index1, index2):
    num1 = values[index1]
    num2 = values[index2]
    values[index1] = num2
    values[index2] = num1
    return values


LOWER_BOUND = 0
UPPER_BOUND = 10
LIST_SIZE = 35
values = make_list(LIST_SIZE, LOWER_BOUND, UPPER_BOUND)
print(values)
for index1 in range(len(values)):
    smallest = None
    cutOff = index1 + 1
    for index2 in range(len(values[cutOff:])):
        if smallest is None or values[cutOff + index2] < smallest:
            smallest = values[cutOff + index2]
            indexToChange = cutOff + index2
    swap_places(index1, indexToChange)
    print(values)
