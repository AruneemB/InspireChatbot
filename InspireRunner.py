#Import various tools needed for Inspire
import random
import time

from InspireDiscussantPrototype import *
from InspireCalculator import *
from InspireEntertainer import *

'''          _____                    _____                    _____                    _____                    _____                    _____                    _____
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \
        /::\    \                /::\____\                /::\    \                /::\    \                /::\    \                /::\    \                /::\    \
        \:::\    \              /::::|   |               /::::\    \              /::::\    \               \:::\    \              /::::\    \              /::::\    \
         \:::\    \            /:::::|   |              /::::::\    \            /::::::\    \               \:::\    \            /::::::\    \            /::::::\    \
          \:::\    \          /::::::|   |             /:::/\:::\    \          /:::/\:::\    \               \:::\    \          /:::/\:::\    \          /:::/\:::\    \
           \:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \               \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \
           /::::\    \      /:::/ |::|   |            \:::\   \:::\    \      /::::\   \:::\    \              /::::\    \      /::::\   \:::\    \      /::::\   \:::\    \
  ____    /::::::\    \    /:::/  |::|   | _____    ___\:::\   \:::\    \    /::::::\   \:::\    \    ____    /::::::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \
 /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\____\  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \
/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\/::\   \:::\   \:::\____\/:::/  \:::\   \:::|    |/::\   \/:::/  \:::\____\/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\
\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::|____|\:::\  /:::/    \::/    /\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /
 \:::\/:::/    / \/____/  \/____/ |::| /:::/    /  \:::\   \:::\   \/____/  \/_____/\:::\/:::/    /  \:::\/:::/    / \/____/  \/____|:::::\/:::/    /  \:::\   \:::\   \/____/
  \::::::/    /                   |::|/:::/    /    \:::\   \:::\    \               \::::::/    /    \::::::/    /                 |:::::::::/    /    \:::\   \:::\    \
   \::::/____/                    |::::::/    /      \:::\   \:::\____\               \::::/    /      \::::/____/                  |::|\::::/    /      \:::\   \:::\____\
    \:::\    \                    |:::::/    /        \:::\  /:::/    /                \::/____/        \:::\    \                  |::| \::/____/        \:::\   \::/    /
     \:::\    \                   |::::/    /          \:::\/:::/    /                  ~~               \:::\    \                 |::|  ~|               \:::\   \/____/
      \:::\    \                  /:::/    /            \::::::/    /                                     \:::\    \                |::|   |                \:::\    \
       \:::\____\                /:::/    /              \::::/    /                                       \:::\____\               \::|   |                 \:::\____\
        \::/    /                \::/    /                \::/    /                                         \::/    /                \:|   |                  \::/    /
         \/____/                  \/____/                  \/____/                                           \/____/                  \|___|                   \/____/
'''

