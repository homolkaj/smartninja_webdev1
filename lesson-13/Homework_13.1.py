# Homework 13.1
# Let's make our program for basketball and football players a bit more useful.
# Add an option that a user can enter data (via input()) and at the end of the
# program the data gets saved in a text file.
# Hint: you can easily convert object into a dictionary via the in-built __dict__ method.
# Try this in your program: lebron.__dict__ (note that there are 2 underscores on each side).

import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

if __name__=="__main__":

    with open("Football_Players.json", "r", encoding="utf-8") as f:
        f_load = json.loads(f.read())
    with open("Basketball_Players.json", "r", encoding="utf-8") as b:
        b_load = json.loads(b.read())

    while True:

        selection = input("Enter A) for a Basketball Player, B) for a Football Player, C) to see the values, or D) quit? ")

        if selection.upper() == "A":
            # Basketball Player
            print("Basketball Player")

            b_player = BasketballPlayer(input("first_name: "), input("last_name: "), int(input("height_cm: ")),
                                        int(input("weight_kg: ")), float(input("points: ")), float(input("rebounds: ")),
                                        float(input("assists: ")))

            print(b_player.__dict__)
            print(b_player.first_name)
            print(b_player.height_cm)

            # converting kg to lbs
            print(str(b_player.weight_kg) + " kg, " + str(b_player.weight_to_lbs()) + " lbs")

            # wirte values in file
            with open("Basketball_Players.json", "w", encoding="utf-8") as b_players_list_file:
                b_players_list_file.write(json.dumps(b_player.__dict__))

        elif selection.upper() == "B":
            # Football player
            print("Football Player")
            f_player = FootballPlayer(input("first_name: "), input("last_name: "), int(input("height_cm: ")),
                                      int(input("weight_kg: ")), int(input("goals: ")), int(input("yellow_cards: ")),
                                      int(input("red_cards ")))

            print(f_player.__dict__)
            # converting kg to lbs
            print(str(f_player.weight_kg) + " kg, " + str(f_player.weight_to_lbs()) + " lbs")
            # wirte values in file
            with open("Football_Players.json", "w", encoding="utf-8") as f_players_list_file:
                f_players_list_file.write(json.dumps(f_player.__dict__))

        elif selection.upper() == "C":
            # File lesen uns ausgeben
            print("Football Players: " + str(f_load))
            # File lesen uns ausgeben
            print("Basketball Players: " + str(b_load))

        else:
            break
