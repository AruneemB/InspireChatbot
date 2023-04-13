import random
import time

def entertainerNumGuesser():
    #Introduces the user to the minigame, explaining the rules and using the time.sleep() function to provide natural pause
    print("Welcome to the number guesser!")
    time.sleep(0.5)
    print("Choose a range from which you have to guess a mystery number that I will randomly select... ")
    time.sleep(0.5)

    #Asks the user what two numbers they would like to use for their min and max values for their range, saves it for later
    minVal = int(input("Enter a minimum value for your range: \n"))
    maxVal = int(input("Enter a maximum value for your range: \n"))

    #Randomly selects a number from the range determined by the min and max values provided by the user
    randomNum = random.randint(minVal, maxVal)

    #Variables saving the user's attempts at guessing and their penalty points gained from wrong guesses (also tracks how many attempts)
    userGuess = 0
    userPenalty = 0

    #Asks the user to make an attempt at guessing the random number
    userGuess = int(input("Enter a number between " + str(minVal) + " and " + str(maxVal) + ": "))

    #While the user's guess is incorrect, runs through series of if and elif statements
    #Each statement customed to help guide the user towards the right choice
    #Will award a penalty point for each attempt that is within the range and not the right number
    while(userGuess != randomNum):
        if(userGuess > maxVal):
            print(str(userGuess) + " is higher than maximum value of " + str(maxVal) + " and is thus invalid.")
            time.sleep(0.5)
            userGuess = int(input("Guess a different number: \n"))
        elif(userGuess < minVal):
            print(str(userGuess) + " is lower than minimum value of " + str(minVal) + " and is thus invalid.")
            time.sleep(0.5)
            userGuess = int(input("Guess a different number: \n"))
        elif(userGuess > randomNum):
            userPenalty = userPenalty + 1
            userGuess = int(input(str(userGuess) + " is too high, guess lower! \n"))
        elif(userGuess < randomNum):
            userPenalty = userPenalty + 1
            userGuess = int(input(str(userGuess) + " is too low, guess higher! \n"))

    #Once the loop is broken when the user guesses correctly, one more penalty point is awarded for that final guess
    #Tells the user that they got the correct number and gives how many attempts were needed to get the correct guess
    if(userGuess == randomNum):
        userPenalty = userPenalty + 1
        print(str(userGuess) + " is the correct number!")
        time.sleep(0.5)
        print("It took you " + str(userPenalty) + " attempts to guess the number correctly.")
        userGuess = 0

    time.sleep(0.5)
    #If and elif statement chain determining what custom response to provide based on the number of attempts towards a guess were made
    if(userPenalty == 0):
        print("Phenomenal work! You aced it!")
    elif(userPenalty <= 3):
        print("Almost perfect! But can you ace it?")
    elif(userPenalty <= 5):
        print("That was really close!")
    elif(userPenalty <= 10):
        print("Close, but you have some room to improve.")
    elif(userPenalty <= 15):
        print("That was pathetic.")
def entertainerDice():
    #Initiates variables to hold what the user and Inspire roll, as well as how many times either win
    userRoll = 0
    InspireRoll = 0
    userWins = 0
    InspireWins = 0

    #Initiates a variable to hold the user input(if they want to quit or keep playing)
    userQuit = ""

    #Converts all characters into lowercase through the casefold() function in order to properly compare
    while "quit" not in userQuit.casefold():
        userQuit = str(input("Enter 'roll' to roll a die, or quit to stop. \n"))
        userRoll = random.randint(1,6)
        print("Your roll: " + str(userRoll))
        InspireRoll = random.randint(1,6)
        print("My roll: " + str(InspireRoll))

        if userRoll > InspireRoll:
            print("You won!")
            userWins += 1
        elif userRoll < InspireRoll:
            print("I won!")
            InspireWins += 1
        else:
            print("We tied!")

        print("You have won " + str(userWins) + " times, I have won " + str(InspireWins) + " times.")
