""" Module for extracting a {term,meta-tag} dictionary
		 for a tweet from the output of metamap tool 
		 stored in file 'meta_out'"""

from collections import defaultdict
import operator
import sys
from nltk.stem.porter import *
stemmer = PorterStemmer()

""" Dictionary which stores metamap generated semantic tags for terms of a tweet """ 
tags = defaultdict(dict)   

def meta_map(file_name):
	with open(file_name, "r") as i:
		line = "read"
		term_list = defaultdict(dict)
		text_list = list()
		start = "Utterance text:" 
		check1 = "Matched Words: ["
		check2 = "Semantic Types: ["
		flag = 1
		while line != "":
			if flag == 1:
				line = i.readline()
			if start in line:

				#!---Should start with 'Utterance text:'---#
					
				line = line.split(start)[1]
				line = line.split("http")[0]
				line = line.lower()
				line = line.strip()
				line = line.replace("  ", " ")
				line = line.replace('"', "")
				text_list = line.split(" ")
	
				for terms in text_list:
					term_list[terms] = {}

			#!---For each term/phrase starts with tag: 'Phrase'---#	

			if 	line.startswith("Phrase:") or flag==0:
				flag = 0
				if line == "":
					break
				line = i.readline()

				#!---Final Semantic tags located under 'Mappings:'' section---#	

				if line.startswith("Mappings:"):
					while line != "":
						if line.startswith("Phrase:"):
							break
						line = i.readline()
						if check1 in line:

							#!---Finding 'Matched Word' and
							#!---'Semantic Tag' followed by it in next line---#

							line = line.split(check1)[1].strip()
							text = line[:len(line)-1].lower()
							for elem in text_list:
								if text in elem:
									text = elem
							line = i.readline()	
							if check2 in line:

								#!---Adding the newly extracted semantic tag
								#!---to a list inside a dictionary with term as key---#								
								ans = line.split(check2)[1].strip()
								ans = ans[:len(ans)-1]
								if term_list[text].has_key(ans):
									term_list[text][ans] += 1
								else:
									term_list[text][ans] = 1

		
		final_tags = defaultdict(str)
		for items in term_list.keys():
			if len(term_list[items].keys()) == 0:
				final_tags[items] = "nil"
			else:
				form_list = term_list[items]

				#!---Selecting the metamap - semantic with 
				#!---the highest frequency for that term---#

				final_tags[items] = max(form_list.iteritems(), key=operator.itemgetter(1))[0]			
		global tags
		tags = final_tags



""" 	Function that returns metamap tag of a term from the dictionary 'tags'	"""

def meta_tag(term):
	global tags
	#print tags
	term = term.lower()
	if tags.has_key(term):
		tags[term] = tags[term].replace(" ","")
		return tags[term]
	else:
		for key in tags.keys():
			try:
				if term in key:
					tags[key] = tags[key].replace(" ","")
					return tags[key]
			except:
				return "nil"		
		return "nil"	

meta_map(sys.argv[1])
