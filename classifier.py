# Classifier using naive bayes

from sklearn.naive_bayes import GaussianNB
def classifier(features_train, label_train):
	clf = GaussianNB()
	clf.fit(features_train,label_train)
	return clf
classifier([1,2,3], [1,2,3])

#Classifier using SVM(support vector machine)

from sklearn import svm
clf_svm = SVC(kernel = "linear")
clf_svm.fit(features_train,label_train)
clf_svm.predict(features_test)