#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC
#clf = SVC(kernel = "linear")
clf = SVC(kernel = "rbf", C = 10000)

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)

#print pred[50]
print len(features_train)
print len(features_train[0])
print len(labels_train)
print len(features_test)
print len(labels_test)

#cnt1=0
#cnt0=0

#for i in range(len(pred)):
#    if pred[i] == 1:
#           cnt1 = cnt1 + 1
#    else:
#           cnt0 = cnt0 + 1           
#print cnt1
#print cnt0

#########################################################

