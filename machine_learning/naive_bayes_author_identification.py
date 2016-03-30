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