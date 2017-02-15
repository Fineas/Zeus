import numpy
from is_greetings import generateGreetingsReply
from is_question import detectQuestion, inspect_question
from is_order import detectOrder
from break_message import s_break


def get_type(message):
	#
	#BREAK MESSAGE IN WORDS
	#
	s_break(message)
	#
	#GREETINGS
	#
	generateGreetingsReply(message)
	#
	#QUESTION
	#
	if detectQuestion(message) == True:
		inspect_question(message)
	#
	#ORDER
	#
	detectOrder(message)


# Text -> Speach = eSpeak API
# Speach -> Text = Google Speech Api