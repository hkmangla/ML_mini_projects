#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from email_data import email_text_data
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop("TOTAL",0)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

word_data, poi_data, email_id_data = email_text_data(data_dict)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
word_data = vectorizer.fit_transform(word_data)
word_data = word_data.toarray()
outliers = []
iterations = 0
for i in data_dict:
	for it in range(len(email_id_data)):
		flag = False
		if data_dict[i]['email_address'] == email_id_data[it]:
			flag = True
			string = 'f'
			counter = 1
			for feature in range(len(word_data[it])):
				data_dict[i][string + str(counter)] = word_data[it][feature]
				if iterations == 0:
					features_list.append(string + str(counter))
				counter += 1
			iterations = 1
			break
	if not flag:
		outliers.append(i)
from sets import Set
m = Set()
for i in outliers:
	data_dict.pop(i,0)
for i in data_dict:
	m.add(len(data_dict[i]))
	# print len(data_dict[i])
print m
my_dataset = data_dict
# print len(my_dataset)
### Extract features and labels from dataset for local testing

data = featureFormat(my_dataset, features_list,sort_keys = True,remove_all_zeroes=False)
# print data
labels, features = targetFeatureSplit(data)
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

clf = DecisionTreeClassifier()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

clf.fit(features_train, labels_train)







### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
