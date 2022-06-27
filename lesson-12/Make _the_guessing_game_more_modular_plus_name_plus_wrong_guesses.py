# Homework 12.5: Make the guessing game more modular
#
#Use functions to make the game more modular.
# Use functions to make the game more modular.
# Also try to add another while loop so the user can play many rounds of the game without having to re-run the program each time.
# Hint, the game would look something like this:
#
#while True:
#    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")
#
#    if selection == "A":
#        play_game()
#    elif selection == "B":
#        for score_dict in get_top_scores():
#            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
#    else:
#        break
#
#And you'll probably need three functions:
#   play_game()
#   get_score_list()
#   get_top_scores()

import datetime
import json
import random

# Funktion Score Liste öffnen
def get_score_list():
    with open("score_list_8.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

#print("Top scores: " + str(score_list))

# Funktion Top 3
def get_top3_score():
    # sort score_list --> Using a Lambda Function --> and sort by attempts
    # https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
    score_list = get_score_list()
    sort_score_list = sorted(score_list, key=lambda item: item["attempts"])[0:3]
    return sort_score_list

# Funktion Spiel spielen + Eingabe Namen
def play():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    name = input("What's your name? ")
    wrong_guesses = []

    while True:

        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses": wrong_guesses})
            with open("score_list_8.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print("Falsche Zahlen: " + str(wrong_guesses))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append(guess)

# Spiel spielen inkl. Namen

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play()
    elif selection.upper() == "B":
        for score_dict in get_top3_score():
            print(str(score_dict["attempts"]) + " attemts, date: " + score_dict.get("date") + ", Player: " + score_dict.get("name") + ", Wrong guesses: " + str(score_dict.get("wrong_guesses")))
    else:
        break
