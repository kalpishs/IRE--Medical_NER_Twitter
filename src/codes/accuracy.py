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

for i in xrange(total_tags):
	#print gold_tags[i], system_tags[i]
	if gold_tags[i].strip()==system_tags[i].strip():
		tags_matched +=1

accuracy= (tags_matched*1.0)/total_tags
print "Accuracy =" + str(tags_matched)+"/"+str(total_tags)+"="+str(accuracy)
		

