""" Extracting and storing pos tags of a tweet
 generated through tweet-nlp stored in file 'pos_out'"""

import re
import itertools

""" Function which returns a dictionary of the form {term:pos-tag_of_term} """
def pos_tags(file_name):
	fobj = open(file_name)
	string=fobj.read()

	#!---Splitting on the basis of quotes, all tweets are in quotes---#
	
	STR=re.split('"', string)
	
	words=STR[1].split(" ")
	word_list=[]
	for word in words:
		word_list.append(word.lower())
	
	#!---Extracting same no. of pos-tags
	#!---as words extracted from tweets---#

	STR[2] = STR[2].strip()
	tags=STR[2].split()[:len(word_list)]
	pos_list=[]
	for tag in tags:
		pos_list.append(tag)
	dictionary  = dict(itertools.izip(word_list,pos_list))
	
	length=len(word_list)
	for listl in range(length):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word_list[listl])
		if urls:
			try:
				del dictionary[word_list[listl]]
			except:
				pass	
	return dictionary


""" Function that returns pos tag of a term if contained in dictionary tagger """
def term_tag(tagger, term):
	term = term.lower()
	if tagger.has_key(term):
		tagger[term] = tagger[term].replace(" ","")
		return tagger[term]
	else:
		for key in tagger.keys():
			try:
				if term in key:
					tagger[key] = tagger[key].replace(" ","")
					return tagger[key]
			except:
				return ","		
		return ","
			