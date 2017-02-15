import numpy as np
from break_message import words

#
#DB
#
present_marks = []
if_counter = 0
question_identifier = ["how", "where", "when", "who", "what", "?"]


def detectQuestion(message):

	if any(question_mark in message for question_mark in question_identifier):
		print("We have a question")
		return True
	else:
		return False


#
#IF DETECTQUESTION IF TRUE
#

def inspect_question(message):
	print("&&&&&&&&&&&&&&")
	for i in xrange(words.length()):
		#ARRAY OF QUESTION MARKS FROM MESSAGE
		print("$$$$$$$$$$$$$$$$$$")
		if present_marks[counter] in words:
			if_counter += 1
			present_marks[if_counter] = words[for_counter]
			print(present_marks[if_counter])
		for_counter+=1

	#ANALYZE QUESTION MARKS
	print("processing question...")

	for question_identifier in present_marks:
		print("We have one")
