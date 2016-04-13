import sys

gold_tags=sys.argv[1]
system_tags=sys.argv[2]

f2 = open(gold_tags, "r")

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

drugs=[0.0,0.0,0.0]
disease=[0.0,0.0,0.0]
symptom=[0.0,0.0,0.0]
none=[0.0,0.0,0.0]
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

p1=r1=f1=p2=r2=f2=p3=r3=f3=p4=r4=f4=0
try:
	p1 = drugs[0]/drugs[1]
except:
	pass

try:
	r1 = drugs[0]/drugs[2]
except:
	pass

try:
	f1 = (2*p1*r1)/(p1+r1)
except:
	pass

try:
	p2 = disease[0]/disease[1]
except:
	pass

try:	
	r2 = disease[0]/disease[2]
except:
	pass

try:
	f2 = (2*p2*r2)/(p2+r2)
except:
	pass

try:	
	p3 = symptom[0]/symptom[1]
except:
	pass

try:	
	r3 = symptom[0]/symptom[2]
except:
	pass

try:
	f3 = (2*p3*r3)/(p3+r3)
except:
	pass

try:	
	p4 = none[0]/none[1]
except:
	pass

try:	
	r4 = none[0]/none[2]
except:
	pass

try:
	f4 = (2*p4*r4)/(p4+r4)
except:
	pass

print "Drugs: Precision - ",p1, " Recall - ",r1, " F-Score - ",f1 

print "Disease: Precision - ",p2, " Recall - ",r2, " F-Score - ",f2 

print "Symptom: Precision - ",p3, " Recall - ",r3, " F-Score - ",f3 

print "None: Precision - ",p4, " Recall - ",r4, " F-Score - ",f4 
print ""


accuracy= (tags_matched*1.0)/total_tags
print "Accuracy =" + str(tags_matched)+"/"+str(total_tags)+"="+str(accuracy)
		

