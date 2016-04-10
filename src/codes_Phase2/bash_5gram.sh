export java_home=/home/chinmay/Workstation/IRE/Major/mallet
export path=/home/chinmay/Workstation/IRE/Major/public_mm/bin/
export path2=/home/chinmay/Workstation/IRE/Major/ark-tweet-nlp-0.3.2/

rm ../training_files/training_file_5gram || ls ../training_files/*
rm ../testing_files/gold_testing_5gram || ls ../testing_files/*

train="../../data/training_Annotations/*"
testi="../../data/testing_Annotations/*"

#------making training feature files-----#
for  folder in $train
do

	for files in $folder/*.txt	
	 do
		echo $files
		`echo "bash $path/testapi.sh --input $files --output meta_out"`
		`echo $(bash $path2/runTagger.sh $files) > pos_out`
		python training_features_5gram.py $files ../training_files/training_file_5gram
	done;
done;		

#---------making testing feature files-------#
for  folder in $testi
do

	for files in $folder/*.txt

	
	 do
		echo $files
		`echo "bash $path/testapi.sh --input $files --output out"`
		python training_features_5gram.py $files ../testing_files/gold_testing_5gram
    		
	
	done;
done;
#----------train model-------#
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_5gram ../training_files/training_file_5gram"`

#---testing----#
cut -d' ' -f1-15 ../testing_files/gold_testing_5gram > ../testing_files/testing_file_5gram
cut -d' ' -f16 ../testing_files/gold_testing_5gram > ../testing_files/gold_tags_5gram
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_5gram ../testing_files/testing_file_5gram) > ../system_result/system_tags_5gram`

#----accuracy---# 
python accuracy.py ../testing_files/gold_tags_5gram ../system_result/system_tags_5gram
 
 
