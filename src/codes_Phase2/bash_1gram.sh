echo """ Implementing Medical NER for 1gram"""

export java_home=/home/chinmay/Workstation/IRE/Major/mallet  			#location of mallet wrt root
export path=/home/chinmay/Workstation/IRE/Major/public_mm/bin/			#location of metamap wrt root
export path2=/home/chinmay/Workstation/IRE/Major/ark-tweet-nlp-0.3.2/	#location of tweet-nlp wrt root

echo """ Removing previously used training files """
rm ../training_files/training_file_1gram || ls ../training_files/*
rm ../testing_files/gold_testing_1gram || ls ../testing_files/*

train="../../data/training_Annotations/*"		#location of training data wrt current folder - codes
testi="../../data/testing_Annotations/*"		#location of testing data wrt current folder - codes

echo """ Generating cluster_out for importing cluster-id dictionary """
python cluster.py ../../data/cluster50/paths	

#------making training feature files-----#
for  folder in $train
do
	for files in $folder/*.txt	
	 do
		echo $files
		python training_1gram_features.py $files ../training_files/training_file_1gram
	done;
done;		

#---------making testing feature files-------#
for  folder in $testi
do
	for files in $folder/*.txt
	 do
		echo $files
		python training_1gram_features.py $files ../testing_files/gold_testing_1gram	
	done;
done;

#----------train model-------#
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_1gram ../training_files/training_file_1gram"`

#---testing----#
cut -d' ' -f1-18 ../testing_files/gold_testing_1gram > ../testing_files/testing_file_1gram
cut -d' ' -f19 ../testing_files/gold_testing_1gram > ../testing_files/gold_tags_1gram
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_1gram ../testing_files/testing_file_1gram) > ../system_result/system_tags_1gram`

#----Evaluating Efficiency----# 
python evaluate.py ../testing_files/gold_tags_1gram ../system_result/system_tags_1gram
 
 
