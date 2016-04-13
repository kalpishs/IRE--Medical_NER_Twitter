import sys
clust_dict = {}
def get_cluster(file):
	f = open(file)
	line = "line"
	word_dict = {}
	while line != "":
		line = f.readline()
		print line
		try:
			cluster = line.split(" ")[0]
			word = line.split(" ")[1]
			word_dict[word] = cluster
		except:
			print "Here", line
	new = "cluster_out"		
	f = open(new, "w")
	f.write(str(word_dict))
	f.close()			 	

def cluster_dict(word):
	global clust_dict
	f = open("cluster_out")
	clust_dict = f.readline
	
get_cluster(sys.argv[1])	
