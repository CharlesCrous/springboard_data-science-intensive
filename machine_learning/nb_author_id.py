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
Branch: master Find file Copy pathspringboard_data-science-intensive/machine_learning/naive_bayes/nb_author_id.py
dd13c9a  20 days ago
@CharlesCrous CharlesCrous add udacity intro to ml
1 contributor
RawBlameHistory     49 lines (31 sloc)  1.14 KB
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 
    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

t0 = time()
clf = gnb.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
y_pred =  clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

y_true = labels_test

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)

print "accuracy score:", accuracy
#########################################################


Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help