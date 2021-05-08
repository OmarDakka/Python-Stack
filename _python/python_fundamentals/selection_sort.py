array = [5,3,8,9,5,2,1]
n = len(array)
for j in range(n-1):
    for i in range(0, n-j-1):
        if array[i]>array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

print(array)