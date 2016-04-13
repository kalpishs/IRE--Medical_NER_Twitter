export java_home=/home/chinmay/Workstation/IRE/Major/mallet
export path=/home/chinmay/Workstation/IRE/Major/public_mm/bin
export path2=/home/chinmay/Workstation/IRE/Major/ark-tweet-nlp-0.3.2/

rm ../training_files/training_file_1gram || ls ../training_files/*
rm ../testing_files/gold_testing_1gram || ls ../testing_files/*

train="../../data/training_Annotations/*"
testi="../../data/testing_Annotations/*"

#------making training feature files-----#
for  folder in $train
do

	for files in $folder/*.txt	
	 do
		echo $files
		`echo "bash $path/testapi.sh --input $files --output meta_out2"`
		`echo $(bash $path2/runTagger.sh $files) > pos_out2`
		python training_1gram_features.py $files ../training_files/training_file_1gram
	done;
done;		

#---------making testing feature files-------#
for  folder in $testi
do

	for files in $folder/*.txt

	
	 do
		echo $files
		`echo "bash $path/testapi.sh --input $files --output meta_out2"`
		`echo $(bash $path2/runTagger.sh $files) > pos_out2`
		python training_1gram_features.py $files ../testing_files/gold_testing_1gram
    		
	
	done;
done;
#----------train model-------#
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_1gram ../training_files/training_file_1gram"`

#---testing----#
cut -d' ' -f1-7 ../testing_files/gold_testing_1gram > ../testing_files/testing_file_1gram
cut -d' ' -f8 ../testing_files/gold_testing_1gram > ../testing_files/gold_tags_1gram
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model ../testing_files/testing_file) > ../system_result/system_tags_1gram`

#----accuracy---# 
python accuracy.py ../testing_files/gold_tags_1gram ../system_result/system_tags_1gram
 
 
