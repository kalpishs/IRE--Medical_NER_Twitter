""" Module which appends combined feature file
	 with feature-rows for all terms of a tweet """

import re
import sys
from metamap import *
from pos_tagger import *
from ortho import *
import ast
from collections import defaultdict
from nltk.stem.porter import *

stemmer = PorterStemmer()
clust_dict = {}
Classify = ["Disease", "Drug", "Symptom"]
length = defaultdict(int)


""" Function which returns word_length """
def get_length(term):
	if length.has_key(term):
		return str(length[term])
	else:
		return str(len(term))	


""" Function which returns lemma of a term """
def stemmed(term):
	try:
		return stemmer.stem(term)
	except:
		return term	


""" Function which returns label of a term from annotated file """
def gives_tag(tlist, term, flag):
	tag = ""
	if len(tlist) == 0:
		return tag
	for lists in tlist:
		if term in lists:
			if lists.index(term) == 0:
				tag = Classify[flag] + "-begin"	
			else:
				tag = Classify[flag] + "-inside"
	return tag	


""" Function which generates global dictionary which contains cluster_id's for all terms """
def cluster_dict(filename):
	global clust_dict
	f = open(filename)
	dictionary = f.readline()
	try:
		clust_dict = ast.literal_eval(dictionary)
	except:
		print "error" 


""" Function which returns cluster_id form term which is a key in global cluster dictionary """
def cluster_tag(term):
	if clust_dict.has_key(term):
		return clust_dict[term]
	else:
		return "nil"	


""" Function which tokenises white spaces and quotes with spaces or blanks """
def tokenise(line):
	gapsadder = ['"',"\n","'","\r"]
	gaps2 = ["\t"]
	gap = "  "
	for i in gapsadder:
		line = line.replace(i, "")
	for i in gaps2:
		line = line.replace(i, " ")
	for gap in line:
		line = line.replace("  ", " ")	
	return line.strip()


""" Main function which appends combined feature file with feature-rows for all terms of a tweet """
def make_file(filename,combined_file):
	ngram=5
	tag_flag=0
	train = ""
	Disease = []
	Drug = []
	Symptom = []
	tmp=filename.split(".txt")

	#!-----Making lists of terms corresponding to each label from annotation file-----#

	fname2 = tmp[0]+ ".ann"	
	f = open(fname2)
	while 1:
		Disease_list = []
		Drug_list = []
		Symptom_list = []
		line = f.readline()
		if line == "":
			break
		line = tokenise(line)
		if line == "":
                        break	
		if line[0] == "T":
			list = line.split(" ")

			for k in xrange(len(list)):
				if list[1] == "Disease":
					tag_flag=1
					for terms in list[4:]:
						if terms not in Disease_list:
							Disease_list.append(terms)
				elif list[1] == "Drug":
					tag_flag=1
					for terms in list[4:]:
						if terms not in Drug_list:
							Drug_list.append(terms)
				elif list[1] == "Symptom-or-Side-Effect":
					tag_flag=1
					for terms in list[4:]:
						if terms not in Symptom_list:
							Symptom_list.append(terms)
		if len(Disease_list) != 0:
			Disease.append(Disease_list)
			joint = ("").join(Disease_list)
			for elem in Disease_list:
				length[elem] = len(joint)/len(Disease_list)
		if len(Drug_list) != 0:
			Drug.append(Drug_list)
			joint = ("").join(Drug_list)
			for elem in Drug_list:
				length[elem] = len(joint)/len(Drug_list)
		if len(Symptom_list) != 0:
			Symptom.append(Symptom_list)
			joint = ("").join(Symptom_list)
			for elem in Symptom_list:
				length[elem] = len(joint)/len(Symptom_list)												
	
	f = open(filename)
	f2 = open(combined_file, "a")
	
	#!-----Iterating over each term of a tweet and assigning feature tags to it-----#

	while 1:
		line = f.readline()
		line = line.split("http")[0]
		if line == "":
			break
		line = tokenise(line)
		list = line.split(" ")
		for ind in xrange(len(list)):
			add1 = ""
			add1 = list[ind] + " " + meta_tag(list[ind]) + " " + term_tag(tagger, list[ind]) + " " + get_length(list[ind]) + ortho_tag(list[ind]) + " " + cluster_tag(list[ind])
			flag1 = 0
			flag2 = 0
			noun = "nil"
			verb = "nil"
		
			for ind2 in range(ind+1, len(list)):
				next_term = list[ind2]
				if tagger.has_key(next_term):
					if tagger[next_term] == "N" and flag1==0:
						noun = next_term
						flag1 = 1
					elif tagger[next_term] == "V" and flag2==0:
						verb = next_term
						flag2 = 1
					elif flag1==1 and flag2==1:
						break

			add1 += " " + noun + " " + verb

			#!----Word Context and corresponding features (metamap + pos) for them----#
			
			context = ngram/2
			try:
				for no in range(1,context+1):
					if ind-no >=0:
						add1 += " " + list[ind-no]  + " " + meta_tag(list[ind-no])+ " " + term_tag(tagger, list[ind-no]) 
					else:
						list[ind+100000]
									
			except:
				add1 += " NOLEFT nil ,"*(context+1 - no) 
			
			try:
				for no in range(1,context+1):
					add1 += " " + list[ind+no]  + " " + meta_tag(list[ind+no]) + " " + term_tag(tagger, list[ind+no])
									
			except:
				add1 += " NORIGHT nil ,"*(context+1 - no) 

			tag = gives_tag(Disease, list[ind], 0)
			if tag == "":
				tag = gives_tag(Drug, list[ind], 1)
				if tag == "":
					tag = gives_tag(Symptom, list[ind], 2)
					if tag == "":
						tag = "None"

			#!-----Finally assigning label to each term according to previously created annotated lists----# 

			add1 += " " + tag + "\n"
			f2.write(add1)		
		f2.close()
		

""" Clustering Module """
cluster_dict("cluster_out")

""" Assigning metamap-tag dictionary for metamap output on whole tweet """
meta_map("meta_out")

""" Assigning pos-tag dictionary for tweetmlp output on whole tweet """
tagger = pos_tags("pos_out")

"""  Calling main function  """
make_file(sys.argv[1],sys.argv[2])

