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