def entertainerSimpleQuiz():

    questionsRight = 0
    questionsWrong  = 0
    questionsTotal = 0

    def provideChoices(choiceOne, choiceTwo, choiceThree, choiceFour):
        print("a.) " + choiceOne)
        print("b.) " + choiceTwo)
        print("c.) " + choiceThree)
        print("d.) " + choiceFour)

    print("Welcome to the Simple Quiz!")
    time.sleep(0.5)
    print("The Simple Quiz is a fun way of testing out your trivia skills regarding things tech!.")
    time.sleep(0.5)
    print("Let's go!")

    correctAnswers = ["Data engineer", "Python", "Central Processing Unit", "Bill Gates", "PlayStation 2"]

    #Question 1
    print("Question 1: Which of the following computer science related jobs has the highest average salary? (answer with the answer choice, not the letter)")
    provideChoices("Computer programmer", "Business intelligence analyst", "Data engineer", "Software developer")
    userAnswer = str(input(""))
    if "data" in userAnswer.lower():
        questionsRight += 1
        questionsTotal += 1
        print("Correct! You earned a point!")
        print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    else:
            questionsWrong += 1
            questionsTotal += 1
            print("Incorrect. The correct answer was: " + correctAnswers[0] + ".")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")

    #Question 2
    print("Question 2: Which of the following programming languages is considered to be the most versatile? (answer with the answer choice, not the letter)")
    provideChoices("JavaScript", "Python", "C++", "SQL")
    userAnswer = str(input(""))
    if "py" in userAnswer.lower():
            questionsRight += 1
            questionsTotal += 1
            print("Correct! You earned a point!")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    else:
            questionsWrong += 1
            questionsTotal += 1
            print("Incorrect. The correct answer was: " + correctAnswers[1] + ".")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")

    #Question 3
    print("Question 3: Which of the following abbreviations of 'CPU' is correct? (answer with the answer choice, not the letter)")
    provideChoices("Computer Processing Unit", "Computer Producing Unit", "Central Processing Unit", "Central Producing Utilization")
    userAnswer = str(input(""))
    if "central processing unit" in userAnswer.lower():
            questionsRight += 1
            questionsTotal += 1
            print("Correct! You earned a point!")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    else:
            questionsWrong += 1
            questionsTotal += 1
            print("Incorrect. The correct answer was: " + correctAnswers[2] + ".")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")

    #Question 4
    print("Question 4: Which of the following entrepreneurs was the founder of Microsoft? (answer with the answer choice, not the letter)")
    provideChoices("Satya Nadela", "Bill Gates", "Steve Jobs", "Linus Torvalds")
    userAnswer = str(input(""))
    if "bill" in userAnswer.lower():
            questionsRight += 1
            questionsTotal += 1
            print("Correct! You earned a point!")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    else:
            questionsWrong += 1
            questionsTotal += 1
            print("Incorrect. The correct answer was: " + correctAnswers[3] + ".")
            print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")

    #Question 5
    print("Question 5: Which of the following has been the best selling video game console of all time? (answer with the answer choice, not the letter)")
    provideChoices("Nintendo DS", "XBOX 360", "PlayStation 2", "XBOX One")
    userAnswer = str(input(""))
    if "playstation" in userAnswer.lower():
        questionsRight += 1
        questionsTotal += 1
        print("Correct! You earned a point!")
        print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    else:
        questionsWrong += 1
        questionsTotal += 1
        print("Incorrect. The correct answer was: " + correctAnswers[4] + ".")
        print("Your current score is: " + str(questionsRight) + "/" + str(questionsTotal) + ".")

    print("Your total score was: " + str(questionsRight) + "/" + str(questionsTotal) + ".")
    print("Thanks for quizzing!")
def entertainer8Ball():
    #Brief introduction to the Magic 8Ball minigame
    print("Welcome to Magic 8Ball!")
    print("Simply ask a yes or no question, and the Magic 8Ball will deliver!")
    print("Say 'quit' if you would like to stop at any moment.")

    #List containing all the responses that the Magic8Ball can provide
    Magic8Ball = [
    #5 affirmative answers
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "As I see it, yes.",
    "Outlook good.",
     #5 negative answers
     "Don't count on it.",
     "My reply is no.",
     "My sources say no.",
     "Outlook not so good.",
     "Very doubtful.",
     #5 non commital answers
     "Reply hazy, try again.",
     "Ask again later."
     "Better not tell you now."
     "Cannot predict now."
     "Concentrate and ask again."
    ]

    #Prompts user to ask a yes or no question
    input8Ball = str(input("Ask a yes or no question. Say 'quit' if you would like to stop at any moment.\n "))

    #While the user doesn't want to quit, Inspire will active the Magic8Ball, giving the user a random response from the preset responses
    while "quit" != input8Ball:
        print(random.choice(Magic8Ball))
        input8Ball = str(input("Ask a yes or no question. Say 'quit' if you would like to stop at any moment.\n "))
