import numpy as np

post_me = None


#
#QUESTION
#
def detectQuestion(message, question_identifier, present_marks):

	if any(question_mark in message for question_mark in question_identifier):
		return True
	else:
		return False


#
#IF DETECT_QUESTION IS TRUE (FIND QUESTION_MARKS, AND ANALYZE)
#
def inspect_qiuestion(words, question_identifier, present_marks):
	for_counter = 0
	true_counter = 0;
	for i in xrange(0, len(words)):
		personal_ques(i, words)
		if_counter = 0
		for j in xrange(0, len(question_identifier)):
			if words[for_counter] == question_identifier[if_counter]:
				present_marks.append(words[for_counter])
				true_counter+=1
			if_counter += 1
		for_counter+=1


#
#FIND IF THE QUESTION HAS THE "you" WORD
#
def personal_ques(coiunter, words):
	if words[counter] == "you":
		print("Personal Question Detected")
		return True


#
#GENERATE ANSWER FOR PERSONAL QUESTION
#
def my_question():
	return "I"


#
#generate QUESTION ANSWER
#
def question_answer(words):
	if personal_ques:
		for i in xrange(0, len(words)):
			if words[i] == "you":
				if words[i-1] == "are":
					post_me = "am"
				else:
					post_me = words[i-1]
		print("%s %s " % (my_question() , post_me))
