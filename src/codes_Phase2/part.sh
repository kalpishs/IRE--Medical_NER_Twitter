echo """ For testing new feature combinations and evaluating models created from those feature sets """
export java_home=/home/chinmay/Workstation/IRE/Major/mallet   #location of mallet folder from root


echo """ Removing previously used model and training files """
rm ../models/trained_model_part
rm ../training_files/train_part ../system_result/system_part
rm ../testing_files/test_part ../testing_files/gold_part ../testing_files/testing_part


echo """ Cutting custom features from previously developed feature files """
cut -d' ' -f1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,25,28,31 ../testing_files/gold_testing_5gram > ../testing_files/test_part_v2
cut -d' ' -f1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,25,28,31 ../training_files/training_file_5gram > ../training_files/train_part_v2
cut -d' ' -f1-20 ../testing_files/test_part_v2 > ../testing_files/testing_part
cut -d' ' -f21 ../testing_files/test_part_v2 > ../testing_files/gold_part


echo """ Running mallet, creating training model and then testing on test data """
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_part ../training_files/train_part_v2"`
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_part ../testing_files/testing_part) > ../system_result/system_part`


echo """ Getting efficiency statistics from system generated and test-file label files """
python evaluate.py ../testing_files/gold_part ../system_result/system_part
 