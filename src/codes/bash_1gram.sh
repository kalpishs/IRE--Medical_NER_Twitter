export java_home=/home/chinmay/Workstation/IRE/Major/mallet



train="./data/training_Annotations/*"
testi="./data/testing_Annotations/*"

#------making training feature files-----#
for  folder in $train
do

	for files in $folder/*.ann	
	 do
		echo $files
		python training_1gram_features.py $files training_file_1gram
	done;
done;		

#---------making testing feature files-------#
for  folder in $testi
do

	for files in $folder/*.ann

	
	 do
		echo $files
		python training_1gram_features.py $files gold_testing_1gram
    		
	
	done;
done;
#----------train model-------#
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file trained_model_1gram training_file_1gram"`

#---testing----#
cut -d' ' -f1 gold_testing_1gram > testing_file_1gram
cut -d' ' -f2 gold_testing_1gram > gold_tags_1gram
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file trained_model testing_file) > system_tags_1gram`

#----accuracy---# 
python accuracy.py gold_tags_1gram system_tags_1gram
 
 
