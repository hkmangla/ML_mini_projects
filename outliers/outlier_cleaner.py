#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error = []
    ### your code goes here
    for i in range(len(net_worths)):
        error.append(abs(net_worths[i][0] - predictions[i][0]))
        # ages[i]
    error.sort()
    error = error[:-9]
    for i in range(len(net_worths)):
        x = abs(net_worths[i][0] - predictions[i][0])
        if( x <= error[len(error)-1]):
            cleaned_data.append((ages[i][0], net_worths[i][0], x))

    return cleaned_data
