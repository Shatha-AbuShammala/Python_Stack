x = [ [5,2,3], [10,8,9] ]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# Update Values
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
print(sports_directory['soccer'][1])
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print("x =", x)
print("students =", students)
print("sports_directory =", sports_directory)
print("z =", z)

#Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(key, "-", value)
iterateDictionary(students)



#get value from alist of direction
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key,some_list):
    for dectionary in some_list:
        print(dectionary[key])

iterateDictionary2('first_name' ,students)
iterateDictionary2('last_name' ,students)


#Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key)
        for item in value:
            print(item)

printInfo(dojo)


