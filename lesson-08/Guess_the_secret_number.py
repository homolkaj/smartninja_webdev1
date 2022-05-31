#Your task is to create this game:

#    First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.
#    Then the user has to find out what this number is (using input()). Store user's guess in a variable called guess.
#    Check if your secret is equal to user's guess.
#    If the user's guess is wrong, let him/her know that (use print() and if/else).
#    If the user's guess is correct, congratulate him/her.

# int() function - change a string into a number
name = input("Your Name: ")
secret = 10
guess = int(input("Guess your secret number - between 1 and 15" + " - " + name + ": "))

if secret == guess:
    print("Your secret number is correct!")
else:
    print("Try again")