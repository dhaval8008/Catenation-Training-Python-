''' TASK FOUR: FUNCTIONS '''
''' QUESTION1- Write a program to reverse a string '''

mystr = "Dhaval"

print(mystr[::-1])

''' QUESTION2- Write a function that accepts a string and calculate the number of uppercase letters
and lowercase letters. '''




'''QUESTION3- Create a function that takes a list and returns a new list with unique elements of the
first list. '''




'''QUESTION4- Write a program that accepts a hyphen-separated sequence of words as input and
prints the words in a hyphen-separated sequence after sorting them alphabetically. '''
friends='charmi-sandip-romit-swarna-gauri'
 



'''QUESTION5- Write a program that accepts a sequence of lines as input and prints the lines after
making all characters in the sentence capitalized. '''

lines = []
while True:
    x = input()
    if x:
        lines.append(x.upper())
    else:
        break

for x in lines:
    print(x)

'''QUESTION6- Define a function that can receive two integral numbers in string form and compute
their sum and print it in console. '''




'''QUESTION7- Define a function that can accept two strings as input and print the string with
maximum length in console. If two strings have the same length, then the function should
print all strings line by line. '''




'''QUESTION8- Define a function which can generate and print a tuple where the value are square of
numbers between 1 and 20.'''
def numbers():
	
  
  

'''QUESTION9- Write a function called showNumbers that takes a parameter called limit. It should
print all the numbers between 0 and limit with a label to identify the even and odd numbers. '''
def showNumbers(limit):

    
    
    

''' QUESTION10- Write a program which can filter() to make a list whose elements are even number
between 1 and 20 ( both included) '''
ls1 = range(1,21) 
  


''' QUESTION11- Write a program which can map() and filter() to make a list whose elements are
square of even number in [1,2,3,4,5,6,7,8,9,10] '''




''' QUESTION12- Write a function to compute 5/0 and use try/except to catch the exceptions '''
def divide (x, y):
  
  
  

'''QUESTION13- Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce '''
import operator
from functools import reduce





'''QUESTION14- What is the output of the following codes: '''
def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)

output = 2

def a():
   try:
      f(x, 4)
   finally:
     print('after f')

   print('after f?')
   
a()

output- after f
