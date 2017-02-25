import numpy as np

from s_type import get_type
from repeated_input import *

msg_insrt = 0
message_history = []

#
#INPUT
#
while True:
	for i in xrange(0, 15):
		print(" ")

	message = raw_input("Say something to Zeus: ")

	repeted_input(message, message_history)
	
	if msg_insrt == 2:
		if message_history[0] == message_history[1] and message_history[0] == message_history[2] and message_history[1] == message_history[2]:
			print("Is '%s' all you know?" % (message_history[0]))
		else:
			get_type(message)
		msg_insrt = 0
		del message_history[:]
	else:
		msg_insrt += 1
		get_type(message)
