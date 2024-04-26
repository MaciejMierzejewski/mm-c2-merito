# EXCERCISE 1- Write a  Python program to find those numbers which are divisible by 7 and multiples of 5,
#             between 1500 and 2700 (both included).
list = []

for x in range(1500,2701):
  if (x % 7 == 0 ) and (x % 5 == 0):
    list.append(str(x))
print(','.join(list))

# EXCERCISE 2- Write a Python program to guess a number between 1 and 9.

import random
targetNum, guessNum = random.randint(1, 10), 0
while targetNum != guessNum:
  guessNum = int(input('Guess a number between 1 and 10 until you get it right : '))

print('Well guessed!')

# EXCERCISE 3- Write a  Python program that accepts a word from the user and reverses it.

word = input("Input a word to reverse: ")

for char in range(len(word) -1, -1, -1):
  print(word[char], end="")

print("\n")

# EXCERCISE 4- Write a Python program to count the number of even and odd numbers in a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

countOdd = 0
countEven = 0

for x in numbers:
  if not x % 2:
    countEven += 1
  else:
    countOdd += 1

print("Number of even numbers:", countEven)
print("Number of odd numbers:", countOdd)

# EXCERCISE 5- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for x in range(6):
  if (x == 3 or x == 6):
    continue
  print(x, end=' ')
print("\n")

# EXCERCISE 6- Write a Python program to get the Fibonacci series between 0 and 50.

x, y = 0, 1

while y < 50:
  print(y)
  x, y = y, x + y

# EXCERCISE 7- Write a Python program that iterates the integers from 1 to 50.For multiples of three print
#              "Fizz" instead of the number and for multiples of five print "Buzz".
#             For numbers that are multiples of three and five, print "FizzBuzz".

for fizzbuzz in range(51):
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
    continue

  elif fizzbuzz % 3 == 0:
    print("fizz")
    continue

  elif fizzbuzz % 5 == 0:
     print("buzz")
     continue

  print(fizzbuzz)

# EXCERCISE 8- Write a Python program that accepts a sequence of lines (blank line to terminate)
#              as input and prints the lines as output (all characters in lower case).

lines = []

while True:
  l = input()

  if l:
    lines.append(l.upper())
  else:
    break;

for l in lines:
  print(l)

# EXCERCISE 9- Write a Python program that accepts a string and calculates the number of digits and letters.

userString = input("Input a string: ")

digits = letters = 0
for characters in userString:
  if characters.isdigit():
    digits = digits + 1
  elif characters.isalpha():
    letters = letters + 1
  else:
    pass

print("Letters:", letters)
print("Digits:", digits)

# EXCERCISE 10- Write a Python program to check the validity of passwords input by users.

import re

password = input("Input your password: ")
x = True
while x:
  if (len(password) < 6 or len(password) > 12):
    break
  elif not re.search("[a-z]", password):
    break
  elif not re.search("[0-9]", password):
    break
  elif not re.search("[A-Z]", password):
    break
  elif not re.search("[$#@]", password):
    break
  elif re.search("\s", password):
    break
  else:
    print("Valid Password")
    x = False
    break
if x:
  print("Not a Valid Password")

# EXCERCISE 11- Write a Python program to find numbers between 100 and 400 (both included) where each
#              digit of a number is an even number. The numbers obtained should be printed in a
#               comma-separated sequence.

items = []
for i in range(100, 401):
  string = str(i)

  if (int(string[0]) % 2 == 0) and (int(string[1]) % 2 == 0) and (int(string[2]) % 2 == 0):
    items.append(string)

print(",".join(items))

# EXCERCISE 12- Write a Python program to calculate a dog's age in dog years.

humanAge = int(input("Input a dog's age in human years: "))

if humanAge < 0:
  print("Age must be a positive number")
  exit()

elif humanAge <= 2:
  dogAge = humanAge * 10.5

else:
  dogAge = 21 + (humanAge - 2) * 4  
  
print("The dog's age in dog's years is", dogAge)

# EXCERCISE 13- Write a Python program to check whether an alphabet is a vowel or consonant.

letter = input("Input a letter of the alphabet: ")

if letter in ('a', 'e', 'i', 'o', 'u'):
  print("%s is a vowel." % letter)

elif letter == 'y':
  print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")

else:
  print("%s is a consonant." % letter)

# Excercise 14- Write a Python program to convert a month name to a number of days.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

monthName = input("Input the name of Month: ")

if monthName == "February":
  print("No. of days: 28/29 days")
elif monthName in ("April", "June", "September", "November"):
  print("No. of days: 30 days")
elif monthName in ("January", "March", "May", "July", "August", "October", "December"):
  print("No. of days: 31 days")
else:
  print("Wrong month name")


# EXCERCISE 15- Write a Python program to sum two integers. However,
#              if the sum is between 15 and 20 it will return 20.

def sum(x, y):
  sum = x + y
  if sum in range(15, 20):
    return 20
  else:
    return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

# EXCERCISE 16- Write a Python program that checks whether a string represents an integer or not.

text = input("Input a string: ")

text = text.strip()
if len(text) < 1:
  print("Input a valid text")
else:
  if all(text[i] in "0123456789" for i in range(len(text))):
    print("The string is an integer.")
  elif (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
    print("The string is an integer.")
  else:
    print("The string is not an integer.")

# EXCERCISE 17- Write a Python program that reads two integers representing a
#              month and day and prints the season for that month and day.

month = input("Input the month (e.g. January, February etc.): ")

day = int(input("Input the day: "))
if month in ('January', 'February', 'March'):
  season = "winter"
elif month in ('April', 'May', 'June'):
  season = "spring"
elif month in ('July', 'August', 'September'):
  season = "summer"
else:
  season = "autumn"

if (month == "March") and (day > 19):
  season = "spring"
elif (month == "June") and (day > 20):
  season = "summer"
elif (month == "September") and (day > 21):
  season = "autumn"
elif (month == "December") and (day > 20):
  season = "winter"
print("Season is", season)


# EXCERCISE 18- Write a  Python program to display the sign of the
#              Chinese Zodiac for the given year in which you were born.


year = int(input("Input your birth year: "))
if (year - 2000) % 12 == 0:
  sign = 'Dragon'
elif (year - 2000) % 12 == 1:
  sign = 'Snake'
elif (year - 2000) % 12 == 2:
  sign = 'Horse'
elif (year - 2000) % 12 == 3:
  sign = 'Sheep'
elif (year - 2000) % 12 == 4:
  sign = 'Monkey'
elif (year - 2000) % 12 == 5:
  sign = 'Rooster'
elif (year - 2000) % 12 == 6:
  sign = 'Dog'
elif (year - 2000) % 12 == 7:
  sign = 'Pig'
elif (year - 2000) % 12 == 8:
  sign = 'Rat'
elif (year - 2000) % 12 == 9:
  sign = 'Ox'
elif (year - 2000) % 12 == 10:
  sign = 'Tiger'
else:
  sign = 'Hare'
print("Your Zodiac sign :", sign)


# EXCERCISE 19- Write a Python program to find the median of three values.

a = float(input("Input first number: "))

b = float(input("Input second number: "))

c = float(input("Input third number: "))    

if a > b:
  if a < c:
    median = a
  elif b > c:
    median = b
  else:
    median = c
else:
  if a > c:
    median = a
  elif b < c:
    median = b
  else:
    median = c
print("The median is", median)

# EXCERCISE 20- Write a  Python program to create the multiplication table (from 1 to 10) of a number.

n = int(input("Input a number: "))

for i in range(1, 11):
  print(n, 'x', i, '=', n * i)
