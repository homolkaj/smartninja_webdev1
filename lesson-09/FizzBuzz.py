# Hausübung 9.2 - FizzBuzz
# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal).
# In case the number is divisible with 3, it prints "fizz" instead of the number.
# If the number is divisible with 5, it prints "buzz".
# If it's divisible with both 3 and 5, it prints "fizzbuzz".

print("Welcome to Fizzbuzz.")

while True:
    question = input("Do you want to play this game (y/n)? ")

    if question == "n":
        print("Goodbye.")
        break
    elif question == "y":
        a = input("Enter a number between 1 and 100: ")
        b = int(a)
        # for b in range(1, 101):
        for b in range(1, b+1): # "b+1" bedeutet, dass wenn z.B. die Zahl 10 eingegeben wird, nach dem 10ten Lauf abgebrochen wird.
        # falsche Reihenfolge
        #   if b % 3 == 0:
        #       print("fizz")
        #   elif b % 5 == 0:
        #       print ("buzz")
        #   elif b % 3 == 0 and b % 5 == 0:
        #        print
           if b % 3 == 0 and b % 5 == 0:
               print("fizzbuzz")
           elif b % 3 == 0:
               print ("fizz")
           elif b % 5 == 0:
               print ("buzz")
           else:
                print (b)
    else:
        print("Okay, let's try again!")