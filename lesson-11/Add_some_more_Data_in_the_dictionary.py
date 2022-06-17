# Hausübung 11.1
# Add some more data in the dictionary
# For now our game only stores the number of attempts and the date.
# Let's also store the name of the player and the secret number in each game.

import random, json
# we now want to incorporate the time of the high score
# into the high score list
# for this we need the datetime library
import datetime

name = input("What's your name? ")
secret = random.randint(1, 30)
attempts = 0

with open("score_list_3.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    # we don't sort the results anymore

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", player: " + score_dict.get("name"))
print("Top scores: " + str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        # we save the high score in a dictionary
        score_data = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": name}
        # and this dictionary we store in a list
        score_list.append(score_data)

        with open("score_list_3.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")