def entertainerRockPaperScissors():
    print("Welcome to Rock, Paper, Scissors!")

    while True:

        #Asks user to enter a number signifying their choice
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        userChoice = int(input("Enter your choice : \n"))

        #Makes sure the number is within the range of choices
        while userChoice > 3 or userChoice < 1:
            userChoice = int(input('Enter either rock, paper, or scissors.'))

        #Assigns each choice a number and name based on input
        if userChoice == 1:
            userChoiceName = "Rock"
        elif userChoice == 2:
            userChoiceName = "Paper"
        elif userChoice == 3:
            userChoiceName = "Scissors"

        #Returns the choice to the user, Inspire makes its own choice
        print("Your choice was: " + userChoiceName + ".")
        print("Now it's my turn.")

        #Inspire randomly chooses a value between 1 and 3, signifying either rock, paper, or scissors.
        computerChoice = random.randint(1,3)

        #Assigns each choice a number and name based on input
        if computerChoice == 1:
            computerChoiceName = 'Rock'
        elif computerChoice == 2:
            computerChoiceName = 'Paper'
        elif computerChoice == 3:
            computerChoiceName = 'Scissors'

        print("My choice is: " + computerChoiceName + ".")
        #Based on user and Inspire's choices, checks for winner, loser, or tie

        #Tie outcome
        if userChoiceName == computerChoice:
            print("<== It's a tie! ==>")

        #Paper outcomes, prints who is the winner based on the choices made
        if (userChoice == 1 and computerChoice == 2):
            print("<== Paper wins! ==>")
            print("<== I win! ==>")
        elif (userChoice == 2 and computerChoice ==1):
            print("<== Paper wins! ==>")
            print("<== You win! ==>")

        #Rock outcomes, prints who is the winner based on the choices made
        if (userChoice == 1 and computerChoice == 3):
            print("<== Rock wins! ==>")
            print("<== You win! ==>")
        elif (userChoice == 3 and computerChoice == 1):
            print("<== Rock wins! ==>")
            print("<== I win! ==>")

        #Scissors outcomes, prints who is the winner based on the choices made
        if (userChoice == 2 and computerChoice == 3):
            print("<== Scissors wins! ==>")
            print("<== I win! ==>")
        elif (userChoice == 3 and computerChoice == 2):
            print("<== Scissors wins! ==>")
            print("<== You win! ==>")

        #Asks user if they are interested in playing again, repeating the game until they are uninterested
        userInterest = str(input("Do you want to play again (yes or no)? \n"))
        if userInterest.lower() == "no":
            break

    print("Thanks for playing!")


def entertainerRunner():
    userEntertainerActive = True
    print("Welcome to the entertainer functionality!")
    userEntertainerInput = str(input("Enter which feature of the entertainer functionality you would like to try out: \n - Type 'number guess' to play a number guessing game.\n - Type 'dice' to play a dice game.\n - Type 'simple quiz' to do some trivia.\n - Type 'magic 8ball' to use a magic 8ball.\n - Type 'rock paper scissors' to play rock, paper, scissors. \n"))

    while userEntertainerActive:
        if "exit" == userEntertainerInput.lower():
            userEntertainerActive = False
            break
        elif userEntertainerInput.lower() in "exit":
            userEntertainerActive = False
            break
        else:
            userEntertainerActive = True

            if "number guess" in userEntertainerInput.lower():
                entertainerNumGuesser()
            elif "dice" in userEntertainerInput.lower():
                entertainerDice()
            elif "simple quiz" in userEntertainerInput.lower():
                entertainerSimpleQuiz()
            elif "8ball" in userEntertainerInput.lower():
                entertainer8Ball()
            elif "rock paper scissors" in userEntertainerInput.lower():
                entertainerRockPaperScissors()
            else:
                print("Sorry, I couldn't understand what you said. Try selecting one of the given options, or type 'exit' if you are trying to quit out of the calculator functionality. \n")

            userEntertainerInput = str(input("Enter which feature of the entertainer functionality you would like to try out: \n - Type 'number guess' to play a number guessing game.\n - Type 'dice' to play a dice game.\n - Type 'simple quiz' to do some trivia.\n - Type 'magic 8ball' to use a magic 8ball.\n - Type 'rock paper scissors' to play rock, paper, scissors. \n"))
