#Excercise 1- Write a python program to calculate the lenght of a string.

user_string = str(input("Enter any string: "))

stringLenght = (len(user_string))

print(f"You string has: {stringLenght} characters.")

#Excercise 2: Write a Python program to count the number of characters (character frequency) in a string.

def charFrequency(str1):
    dictionary = {}
    for n in str1:
        keys = dictionary.keys()
        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    return dictionary

print(charFrequency("google.com"))


#Excercise 3- Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
#             If the string length is less than 2, return the empty string instead.

def string_both_ends(str):
    if len(str) < 2:
        return ""
    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#Excercise 4- Write a Python program to get a string from a given string where all occurrences of
#             its first char have been changed to '$', except the first char itself.

def changeChar(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1
print(changeChar('restart'))

#Excercise 5- Write a Python program to get a single string from two given strings,
#            separated by a space and swap the first two characters of each string.

def charsMixUp(A, B):
    new_A = B[:2] + A[2:]
    new_B = A[:2] + B[2:]
    return new_A + ' ' + new_B
print(charsMixUp('abc', 'xyz'))

#Excercise 6- Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less
# than 3, leave it unchanged.

def addString(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1
print(addString('ab'))
print(addString('abc'))
print(addString('string'))

#Excercise 7- Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def notPoor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1
print(notPoor('The lyrics are not that poor!'))
print(notPoor('The lyrics are poor!'))

#Excercise 8- Write a Python function that takes a list of words and return the
#              longest word and the length of the longest one.

def findLongestWord(wordsList):
    wordLen = []
    for n in wordsList:
        wordLen.append((len(n), n))
    wordLen.sort()
    return wordLen[-1][0], wordLen[-1][1]
result = findLongestWord(["PHP", "Exercises", "Backend"])
print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])

#Excercise 9- Write a Python program to remove the nth index character from a nonempty string.
def removeChar(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part
print(removeChar('Python', 0))  
print(removeChar('Python', 3))  
print(removeChar('Python', 5))

#Excercise 10- Write a Python program to change a given string to a newly string
#              where the first and last chars have been exchanged.
def changeString(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
print(changeString('abcd'))   
print(changeString('12345'))

#Excercise 11- Write a Python program to remove characters that have odd index values in a given string.
def oddValuesString(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
print(oddValuesString("abcdef"))
print(oddValuesString("python"))

#Excercise 12- Write a Python program to count the occurrences of each word in a given sentence.
def wordCount(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(wordCount('The quick brown fox jumps over the lazy dog.'))

#Excercise 13- Write a Python script that takes input from the user and displays
#              that input back in upper and lower cases.

userInput = input("What's your favorite language? ")
print("My favorite language is", userInput.upper())
print("My favorite language is", userInput.lower())

#Excercise 14- Write a Python program that accepts a comma-separated sequence of words
#              as input and prints the distinct words in sorted form (alphanumerically).

items = input("Input comma-separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#Excersice 15- Write a Python program to remove a newline in Python.

str1 = "Python Exercises\n"
print(str1)
print(str1.rstrip())

#Excercise 16- Write a Python program to format a number with a percentage.

x = 0.25
y = -0.25
print()
print("Original Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x))
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y))
print()

#Excercise 17- Write a Python function to get a string made of 4 copies of the last two
#              characters of a specified string (length must be at least 2).
def insertEnd(str):
    sub_str = str[-2:]
    return sub_str * 4
print(insertEnd('Python'))
print(insertEnd('Exercises'))

#Excercise 18- Write a Python function to get a string made of the
#first three characters of a specified string. If the length of the string is less than 3, return the original string.

def firstThree(str):
    if len(str) > 3:
        return str[:3]
    else:
        return str
print(firstThree('ipy'))
print(firstThree('python'))
print(firstThree('py'))

#Excercise 19- Write a Python function to reverse a string if its length is a multiple of 4.

def reverseString(str1):
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))
    return str1
print(reverseString('abcd'))
print(reverseString('python'))

#Excercise 20- Write a Python function to convert a given string to all uppercase if it contains
#              at least 2 uppercase characters in the first 4 characters.

def toUppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1
print(toUppercase('Python'))
print(toUppercase('PyThon'))



