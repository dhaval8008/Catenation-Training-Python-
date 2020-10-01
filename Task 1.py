"""TASK ONE: NUMBERS AND VARIABLES
Create three variables in a single line and assign different values to them and
make sure their data types are invited differently. Like one is int, another one is float
and last one is string."""


    Last login: Tue Sep 29 02:33:42 on console
dhavaladhvaryu@Dhavals-Air ~ % python 

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Jun  5 2020, 22:59:21) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a,b,c = 2,3.5,"Dhaval"
>>> print (type(c))
<type 'str'>



'''2. Create a variable of value type complex and swap it with another variable
whose value is an integer.'''

Last login: Thu Oct  1 10:47:33 on ttys000
dhavaladhvaryu@Dhavals-Air ~ % python3
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a=50+20j
>>> print (type(a))
<class 'complex'>
>>> b=80
>>> print(type(b))
<class 'int'>
>>> a=b
>>> print(a)
80
>>> 





'''3. Swap two numbers using third variable as result name and do the same task
without using any third variable'''


>>> a=30
>>> b=40
>>> end_value =a
>>> b= end_value
>>> print(a,b)
30 30
>>> #witout using variable 
>>> a,b=b,a
>>> print(a,b)
30 30
>>> 



'''4. Write a program to print the value given by the user by using both Python 2.x
and Python 3.x Version.'''

enter_value =input("Enter value 2.x")

'''5. Write a program to complete the task given below:

● Ask user to enter any 2 numbers in between 1-10 and add both of
them to another variable call z.
● Use z for adding 30 into it and print the final result by using
variable result.'''


X= int(input("enter the first value"))
Y= int(input("enter the first value"))
Z= X+Y
Z= Z+30
print(Z)

'''6. Write a program to check the data type of the entered values. HINT: Printed
output should say - The input value data type is : int/float/string/etc'''

a,b,c = 12,5.80,"Dhaval"
print(type(b))

