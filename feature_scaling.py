
def featureScaling(arr):
    maxi = max(arr);
    mini = min(arr);
    newArr = []
    for i in arr:
        newArr.append(float(i - mini)/(maxi - mini))
    return newArr
from sklearn.preprocessing import MinMaxScaler
import numpy

scaler = MinMaxScaler()

weights = numpy.array([[115.], [140.], [175.0]])
rescaled_weights = scaler.fit_transform(weights)
print rescaled_weights