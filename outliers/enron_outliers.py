#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# print data_dict
for i in data_dict:
	if data_dict[i]["bonus"] == 5600000 or data_dict[i]["bonus"] == 7000000:
		print i
data_dict.pop("TOTAL",0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
# print data
maxSalary = 0
maxBonus = []
### your code below
for i in data:
	maxSalary = max(maxSalary, i[0])
	if i[1] == 5600000 or i[1] == 7000000:
		print i
	maxBonus.append(i[1])
# make visualization 
# maxBonus.sort()
print maxBonus

for point  in data:
	salary = point[0]
	bonus = point[1]
	matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()