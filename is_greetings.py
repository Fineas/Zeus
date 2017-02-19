import numpy as np
import random


#
#GREETINGS
#
def generateGreetingsReply(message, greetings, greetings_responses):
		
	tokens = message.split(" ")
		
	#If first word of message is an element of greetings
	if len(tokens) > 0 and tokens[0].lower() in greetings:
		print( random.choice(greetings_responses) )
		return True

	else:
		return False