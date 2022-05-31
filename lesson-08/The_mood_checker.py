#For the first exercise let's continue the mood checking program from before. Ask user to tell you what mood s/he is in:
#if the mood is "happy", the program should print out "It is great to see you happy!"
#if the mood is "nervous", respond with "Take a deep breath 3 times.". Use elif to enter more if statements: elif mood == "nervous":.
#Make up responses also for "sad", "excited" and "relaxed".
#The last option should be the normal else, which responds with "I don't recognize this mood".

leerzeichen = " "
name = input("What's your name? ")
mood = input("What's your mood totay," + leerzeichen + name + "? ")

if mood == "happy":
    print(name + " " + ", it is great to see you happy")
elif mood == "nervous":
    print(name + " " + ", take a deep breath 3 times.")
elif mood == "excited":
    print(name + " " + ", it is so exiting!")
elif mood == "sad":
    print(name + " " + ", I'm so sad totay.")
elif mood == "relaxed":
    print(name + " " + ", It's going to be chill today.")
else:
    print(name + " " + ", I don't recognize this mood.")