# Hausübung 11.3
# Add unsuccessful guesses into the dictionary For now our game only stores the number of attempts and
# the date. Let's also store the name of the player and the secret number in each game. During the game,
# collect user's unsuccessful guesses and then store them in the dictionary under the name "wrong_guesses". Now that
# we removed the score_list.sort() line (because it doesn't work with dictionaries in the list), we have to find
# another way to sort the scores. There are many ways how to do it. Use your imagination (and Google) and try to
# figure out at least one of them. :)

import random, json
# we now want to incorporate the time of the high score
# into the high score list
# for this we need the datetime library
import datetime


name = input("What's your name? ")
secret = random.randint(1, 30)
attempts = 0

with open("score_list_5.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    # we don't sort the results anymore

# sort score_list --> Using a Lambda Function --> and sort by attempts
# https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
sort_score_list = sorted(score_list, key=lambda item: item["attempts"])[0:3]

print("Top 3 players (attempts, date, player, worng guesses")

for score_dict in sort_score_list:
    print(str(score_dict["attempts"]) + " attemts, date: " + score_dict.get("date") + ", Player: " + score_dict.get("name") + ", wong guesses " + str(score_dict["wrong_guesses"]))
print("Top scores: " + str(sort_score_list))

wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        # we save the high score in a dictionary
        score_data = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses": wrong_guesses}
        # and this dictionary we store in a list
        score_list.append(score_data)

        with open("score_list_5.json", "w") as score_file:
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