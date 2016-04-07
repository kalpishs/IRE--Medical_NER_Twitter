for filename in /home/kalpish/Desktop/IRE_major/data/twitter/training_Annotations/anjali/*.ann; do
 cut -d " " -f1,2 $filename >> result
done;
