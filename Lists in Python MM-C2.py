#EXCERCISE 1- Write a Python program to sum all the items in a list.
def sumList(items):
    sumNumbers = 0
    for x in items:
        sumNumbers += x
    return sumNumbers
print(sumList([1, 2, -8]))

#EXCERCISE 2- Write a Python program to multiply all the items in a list.
def multiplyList(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiplyList([1, 2, -8]))

#EXCERCISE 3- Write a Python program to get the largest number from a list.
def maxNumInList(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(maxNumInList([1, 2, -8, 0]))

#EXCERCISE 4- Write a Python program to get the smallest number from a list.
def smallestNumInList(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
print(smallestNumInList([1, 2, -8, 0]))

#EXCERCISE 5- Write a Python program to count the number of strings from a given list of strings.
#             The string length is 2 or more and the first and last characters are the same.

def matchingWords(words):
    counter = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
    return counter
print(matchingWords(['abc', 'xyz', 'aba', '1221']))

#EXCERCISE 6- Write a Python program to get a list, sorted in increasing order by the last
#             element in each tuple from a given list of non-empty tuples.

def last(n):
    return n[-1]

def sortListLast(tuples):
    return sorted(tuples, key=last)
print(sortListLast([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#EXCERCISE 7- Write a Python program to remove duplicates from a list.

randomList = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
duplicatedItems = set()
uniqueItems = []

for x in randomList:
    if x not in duplicatedItems:
        uniqueItems.append(x)
        duplicatedItems.add(x)
print(duplicatedItems)

#EXCERCISE 8- Write a Python program to check if a list is empty or not.

emptyList = []
if not emptyList:
    print("List is empty")

#EXCERCISE 9- Write a Python program to clone or copy a list.

randomList = [10, 22, 44, 23, 4]
newList = list(randomList)

print(randomList)
print(newList)

#EXCERCISE 10- Write a Python program to find the list of words that are longer than n from a given list of words.
def longWords(n, str):
    wordLen = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            wordLen.append(x)
    return wordLen
print(longWords(3, "The quick brown fox jumps over the lazy dog"))

#EXCERCISE 11- Write a Python function that takes two lists and returns True if they have at least one common member.
def commonData(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(commonData([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(commonData([1, 2, 3, 4, 5], [6, 7, 8, 9]))

#EXCERCISE 12- Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

print(color)

#EXCERCISE 13- Write a Python program to find the second smallest number in a list.
def secondSmallest(numbers):
    if len(numbers) < 2:
        return
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return
    duplicatedItems = set()
    uniqueItems = []
    for x in numbers:
        if x not in duplicatedItems:
            uniqueItems.append(x)
            duplicatedItems.add(x)
    uniqueItems.sort()
    return uniqueItems[1]
print(secondSmallest([1, 2, -8, -2, 0, -2]))
print(secondSmallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))

#EXCERCISE 14- Write a Python program to print the numbers of a specified list after removing even numbers from it.
numbers = [7, 8, 120, 25, 44, 20, 27]
numbers = [x for x in numbers if x % 2 != 0]

print(numbers)

#EXCERCISE 15- Write a Python program to shuffle and print a specified list.
from random import shuffle

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)

print(color)

#EXCERCISE 16- Write a Python program to generate and print a list of the first and last
#              5 elements where the values are square numbers between 1 and 30 (both included).

def printValues():
    myList = list()
    for i in range(1, 21):
        myList.append(i ** 2)
    print(myList[:5])
    print(myList[-5:])
printValues()

#EXCERCISE 17- Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1, 2, 3])))

#EXCERCISE 18- Write a Python program to calculate the difference between the two lists

list1 = [1, 3, 5, 7, 9]

list2 = [1, 2, 4, 6, 7, 8]

firstDifference = list(set(list1) - set(list2))
secondDifference = list(set(list2) - set(list1))

totalDifference = firstDifference + secondDifference

print(totalDifference)

#EXCERCISE 19- Write a Python program to access the index of a list.

numbers = [5, 15, 35, 8, 98]

for numberIndex, numberValue in enumerate(numbers):
    print(numberIndex, numberValue)

#EXCERCISE 20- Write a Python program to convert a list of characters into a string.

list = ['a', 'b', 'c', 'd']

str1 = ''.join(list)

print(str1)





