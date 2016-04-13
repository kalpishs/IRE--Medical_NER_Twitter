export java_home=/home/chinmay/Workstation/IRE/Major/mallet
rm ../models/trained_model_part
rm ../training_files/train_part ../system_result/system_part
rm ../testing_files/test_part ../testing_files/gold_part ../testing_files/testing_part

cut -d' ' -f1-24 ../testing_files/gold_testing_5gram_v1 > ../testing_files/test_part_v2
cut -d' ' -f1-24 ../training_files/training_file_5gram_v1 > ../training_files/train_part_v2
cut -d' ' -f1-23 ../testing_files/test_part_v2 > ../testing_files/testing_part
cut -d' ' -f24 ../testing_files/test_part_v2 > ../testing_files/gold_part
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_part ../training_files/train_part_v2"`
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_part ../testing_files/testing_part) > ../system_result/system_part_v2`

#----accuracy---# 
python evaluate.py ../testing_files/gold_part ../system_result/system_part
 