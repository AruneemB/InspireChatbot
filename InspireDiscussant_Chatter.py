from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Inspire")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
