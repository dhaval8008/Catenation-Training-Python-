'''1.Write a program in Python to perform the following operation:

● If a number is divisible by 3 it should print “Consultadd” as a string
● If a number is divisible by 5 it should print “c” as a string
● If a number is divisible by both 3 and 5 it should print “Consultadd
Python Training” as a string.'''



x=eval(input("Enter the Number"))
if x%3==0:
    if ((x % 3 == 0)and (x % 5 ==0)):
        print("Consultadd Python Training")
    elif x % 3 == 0:
        print("Consultadd")
    elif x % 5== 0:
        print("C")




'''2. Write a program in Python to perform the following operator based task:

● Ask user to choose the following option first:

○ If User Enter 1 - Addition
○ If User Enter 2 - Subtraction
○ If User Enter 3 - Division
○ If USer Enter 4 - Multiplication
○ If User Enter 5 - Average
● Ask user to enter the 2 numbers in a variable for first and second for the
first 4 options mentioned above.
● Ask user to enter two more numbers as first and second2 for
calculating the average as soon as user choose an option 5.
● At the end if the answer of any operation is Negative print a statement
saying “NEGATIVE”
● NOTE: At a time user can perform one action at a time.'''


a = int(input("Enter the choice 1(Addition), 2(Subtraction), 3(Division), 4(Multiplication), 5(Average)"))
if a==1 or a==2 or a==3 or a ==4:
    first=eval(input("Enter the First Number"))
    second = eval(input("Enter the second Number"))
    if a==1:
        print(first+second)
    if a==2:
        print(first-second)
    if a==3:
        print(first*second)
    if a==4:
        print(first/second)

elif a==5:
    first1=eval(input("Enter the first1 Number"))
    second1=eval(input("Enter the second2 Number"))
    Average = (first1+second1)/2
    print(Average)
elif a<0:
    print("Negative")
'''3. Write a program in Python to implement the given flowchart:


a=10
b=20
c=30
avg=(a+b+c)/3
print("Avg=", avg)
if avg>a and avg>b and avg>c:
    print("Avg is higher than a,b,c")
elif avg>a and avg>b:
    print("Avg greater than a and b")
elif avg>a and avg>c:
     print("Avg is higher than a,c")
elif avg>b and avg>c:
    print("Avg is higher than b,c")
elif avg>a:
    print("avg is just greater than a")
elif avg>b:
    print("avg is just greater than b")
elif avg>c:
    print("avh is just greater than c")
    
'''4. Write a program in Python to break and continue if the following cases
occurs:

● If user enters a negative number just break the loop and print “It’s Over”
● If user enters a positive number just continue in the loop and print
“Good Going”'''

while True:
    a = int(input("Enter the Value, (-1) to Exit"))
    if a<0:
        print("Its over")
        break
    else:
        print("Good Going")
        continue
    
'''5.  Write a program in Python which will find all such numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200.'''

for x in range (2000,3201):
    if x % 7 == 0 and x % 5 != 0:
        print(x)


'''6. What is the output of the following code examples?'''

#1. TypeError: 'int' object is not iterable
#2.  0
#   error
#   1
#   error
#   2
#   error (Continously running)

#3. 0
#    1
#    2
#    3
#    4

'''7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement'''

for i in range(6):
    if (i == 3 or i == 6):
        continue
    print(i)

'''8. Write a program that accepts a string as an input from user and calculate the
number of digits and letters.
Expected output: consul12'''

x = input("Enter a string: ")
d = l = 0
for i in x:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
    else:
        pass
print("# of Letters: ",l)
print("# of Digits: ",d)
Letters 6
Digits 2


'''Read the two parts of the question below:
● Write a program such that it asks users to “guess the lucky number”. If the
correct number is guessed the program stops, otherwise it continues forever.
● Modify the program so that it asks users whether they want to guess again
each time. Use two variables, ‘number’ for the number and ‘answer’ for the
answer to the question whether they want to continue guessing. The
program stops if the user guesses the correct number or answers “no”. ( The
program continues as long as a user has not answered “no” and has not
guessed the correct number)'''

#Part1
while True:
    x = int(input("Guess the Lucky Number:"))
    y = 20
    if x==y:
        break
    else:
        ans = str(input("Try Again"))
    

#Part2
while True:
    x = int(input("Guess the Lucky Number:"))
    y = 20
    if x==y:
        break
    else:
        ans = str(input("Try Again? (yes/no):"))
        if ans == 'no' :
            break
        else:
            continue





'''10. Write a program that asks five times to guess the lucky number. Use a while loop
and a counter, such as
counter=1

While counter &lt;= 5:
print(“Type in the”, counter, “number”
counter=counter+1

The program asks for five guesses (no matter whether the correct number was
guessed or not). If the correct number is guessed, the program outputs “Good
guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints
“Game over!”.'''

#answer for 10 and 11

c = 1
y = 82

while c <= 5:
    x = int(input("Guess the Lucky Number:"))
    c = c + 1
    if x==y:
        print("Good Guess")
        break
    else:
        print("Try Again")
