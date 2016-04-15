____________________________________________________________________________________________________________________________________________
Mentor: Nikhil Pattisapu
Project No. : 19
Team No. : 56

By Chinmay Bapna, Juhi Tandon, Kalpish Singhal
____________________________________________________________________________________________________________________________________________

==============================================================================================================================================
 Medical Named Entity on twitter Data
==============================================================================================================================================
Medical Entity Recognition is a crucial step towards efficient medical texts analysis. The task of a Medical Name Entity Recognizer is two fold. ­ 
(i) Identification of entity boundaries in the sentences. 
(ii) Entity categorization. 
Our objective is to extend medical entity  recognition for tweets. 

Medical   entities   can   be   diseases,   drugs,   symptoms,   etc.   Previously,   researchers   in   the   field  have   used   hand   crafted   features   to   identify   medical   entities   in   medical   literature.   It   has   been  found   that   in   contrast   with   semantic   approaches   which   require   rich   domain­ knowledge for rule or pattern construction, statistical approaches are more scalable.


==============================================================================================================================================
		    			 Data set Used
==============================================================================================================================================
# 1 : Twitter data SET for Training and Testing purposes
	We   have   a   dataset   of   1   year   of   tweets   about   4   diseases   and   32   drugs.   A   team   of   domain  experts   has   annotated   about   2000   tweets   with   entities   (around   20   types:   diseases,   drugs,  symptoms) and also relations (around 40 relation types: cures, causes, etc). 

==============================================================================================================================================
                     			 Project Scope
==============================================================================================================================================
This project is mainly focused on feature extraction  of medical entities on the set of tweets. This will be divided into three phases namely.
	(i) Feature Identification and extraction
	(ii) Model training using CRF 
	(iii) Testing using trained model 
	(iv) Evaluating the output obtained for different feature-models using metrics such as Precision, Recall, F-score and Accuracy.
	(v) Selecting some feature models and plot their precision , recall , F-scores for each label

	
==============================================================================================================================================
                    			 List of Files 
==============================================================================================================================================

(i) bash_5gram.sh (Bash script to execute the project files in one-go)
(ii) training_features_5gram.py (main code for constructing feature files)
(iii) metamap.py (for extracting semantic tags from Metamap(tool) generated output)
(iv) pos_tagger.py (for extracting part-of-speech tags from Tweet-NLP(tool) generated output)
(v) ortho.py (for assigning orthographic features)
(vi) cluster.py (for extracting cluster-id tags from Brown-Clustering(algorithm) generated output)
(vii) part.sh (for testing-exploring new feature sets from pre-existing feature file)
(viii) evaluate.py (for testing system generated output on the basis of different evaluation metrics)


==============================================================================================================================================
                    			How to Run  
==============================================================================================================================================
->Install Following Tools:
	1)Mallet :- A Java-based package for statistical natural language processing,text classification and  information extraction tool
	  using Command line scripts.
	  MALLET includes sophisticated tools for document classification: efficient routines for converting text to "features",a wide variety 
	  of algorithms eg. CRF
	  Installation instructions available at http://mallet.cs.umass.edu/
	2)Meta-Map 2013 :- MetaMap is a highly configurable program developed to map biomedical text to the UMLS Metathesaurus or,
	  equivalently, to discover Metathesaurus concepts referred to in text.
	  We have made use of Meta-Map Java-api for making use of this tool to find semantic tags.
	  Installation instructions available at https://metamap.nlm.nih.gov/JavaApi.shtml
	3)Tweet-NLP :-  Provide a tokenizer, a part-of-speech tagger, hierarchical word clusters, and a dependency parser for tweet. We used
	  it to address the problem of part-of-speech tagging for English data from the popular microblogging service Twitter. The tool 
	  reports tagging results nearing 90% accuracy. 
	  Installation instructions available at http://www.cs.cmu.edu/~ark/TweetNLP/
	4)You'll also need to run Brown-CLustering algorithm on both - testing and training data, for this project, we already have stored
	  its output in usable format in the file IRE--Medical_NER_Twitter/data/cluster-50/paths 
	  Code and usage instructions available at https://github.com/percyliang/brown-cluster
 
Download the Project from here, https://github.com/kalpishs/IRE--Medical_NER_Twitter.git
Configure the file bash_5gram.sh in the codes_Phase2 folder in src, with the paths of installed tools, data, etc.
Start the metamap server, for Metamap server Java-api, run bash publc-mm/bin/mmserver13  (public-mm -> Metamap installed directory) 
Execute bash_5gram.sh and voila -> it will run successfully.
This bash script calls, 
All the files mentioned in the previous section sequentially, It also runs commands to get output from different tools such as:
1) bash $path/testapi.sh --input $files --output meta_out      (Running metamap)
2) bash $path2/runTagger.sh $files) > pos_out                  (Running tweet-nlp)
3) java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file ../models/
   trained_model_5gram ../training_files/training_file_5gram   (Running mallet on training data and training model 'trained_model_5gram')
4) java -cp $java_home/class:$java_home/lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file ../models/trained_model_5gram 
   ../testing_files/testing_file_5gram) > ../system_result/system_tags_5gram  	(Running mallet on testing data using trained model)

==============================================================================================================================================
                      			Output FORMAT
==============================================================================================================================================
We have used the BIO(Begin-Inside-Outside)  model for labelling entities. For a whole corpus of tweets, we are labelling data term-wise. This model (BIO) lets us handle entities that span over multiple terms.
For instance, the words “childhood asthma” represent a single entity which is a disease, 
In accordance with our  implementation, the separate words childhood and asthma will be labelled as childhood -> Disease-Begin  and asthma -> Disease-Inside.
So, this is the output format and the corresponding labels are as follows:
{Disease-begin, Disease-inside, Drug-begin, Drug-inside, Symptom-begin, Symptom-inside, None}
So, we basically assign 2 labels (Begin, Inside) per entity (Disease, Drug, Symptom) and 1 extra label (None) representing Outside tag in BIO model.
These labels are the output which are obtained in system generated file by the trained tool.


==============================================================================================================================================
                     			Conclusion
==============================================================================================================================================
The dataset provided to us consists of 85% of ‘None’ entity tags, hence if we label all the terms as none - we’ll have 85% accuracy. This conveys that accuracy is not the correct metric for correct evaluation of feature models.
Since this metric isn’t good-enough to tell us significance of one feature model over another, we tried using more application specific metrics such as Precision, Recall and F-Score. 
In this project we experimented with different feature sets and evaluated their efficiency in NER.

--- The best 3 feature models along with statistic analysis are represented in the presentation available at: link
--- A video demonstrating our work has also been put-up and can be accessesed from: link 

==============================================================================================================================================
                     			Tags
==============================================================================================================================================
'Information Retrieval and Extraction Course', 'IIIT-H', Major Project', 'Mallet', 'Medical NER', 'Feature Sets', 'Disease', 'Drug', 'Symptom', 'Analysis and Approach'




