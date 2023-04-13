import random

greetingPatterns = [
"Hi",
"Hey",
"Hello"
]
greetingResponses = [
"Hi, thanks for visiting! How can I help?",
"Hey, thanks for visiting! How can I help?",
"Hello, thanks for visting! How can I help?"
]

howAreYouPatterns = [
"How are you",
"How are you doing",
"How are you feeling",
"Whats up",
"Sup"
]
howAreYouResponses = [
"I'm alright.",
"Doing alright!",
"Feeling good."
]

goodbyePatterns = [
"Bye",
"Goodbye",
"See you later"
]
goodbyeResponses = [
"Bye, thanks for visiting! Come again soon.",
"Goodbye, thanks for visiting! Come again soon.",
"See you later, thanks for visiting! Come again soon."
]

thanksPatterns = [
"Thanks",
"Thank you",
"Thanks for helping out",
"Thanks for helping me"
]
thanksResponses = [
"No problem!",
"My pleasure!",
"Any time!",
"Happy to help!",
"Glad to help!"
]

identityPatterns = [
"Who are you",
"What are you",
"Who made you",
"Who designed you",
"Who programmed you",
"Who created you",
"Who is your maker",
"Who is your designer",
"Who is your programmer",
"Who is your creator"
]
identityResponses = [
"""My name is Inspire, a simple, basic chatbot designed, programmed, and created by Aruneem. I can complete various simple tasks. Here's a simple breakdown of what I can do:\n
- Discussant: engaging in simple talk with you.\n
- Calculator: performing basic mathematical calculations for you.\n
- Entertainer: playing simple games with you.\n
Let me know what you need, and I can see what I can do!"""
]

capabilitiesPatterns = [
"What do you do",
"What can you do",
"How can you help",
"How can you be helpful",
"What is your purpose",
"What is your significance",
"What is your use",
"What support do you offer",
"What support is offered",
"What is your objective"
"What can you do"
"What do you do"
"What do you provide"
"What can you provide"
]
capabilitiesResponses = [
"""I can complete various simple tasks. Here's a simple breakdown of what I can do:\n
- Discussant: engaging in simple talk with you.\n
- Calculator: performing basic mathematical calculations for you.\n
- Entertainer: playing simple games with you.\n
Let me know what you need, and I can see what I can do!"""
]

jokePatterns = [
 "Joke",
"Tell a joke",
"Tell me a joke",
"Laugh",
"Make me laugh",
"Funny",
"Say something funny"
]
jokeResponses = [
"Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
"Where are average things manufactured? The satisfactory.",
"How do you drown a hipster? Throw him in the mainstream.",
"What is an astronaut’s favorite part on a computer? The space bar.",
"How do you throw a space party? You planet.",
"Why can’t male ants sink? They’re buoy-ant.",
"Want to hear a construction joke? Oh never mind, I’m still working on that one."
]

hobbiesPatterns = [
"What do you like to do",
"What do you like to do in your free time",
"What is your hobby",
"What is your pastime",
"What do enjoy",
"What do you like",
"What do you love"
]
hobbiesResponses = [
"My creator loves learning about new things, playing video games, and watching Star Wars. In my free time, I like to learn more about human speech and become a better chatbot!"
]


specialCharacters = [".", ",", ";", ":", "?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/"]

def intentFinder(intent, patterns, responses, found):
    for pattern in patterns:
        if pattern.lower() in intent:
            intent = str("\n" + input(random.choice(responses) + "\n"))
            found = True
        elif intent in pattern.lower():
            intent = str("\n" + input(random.choice(responses) + "\nType 'exit' to quit out of the beta feature. \n"))
            found = True

def discussantRunner():
    print("Welcome to the beta feature of the discussant functionality!")
    userDiscussantActive = True
    responseFound = False
    userDiscussantInput = str(input("Type whatever you'd like, and I can try my best to form a relevant response! \n"))

    while userDiscussantActive:

        for specialCharacter in specialCharacters:
            userDiscussantInput = userDiscussantInput.replace(specialCharacter, "")
            userDiscussantInput = userDiscussantInput.lower()

        if "exit" in userDiscussantInput.lower():
            userDiscussantActive = False
            break
        elif userDiscussantInput.lower() in "exit":
            userDiscussantActive = False
            break
        else:
            userDiscussantActive = True

            intentFinder(userDiscussantInput, greetingPatterns, greetingResponses, responseFound)
            intentFinder(userDiscussantInput, howAreYouPatterns, howAreYouResponses, responseFound)
            intentFinder(userDiscussantInput, goodbyePatterns, goodbyeResponses, responseFound)
            intentFinder(userDiscussantInput, thanksPatterns, thanksResponses, responseFound)
            intentFinder(userDiscussantInput, identityPatterns, identityResponses, responseFound)
            intentFinder(userDiscussantInput, capabilitiesPatterns, capabilitiesResponses, responseFound)
            intentFinder(userDiscussantInput, jokePatterns, jokeResponses, responseFound)
            intentFinder(userDiscussantInput, hobbiesPatterns, hobbiesResponses, responseFound)

            if responseFound == False:
                userDiscussantInput = str(input("Sorry, I couldn't understand what you said. Perhaps you could try typing something else, or rephrasing what you said? \nType 'exit' to quit out of the beta feature. \n"))

                responseFound = False