def inspireIntro():
    #Introductions class used as a blueprint for Inspire
    class Introductions:
        def __init__(self, greetings): #Uses the parameter in order to randomly select a greeting and add it as a string
            greetingsStr = ""
            self.greetings = greetingsStr.join(random.choice(greetings))
        def __str__(self):
            return f"{self.greetings}" #Returns greeting for a casual introduction

    #Array with various casual greetings, used as paramteters for Inspire's introduction feature
    introductoryGreetings = ["Hi!", "Hi there!", "Hey!", "Hey there!", "Hello!", "Hello there!", "What's up!"]
    #Instance of the Introductions class used to introduce Inspire to the user
    inspireIntroductions = Introductions(introductoryGreetings)
    #Prints out the casual introduction, using the .sleep() function to seem more natural in text
    print(inspireIntroductions)
    time.sleep(0.5)

    #Asks for the user's name, concatenating it into its response, then asks the user if they want a breakdown of what it can do
    userName = input("Looks like you're new around here, what's your name?\n")
    time.sleep(0.5)
    print("Nice to meet you, " + userName + ", my name is Inspire, a simple chatbot.")
    userBreakDownPref = input("Want a quick breakdown of what I can do?\n")

    #String containing the breakdown if the user does request for it
    #Triple quotation marks allows for a multiline String
    inspireBreakdown = """I am a basic chatbot that can complete various simple tasks. Here's a simple breakdown of what I can do:\n
    - Discussant: engaging in simple talk with you.\n
    - Calculator: performing basic mathematical calculations for you.\n
    - Entertainer: playing simple games with you.\n

        To access each feature, simply type either discussant, calculator, or entertainer to view what tools I have to fit your needs! \n
    Let me know what you need, and I can see what I can do!"""

    #Lists containing what the user could say, as well as booleans to check if the user needs a breakdown or if their answer is unclear
    userPossibleAffirmations = ["y", "yes", "sure", "alright", "affirmative"]
    userPossibleNegations = ["n", "no", "nope", "not", "negative"]
    userBreakDownNeeded = False
    userUnclear = True

    for val in range(len(userPossibleAffirmations)): #Checks the user's reply with each element in the possible affirmative responses
        if userBreakDownPref.lower() in userPossibleAffirmations[val]: #If reply matches the possible affirmation, user breakdown is needed and their response is clear
            userBreakDownNeeded = True
            userUnclear = False
            break #Breaks the loop
        elif userPossibleAffirmations[val] in userBreakDownPref.lower(): #If possible affirmation matches reply, user breakdown is needed and their response is clear
            userBreakDownNeeded = True
            userUnclear = False
            break #Breaks the loop
    for val in range(len(userPossibleNegations)): #Checks the user's reply with each element in the possible negative responses
        if userBreakDownPref.lower() in userPossibleNegations[val]: #If reply matches possible negation, user breakdown is not needed and their response is clear
            userUnclear = False
            break #Breaks the loop
        elif userPossibleNegations[val] in userBreakDownPref.lower():
            userUnclear = False
            break #Breaks the loop

    #Uses the boolean values to provide a proper response to the user
    if userUnclear == False: #Will immediately answer the user if their answer is clear
        if userBreakDownNeeded == True:
            print(inspireBreakdown)
        else:
            print("Ok, tell me what you need me to do!")
    else: #Will ask the user if their answer is not clear
        while userBreakDownPref != "yes" or userBreakDownPref != "no": #Will continue to ask the user if their answer is still not clear
            print("Sorry, your response was unclear. Try answering with the words 'yes' or 'no' in lowercase.")
            userBreakDownPref = input()
            if userBreakDownPref == "yes":
                print(inspireBreakdown)
                break
            elif userBreakDownPref == "no":
                print("Ok, tell me what you need me to do!")
                break
def inspireRunner():
    userActive = True
    userInput = input("")
    while userActive:
        if "quit" in userInput.lower():
            print("It was great spending time knowing you, " + userName + ". Hope to meet once again sometime soon!")
            userActive = False
            break
        elif userInput.lower() in "exit":
            userActive = False
            break
        else:
            userActive = True

        if "discussant" in userInput.lower():
            discussantRunner()
            userInput = input("Would you like to try another functionality (answer discussant, calculator, or entertainer)? If you want to end this session, type 'quit.' \n")
        elif "calculator" in userInput.lower():
            calculatorRunner()
            userInput = input("Would you like to try another functionality (answer discussant, calculator, or entertainer)? If you want to end this session, type 'quit.' \n")
        elif "entertainer" in userInput.lower():
            entertainerRunner()
            userInput = input("Would you like to try another functionality (answer discussant, calculator, or entertainer)? If you want to end this session, type 'quit.' \n")
        else:
            userInput = str(input("Sorry, your response was unclear. Try typing either 'discusstant', 'calculator', or 'entertainer' to access any of my features! If you want to end this session, type 'quit.' \n"))


inspireIntro()
inspireRunner()
