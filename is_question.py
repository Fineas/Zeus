import numpy as np


#
#QUESTION
#
def detectQuestion(message, question_identifier, present_marks):

	if any(question_mark in message for question_mark in question_identifier):
		return True
	else:
		return False


#
#IF DETECT_QUESTION IS TRUE
#
def inspect_question(message, words, question_identifier, present_marks):
	for_counter = 0
	true_counter = 0;
	for i in xrange(0, len(words)):
		if_counter = 0
		for j in xrange(0, len(question_identifier)):
			if words[for_counter] == question_identifier[if_counter]:
				present_marks.append(words[for_counter])
				true_counter+=1
			if_counter += 1
		for_counter+=1
	print(present_marks)