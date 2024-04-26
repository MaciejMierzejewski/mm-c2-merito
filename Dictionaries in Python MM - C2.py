#EXCERCISE 1- Write a Python program to add a key to a dictionary.
dictionary = {0: 10, 1: 20}
print(dictionary)

dictionary.update({2:30})

print(dictionary)

#EXCERCISE 2- Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

#EXCERCISE 3- Write a Python program to iterate over dictionaries using for loops.

dictionary = {'x': 10, 'y': 20, 'z': 30}

for dictKey, dictValue in dictionary.items():
    print(dictKey, '->', dictValue)

#EXCERCISE 4- Write a Python script to generate and print a dictionary that contains a
#             number (between 1 and n) in the form (x, x*x).

n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x
print(d)

#EXCERCISE 5- Write a Python script to print a dictionary where the keys are numbers
#             between 1 and 15 (both included) and the values are the square of the keys.

d = dict()

for x in range(1, 16):
    d[x] = x ** 2
print(d)

#EXCERCISE 6- Write a Python script to merge two Python dictionaries.

firstDict = {'a': 100, 'b': 200}
secondDict = {'x': 300, 'y': 200}

d = firstDict.copy()
d.update(secondDict)

print(d)

#EXCERCISE 7- Write a Python program to iterate over dictionaries using for loops.
dictionary = {'Red': 1, 'Green': 2, 'Blue': 3}

for colorKey, value in dictionary.items():
    print(colorKey, 'corresponds to ', dictionary[colorKey])

#EXCERCISE 8- Write a Python program to sum all the items in a dictionary.

dictionary = {'data1': 100, 'data2': -54, 'data3': 247}

result = sum(dictionary.values())
print(result)

#EXCERCISE 9- Write a Python program to multiply all the items in a dictionary.

dictionary = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1
for key in dictionary:
    result = result * dictionary[key]

print(result)

#EXCERCISE 10- Write a Python program to remove a key from a dictionary.

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dictionary)

if 'a' in dictionary:
    del dictionary['a']

print(dictionary)

#EXCERCISE 11- Write a Python program to print a dictionary in table format.

dictionary = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for row in zip(*([key] + (value) for key, value in sorted(dictionary.items()))):
    print(*row)

#EXCERCISE 12- Write a Python program to count the values associated with a key in a dictionary.

student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(d['id'] for d in student))

print(sum(d['success'] for d in student))

#EXCERCISE 13- Write a Python program to convert a list into a nested dictionary of keys.

numberList = num_list = [1, 2, 3, 4]
newDict = current = {}

for name in num_list:
    current[name] = {}
    current = current[name]

print(newDict)

#EXCERCISE 14- Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sortedDict = {x: sorted(y) for x, y in num.items()}

print(sortedDict)

#EXCERCISE 15- Write a Python program to remove spaces from dictionary keys.

studentList = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ", studentList)

studentDict = {x.translate({32: None}): y for x, y in studentList.items()}

print("New dictionary: ", studentDict)

#EXCERCISE 16- Write a Python program to print a dictionary line by line.

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

for a in students:
    print(a)
    for b in students[a]:
        print(b, ':', students[a][b])

#EXCERCISE 17- Write a Python program to check if multiple keys exist in a dictionary.

student = {
'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

print(student.keys() >= {'class', 'name'})

print(student.keys() >= {'name', 'Alex'})

print(student.keys() >= {'roll_id', 'name'})

#EXCERCISE 18- Write a Python program to split a given dictionary of lists into lists of dictionaries.

def listOfDicts(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    result = [dict(zip(keys, v)) for v in vals]
    return result

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)

print("\nSplit said dictionary of lists into a list of dictionaries:")

print(listOfDicts(marks))

#EXCERCISE 19- Write a Python program to verify that all values in a dictionary are the same.

def valueCheck(students, n):
    result = all(x == n for x in students.values())
    return result

students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
print("Original Dictionary:")
print(students)
n = 12

print("\nCheck all are", n, "in the dictionary.")

print(valueCheck(students, n))
n = 10
print("\nCheck all are", n, "in the dictionary.")
print(valueCheck(students, n))

#EXCERCISE 20- Write a Python program to access dictionary key's element by index.

num = {'physics': 80, 'math': 90, 'chemistry': 86}

print("\nAccess the keys of the dictionary as a list:")
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])







