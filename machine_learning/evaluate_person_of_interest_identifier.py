#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../ud120-projects-master/final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# train-test split
features_train, features_test, labels_train, labels_test = train_test_split(features, 
	labels, test_size=0.3, random_state=42) 

print(labels_test)

# classifier
clf = tree.DecisionTreeClassifier()

clf.fit(features_train, labels_train)  

y_pred = clf.predict(features_test)

# performance measures
accuracy = accuracy_score(labels_test, y_pred)
precision= precision_score(labels_test, y_pred)
recall = recall_score(labels_test, y_pred)
print "accuracy score:", accuracy
print "precision score:", precision
print "recall score:", recall


