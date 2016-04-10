#/usr/bin
# -*- coding: utf-8 -*-
import re
import sys
from metamap import *
from pos_tagger import *

Classify = ["Disease", "Drug", "Symptom"]

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

def make_file(filename,combined_file):
	ngram=5
	tag_flag=0
	train = ""
	Disease = []
	Drug = []
	Symptom = []
	tmp=filename.split(".txt")
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
		if len(Drug_list) != 0:
			Drug.append(Drug_list)
		if len(Symptom_list) != 0:
			Symptom.append(Symptom_list)												
	
	f = open(filename)
	f2 = open(combined_file, "a")
	
	while 1:
		line = f.readline()
		line = line.split("http")[0]
		if line == "":
			break
		line = tokenise(line)
		list = line.split(" ")
		for ind in xrange(len(list)):
			add1 = ""
			add1 = list[ind] + " " + meta_tag(list[ind]) + " " + term_tag(tagger, list[ind])
			context = ngram/2
			try:
				for no in range(1,context+1):
					if ind-no >=0:
						add1 += " " + list[ind-no] + " " + meta_tag(list[ind-no])+ " " + term_tag(tagger, list[ind-no])
					else:
						list[ind+100000]
									
			except:
				add1 += " NOLEFT nil ,"*(context+1 - no) 
			
			try:
				for no in range(1,context+1):
					add1 += " " + list[ind+no] + " " + meta_tag(list[ind+no]) + " " + term_tag(tagger, list[ind+no])
									
			except:
				add1 += " NORIGHT nil ,"*(context+1 - no) 

			tag = gives_tag(Disease, list[ind], 0)
			if tag == "":
				tag = gives_tag(Drug, list[ind], 1)
				if tag == "":
					tag = gives_tag(Symptom, list[ind], 2)
					if tag == "":
						tag = "None"

			add1 += " " + tag + "\n"
			f2.write(add1)
		#f2.write("\n")
		
		f2.close()
		

meta_map("meta_out")
tagger = pos_tags("pos_out")
make_file(sys.argv[1],sys.argv[2])

