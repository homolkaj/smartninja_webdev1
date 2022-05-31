#Write a program that does the basic arithmetic operations:
#
#    addition (+),
#    subtraction (-),
#    multiplication (*),
#    and division (/).

#Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").

#Then use if/elif/else statements to do the right operation.

name = input("Your name: ")
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
c = input(name + ", chose +, -, * or / for your calculation: ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("Not the correct operator! Try again, " + name + ".")