import sys

""" Testing file - predefined annotated tags """
gold_tags=sys.argv[1]       

""" System Generated file - containing tags separated by space """  
system_tags=sys.argv[2]

f2 = open(gold_tags, "r")

""" 	Making 2 lists of tags with the tags extracted from each file 	"""   

gold_tags = list()
line = "gold"
while line != "":
	line = f2.readline()
	if line != "":
		gold_tags.append(line)

f = open(system_tags, "r")
system_tags = f.readline()
system_tags = system_tags.split(" ")

tags_matched=0
total_tags=len(gold_tags)


print "system_tags:", len(system_tags)
print "gold_tags:",len(gold_tags)

drugs=[0.01,0.01,0.01]
disease=[0.01,0.01,0.01]
symptom=[0.01,0.01,0.01]
none=[0.01,0.01,0.01]
for i in xrange(total_tags):
	#print gold_tags[i], system_tags[i]
	if gold_tags[i].strip()==system_tags[i].strip():
		if "Drug" in system_tags[i]:
			drugs[0] += 1
		elif "Disease" in system_tags[i]:
			disease[0] += 1
		elif "Symptom" in system_tags[i]:
			symptom[0] += 1
		else:
			none[0] += 1

		tags_matched +=1
	if "Drug" in system_tags[i]:
		drugs[1] += 1
	elif "Disease" in system_tags[i]:
		disease[1] += 1
	elif "Symptom" in system_tags[i]:
		symptom[1] += 1
	else:
		none[1] += 1
					

	if "Drug" in gold_tags[i]:
		drugs[2] += 1
	elif "Disease" in gold_tags[i]:
		disease[2] += 1
	elif "Symptom" in gold_tags[i]:
		symptom[2] += 1
	else:
		none[2] += 1

""" p represents precision, r recall and f represents f score """
""" Calculating the above mentioned metrics for each label """

p1 = drugs[0]/drugs[1]
r1 = drugs[0]/drugs[2]
f1 = (2*p1*r1)/(p1+r1)

p2 = disease[0]/disease[1]
r2 = disease[0]/disease[2]
f2 = (2*p2*r2)/(p2+r2)
	
p3 = symptom[0]/symptom[1]
r3 = symptom[0]/symptom[2]
f3 = (2*p3*r3)/(p3+r3)

p4 = none[0]/none[1]
r4 = none[0]/none[2]
f4 = (2*p4*r4)/(p4+r4)

print "Drugs: Precision - ",p1, " Recall - ",r1, " F-Score - ",f1 

print "Disease: Precision - ",p2, " Recall - ",r2, " F-Score - ",f2 

print "Symptom: Precision - ",p3, " Recall - ",r3, " F-Score - ",f3 

print "None: Precision - ",p4, " Recall - ",r4, " F-Score - ",f4 
print ""


""" Accuracy calculated by a simple formula """

accuracy= (tags_matched*1.0)/total_tags
print "Accuracy =" + str(tags_matched)+"/"+str(total_tags)+"="+str(accuracy)
		

