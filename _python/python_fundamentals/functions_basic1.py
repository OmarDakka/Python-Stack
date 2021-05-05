1
def a():
    return 5
print(a()) ##The function will return the number 5

2
def a():
    return 5
print(a()+a()) ##The function will return the number 10

3
def a():
    return 5
    return 10
print(a())
            #The function will return the number 5, it wont run any command after the first return

4
def a():
    return 5
    print(10)
print(a())
            #The function will return the number 5, because again it wont run a line of code after the return function.

5
def a():
    print(5)
x = a()
print(x)    #the function prints number 5 which is now stored in variable x, when we print variable x it will return the number 5

6
def a(b, c):
    print(b+c)

print(a(1, 2) + a(2, 3)) ##the function will return an error

7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) ##the function will print out the numbers 2 and 5 without adding them because of the str funciton

8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) ## the function will return the number 100 and 10

9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) ##this will return 7
print(a(5,3)) ##this will return 14
print(a(2,3) + a(5,3)) ##this will return 21

10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) #this will return the number 8

11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b) ##this will print 500,300,500

12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b) ##this will print 500
a() ## this will print 500 and 300 
print(b) ## this will print 500

13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b) ## this will print 500 
b=a() ## this will print 500 and 300
print(b) ## this will print 300

14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() ##this will print 1 and 3 and 2

15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) ## it will print number 1 and print 3 and 5 then print 10
