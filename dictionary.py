import numpy as np
import urllib2
import requests

response = urllib2.urlopen("http://google.ro")
page_source = response.read()

data = urllib2.urlopen("http://www.google.com").read(20000) # read only 20 000 chars
data = data.split("\n") # then split it into lines

for line in data:
    print line


#
#QUESTION
#
dictionary = []

class word:
	name = "name"
