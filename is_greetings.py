import numpy as np
import random

#
#DB
#
greetings = ["hi", "hello", "hey", "yo", "greetings"]
greetings_responses = ["Hi there.", "Greetings Human.", "Hello there", "Hey"]

#
#GREETINGS
#
def generateGreetingsReply(message):
		
	tokens = message.split(" ")
		
	#If first word of message is an element of greetings
	if len(tokens) > 0 and tokens[0].lower() in greetings:
		print( random.choice(greetings_responses) )
		return True

	else:
		return False