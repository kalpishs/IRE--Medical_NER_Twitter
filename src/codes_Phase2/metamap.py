from collections import defaultdict
import operator
import sys
from nltk.stem.porter import *
stemmer = PorterStemmer()
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
				line = line.split(start)[1]
				line = line.split("http")[0]
				line = line.lower()
				line = line.strip()
				line = line.replace("  ", " ")
				line = line.replace('"', "")
				text_list = line.split(" ")
	
				for terms in text_list:
					term_list[terms] = {}
			
			if 	line.startswith("Phrase:") or flag==0:
				flag = 0
				if line == "":
					break
				line = i.readline()
				if line.startswith("Mappings:"):
					while line != "":
						if line.startswith("Phrase:"):
							break
						line = i.readline()
						if check1 in line:
							line = line.split(check1)[1].strip()
							text = line[:len(line)-1].lower()
							for elem in text_list:
								if text in elem:
									text = elem
							line = i.readline()	
							if check2 in line:
								ans = line.split(check2)[1].strip()
								ans = ans[:len(ans)-1]
								if term_list[text].has_key(ans):
									term_list[text][ans] += 1
								else:
									term_list[text][ans] = 1

		
		final_tags = defaultdict(str)
		#print "term_list", term_list			
		for items in term_list.keys():
			if len(term_list[items].keys()) == 0:
				final_tags[items] = "nil"
			else:
				form_list = term_list[items]
				final_tags[items] = max(form_list.iteritems(), key=operator.itemgetter(1))[0]			
		global tags
		tags = final_tags
		#print tags

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
