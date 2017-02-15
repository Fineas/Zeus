import numpy as np
from s_type import get_type

#
#DB
#
questions_keywords = ["how", "what", "where", "when", "which"]


#
#INPUT
#
while True:
	message = raw_input("Say something to Pateu: ")
	#FUNCTIONS
	get_type(message)