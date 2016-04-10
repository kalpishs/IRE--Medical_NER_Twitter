import re
import itertools

def pos_tags(file_name):
	fobj = open(file_name)
	string=fobj.read()

	STR=re.split('"', string)
	
	words=STR[1].split(" ")
	word_list=[]
	for word in words:
		word_list.append(word.lower())
	
	#print len(words)
	STR[2] = STR[2].strip()
	#print STR[2]
	tags=STR[2].split()[:len(word_list)]
	pos_list=[]
	for tag in tags:
		pos_list.append(tag)
	dictionary  = dict(itertools.izip(word_list,pos_list))
	
	length=len(word_list)
	for listl in range(length):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word_list[listl])
		if urls:
			del dictionary[word_list[listl]]

	#print dictionary		
	return dictionary

def term_tag(tagger, term):
	term = term.lower()
	if tagger.has_key(term):
		tagger[term] = tagger[term].replace(" ","")
		return tagger[term]
	else:
		for key in tagger.keys():
			try:
				if unicode(term) in unicode(key):
					tagger[key] = tagger[key].replace(" ","")
					return tagger[key]
			except:
				#print term
				return ","		
		return ","
			