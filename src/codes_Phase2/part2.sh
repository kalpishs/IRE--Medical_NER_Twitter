echo """ For testing new feature combinations and evaluating models created from those feature sets """
export java_home=/home/chinmay/Workstation/IRE/Major/mallet-deps    #location of mallet folder from root

echo """ Cutting custom features from previously developed feature files """
cut -d' ' -f1,3,18,19,21,22,24,25,27,28,30,31 ../testing_files/gold_testing_5gram > ../testing_files/test_part_v1
cut -d' ' -f1,3,18,19,21,22,24,25,27,28,30,31 ../training_files/training_file_5gram > ../training_files/train_part_v1
cut -d' ' -f1-11 ../testing_files/test_part_v1 > ../testing_files/testing_part_v2
cut -d' ' -f12 ../testing_files/test_part_v1 > ../testing_files/gold_part_v2

echo """ Running mallet, creating training model and then testing on test data """
`echo "java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/trained_model_part_v2 ../training_files/train_part_v1"`
`echo $(java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_part_v2 ../testing_files/testing_part_v2) > ../system_result/system_part_v2`


echo """ Getting efficiency statistics from system generated and test-file label files """
python evaluate.py ../testing_files/gold_part_v2 ../system_result/system_part_v2
 