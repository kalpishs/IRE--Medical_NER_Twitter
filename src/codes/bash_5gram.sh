export java_home=/home/chinmay/Workstation/IRE/Major/mallet



train="./data/training_Annotations/*"
testi="./data/testing_Annotations/*"

#------making training feature files-----#
for  folder in $train
do

	for files in $folder/*.ann	
	 do
		echo $files
		python training_features_5gram.py $files training_file_5gram
	done;
done;		

#---------making testing feature files-------#
for  folder in $testi
do

	for files in $folder/*.ann

	
	 do
		echo $files
		python training_features_5gram.py $files gold_testing_5gram
    		
	
	done;
done;
#----------train model-------#
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file trained_model_5gram training_file_5gram"`

#---testing----#
cut -d' ' -f1,2,3,4,5 gold_testing_5gram > testing_file_5gram
cut -d' ' -f6 gold_testing_5gram > gold_tags_5gram
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file trained_model_5gram testing_file_5gram) > system_tags_5gram`

#----accuracy---# 
python accuracy.py gold_tags_5gram system_tags_5gram
 
 
