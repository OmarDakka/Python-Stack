#1
def biggie(array: list):
    for i in range(len(array)):
        if array[i] >= 0:
            array[i] = "Big PP"
    return array

print(biggie([3,-2,10,-69,0]))

#2
def count_positives(array: list):
    counter: int = 0
    for i in range(len(array)):
        if array[i] > 0:
            counter = counter + 1
    array[len(array) - 1] = counter
    return array

print(count_positives([-3,10,-2,4,5,6,-10]))

#3
def sum(array: list):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    return sum
print(sum([1,23,4,5,56,6,7,78,788]))

#4
def average(array: list):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    return (sum/len(array))

print(average([1,23,4,5,66,7,312,22]))

#5
def length(array: list):
    counter: int = 0
    for i in range(len(array)):
        counter = counter + 1
    return counter

print(length([1,23,3,4,5,6,67,7,78]))

#6
def min(array: list):
    min: int = 999
    if array == []:
        return False
    else:
        for i in array:
            if i < min:
                min = i
        return min

print(min([124,232,45,6,7,1,4,34]))
print(min([]))

#7
def max(array: list):
    max: int = 0
    if array == []:
        return False
    else:
        for i in array:
            if i > max:
                max = i
        return max

print(max([124,232,45,6,7,1,4,34]))
print(max([]))

#8
def ultimate_analysis(array: list):
    max: int = 0
    min: int = 999
    sum: int = 0
    counter: int = 0
    average: float = 0
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
        sum = sum + i
        average = sum/ len(array)
        counter = counter + 1
    return ("sumTotal: " + str(sum),"average: " + str(average), "minimum: " + str(min), "maximum: " + str(max), "length: " + str(counter))

print(ultimate_analysis([14,23,5,6445,23,1,12]))

# 9
import math
def reverse_list(array: list):
    temp: int = 0
    halfArrayIndex =math.floor(len(array)/2)
    for i in range(halfArrayIndex):
        temp = array[i]
        array[i] = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = temp
    return array


print(reverse_list([1, 3, 5, 6, 10,123,2,444,-13, 2, 3]))
