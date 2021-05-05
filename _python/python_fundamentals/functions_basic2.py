1
def countdown(number):
    for x in range(number, 0, -1):
        print(x)
countdown(50)

2
def printAndReturn(a,b):
      print(a)
      return(b)
print(printAndReturn(5,6))

3
def first_plus_length(list):
   x = list[0] + len(list)
   print(x)

first_plus_length([1,2,3,4,5,6])

4
def values_greater_than_second(list):
    newList = []
    counter = 0
    if len(list) <= 2:
        return False
    else:
        for i in range(len(list)):
            if list[1] < list[i]:
                newList.append(list[i])
                counter = counter + 1
        print(counter)
        return newList


print(values_greater_than_second([1, 2, 3, 4, 5, 6]))
print(values_greater_than_second([5,2,6,1,2,10,-15]))

5
def length_and_value(size,value):
    newList = []
    for x in range(0,size,1):
        newList.append(value)
    return newList

print(length_and_value(6,2))