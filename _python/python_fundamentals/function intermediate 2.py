#1
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update():
    (x[1])[0] = 15
    students[0]['last_name'] = 'Bryant'
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30
    print(x)
    print(students)
    print(sports_directory)
    print(z)

update()

2


students = [
{'first_name': 'Michael', 'last_name': 'Jordan'},
{'first_name': 'John', 'last_name': 'Rosales'},
{'first_name': 'Mark', 'last_name': 'Guillen'},
{'first_name': 'KB', 'last_name': 'Tonel'}
]   
def iterateDictionary():
    for key in students:
        print("first_name", "-", key['first_name'],"," "last_name","-", key['last_name'])

iterateDictionary()

3


def iterateDictionary2(key_name, list_name):
    for k in list_name:
        print(k[key_name])

iterateDictionary2('last_name', students)

4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(x):
    for i in x:
        print(len(x[i]),i.upper())
        print(*x[i], sep = "\n")
        

printInfo(dojo)

 


