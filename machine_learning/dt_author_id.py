Skip to content
This repository  
Search
Pull requests
Issues
Gist
 @CharlesCrous
 Unwatch 1
  Star 1
  Fork 1 CharlesCrous/springboard_data-science-intensive
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathspringboard_data-science-intensive/machine_learning/decision_tree/dt_author_id.py
1ab6fd4  18 days ago
@CharlesCrous CharlesCrous add decision tree mini-project
1 contributor
RawBlameHistory     49 lines (33 sloc)  1.34 KB
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
print "number of features: ", len(features_train[0])

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)

#added to sample 1% of original dataset for faster results
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)  
print "training time:", round(time()-t0, 3), "s"

t0 = time()
y_pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, y_pred)
print "accuracy score:", accuracy
Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help