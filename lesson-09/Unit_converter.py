# Create a program that converts units. More specifically, kilometers into miles.

# Plan:
# The program greets user and describes what's the purpose of the program.
# The program asks user to enter number of kilometers.
# User enters the amount of kilometers.
# The program converts these kilometers into miles and prints them.
# The program asks user if s/he'd want to do another conversion.
# If yes, repeat the above process (except the greeting).
# If not, the program says goodbye and stops.

print("With this programm you can convert kilometers into miles.")

while True:
    conv_factor_miles = 0.621371
    #conv_factor_miles_type = print(type(conv_factor_miles))

    kilometer = input("Enter a number of kilometers: ")
    repl_kilometer = float(kilometer.replace(",", "."))
    miles = repl_kilometer * conv_factor_miles

    print(repl_kilometer, "kilometer correspond to",  miles, "miles.")

    question = input("Do you want to do a conversion again (y/n)?")

    if question == "n":
        print("Goodbye.")
        break
    else:
        print("Okay, let's try again!")