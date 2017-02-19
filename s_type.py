import numpy as np
import random
import sys

from break_message import s_break
from is_question import detectQuestion, inspect_question
from is_greetings import generateGreetingsReply
from is_order import detectOrder


#
#INITIALIZATION
#
words = []
present_marks = []
words = []
if_counter = 0
question_identifier = ["how", "where", "when", "who", "what", "?"]
greetings = ["hi", "hello", "hey", "yo", "greetings"]
greetings_responses = ["Hi there.", "Greetings Human.", "Hello there", "Hey"]


#
#DETECT TYPE OF SENTENCE
#
def get_type(message):
	#
	#BREAK MESSAGE IN WORDS
	#
	words = message.split(" ")
	#
	#GREETINGS
	#
	generateGreetingsReply(message, greetings, greetings_responses)
	#
	#QUESTION
	#
	if detectQuestion(message, question_identifier, present_marks) == True:
		inspect_question(message, words, question_identifier, present_marks)
	#
	#ORDER
	#
	detectOrder(message)






























# Text -> Speach = eSpeak API
# Speach -> Text = Google Speech Api