#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# k nearest neighbors algorithm
# It's choose the class having majority of votes from its neighbors
from time import time
from sklearn.metrics import accuracy_score
from sklearn import neighbors
clf = neighbors.KNeighborsClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "knn training time:", round(time()-t0,3), "s" # 0.001s 
t1 = time()
pred = clf.predict(features_test)
print "knn prediction time:", round(time()-t1,3), "s" #0.001s
print "knn accuracy_score:", accuracy_score(pred,labels_test)  #0.92

from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "AdaBoost training time:", round(time()-t0,3), "s" # 0.001s 
t1 = time()
pred = clf.predict(features_test)
print "AdaBoost prediction time:", round(time()-t1,3), "s" #0.001s
print "AdaBoost accuracy_score:", accuracy_score(pred,labels_test)  #0.92

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 20)
t0 = time()
clf.fit(features_train, labels_train)
print "Rf training time:", round(time()-t0,3), "s" # 0.001s 
t1 = time()
pred = clf.predict(features_test)
print "Rf prediction time:", round(time()-t1,3), "s" #0.001s
print "Rf accuracy_score:", accuracy_score(pred,labels_test)  #0.92

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "nb training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)

print "nb Prediction time:", round(time()-t1,3), "s"
print "nb accuracy_score:", accuracy_score(labels_test, pred)



from sklearn import svm
clf = svm.SVC(kernel = "rbf", C = 10000)
t0 = time()
clf.fit(features_train,labels_train)

print "svm training time:",round(time()-t0,3),"s" 
t1 = time()
pred = clf.predict(features_test)

print "svm prediction time:", round(time() - t1, 3) ,"s"
print "svm accuracy_score:", accuracy_score(pred, labels_test)


from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf = clf.fit(features_train, labels_train)
print "dt Training time:", round(time()-t0,3), "s"
t1 = time()
pred = clf.predict(features_test)
print "dt prediction time:", round(time()-t1, 3), "s"
from sklearn.metrics import accuracy_score
print "dt accuracy_score: ", accuracy_score(pred, labels_test)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
