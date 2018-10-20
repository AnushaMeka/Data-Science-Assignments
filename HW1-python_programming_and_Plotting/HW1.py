# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:01:48 2017
HW1 Code Skeleton
@author: Jianhua Ruan
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

### 2a Complete the following two functions to implement merge sort

def merge(a, b):
    """Given two non-decreasingly sorted list of numbers, 
       return a single merged array in non-decreasing order
    """
    output_list = []
    while (len(a) != 0) and (len(b) != 0):
        if a[0] < b[0]:
            output_list.append(a[0])
            a.pop(0)
        else:
            output_list.append(b[0])
            b.pop(0)
    if len(a) == 0:
        output_list += b
    else:
        output_list += a
    return output_list
   

def mergeSort(inputArray):
    """
    Given a list of numbers in order order, 
    return a new list sorted in non-decreasing order, 
    and leave the original list unchanged.
    """
    if (len(inputArray) <= 1):
        return inputArray
    else:
        mid = int(len(inputArray)/2)
        sortedList =  merge(mergeSort(inputArray[:mid]), mergeSort(inputArray[mid:]))
        return sortedList


def summaryStatistics(listOfNums):
    """Givne a list of numbers in random order, return the summary statistics 
    that includes the max, min, mean, population standard deviation, median,
    75 percentile, and 25 percentile.
    """  
    #mean
    sum = 0
    for item in listOfNums :
        sum = sum + item
    meanVal =  sum/len(listOfNums)
    
    #median
    length = len(listOfNums)
    sortlist = sorted(listOfNums)
    if (length % 2) == 0 :
        b = length/2
        a = (length-2)/2
        medianVal = (sortlist[int(a)] + sortlist[int(b)])/2
    else:
        medianVal = sortlist[math.floor(length/2)]
        
    #min element
    minVal = listOfNums[0]
    for item in listOfNums[1: ] :
        if(item < minVal) :
            minVal = item
    
    #max element
    maxVal = listOfNums[0]
    for item in listOfNums[1: ] :
        if(item > maxVal) :
            maxVal = item
            
    #standard deviation
    squareList = []
    sum = 0
    for item in listOfNums :
        squareList.append((item - meanVal)**2)
    for item in squareList :
        sum = sum + item
    meanOfSquares =  sum/len(squareList)
    stdev = meanOfSquares**0.5
        
    #25th and 75th percentile   
    listLen = len(sortlist)
    x = math.floor((listLen-1)/2)
    if ((listLen%2) !=0) :
        if (x%2 != 0) :
            perc25 = sortlist[math.floor(x/2)]
            perc75 = sortlist[math.ceil((x+listLen)/2)]
        else:
            perc25 = (sortlist[math.floor((x-1)/2)] + sortlist[math.ceil((x-1)/2)])/2
            perc75 = (sortlist[math.floor((x+listLen)/2)] + sortlist[math.ceil((x+listLen+1)/2)])/2
    else:
        if (x%2 != 0) :
            perc25 = (sortlist[math.floor(x/2)] + sortlist[math.ceil(x/2)])/2
            perc75 = (sortlist[math.floor((x+listLen)/2)] + sortlist[math.ceil((x+listLen)/2)])/2
        else:
            perc25 = sortlist[math.floor(x/2)]
            perc75 = sortlist[math.ceil((x+listLen)/2)]
    
    
    return {'mean' : meanVal,
            'median' : medianVal,
            'min' : minVal,
            'max' : maxVal,
            'std' : stdev,
            'perc25' : perc25,
            'perc75' : perc75}


def scaleToInt(listOfNums):
    """Given a list of real numbers in any range, scale them to be integers
    between 0 and 15 (inclusive). For each number x in the list, the new number
    is computed with the formula round(15 * (x-min) / (max-min))
    """
 
    newList = []  
    for item in listOfNums :
        newList.append(round(15*(item-min(listOfNums))/(max(listOfNums)-min(listOfNums))))
    return newList  
        
def myHistWithRescale(listOfNums):
    """Givne a list of real numbers in any range, first scale the numbers to
    inters between 0 and 15 (inclusive), then return the number of occurrences
    of each integer in a list
    """
    scaledData = scaleToInt(listOfNums)
    counts = dict(Counter(scaledData))
    counts = dict(sorted(counts.items()))
    return counts


## This if statement makes sure that the following code will be executed only 
## if you are running it as a script (rather than loading it as a module).
if __name__ == '__main__':
   
    import random
    
    # Testing merge sort
    
    a = [random.randint(0, 20) for _ in range(10)]
    
    b = mergeSort(a)
    
    print('random array is: ', a)
    print('sorted array is: ', b)
    print('mergeSort is', 'correct' if b == sorted(a) else 'incorrect')
    
    # Generate three sets of random data
    
    listA = [random.gauss(5, 3) for _ in range(1000)]
    listB = [10*random.random() for _ in range(1000)]
    listC = [math.exp(random.gauss(1, 0.5)) for _ in range(1000)]
    

    # testing summaryStatistics
    ssA = summaryStatistics(listA)    
    ssB = summaryStatistics(listB)    
    ssC = summaryStatistics(listC)    
        
    
    print("Summary statistics for data set A: \n", ssA)
    print("Summary statistics for data set B: \n", ssB)
    print("Summary statistics for data set C: \n", ssC)
            


# 3a complete the following code to plot the summary statistics of 
# the above data using Fig 1 in HW1 as a template
    
all_list = [list(ssA.values()),list(ssB.values()),list(ssC.values())]
params_lst = []
for i in range(0,7) :
    params_lst.append([x[i] for x in all_list])
m_plus_std = [x + y for x,y in zip(params_lst[0] , params_lst[4])]
m_minus_std = [x - y for x,y in zip(params_lst[0] , params_lst[4])]
x = [1,2,3]

plt.close('all')
plt.figure(figsize=(10,5))
plt.xticks([1, 2, 3, 4], ['DataA', 'DataB', 'DataC', 'DataD'])
plt.yticks(np.arange(-2.5, 20, step=2.5))
plt.xlabel("Data")
plt.ylabel("Value")
    
plt.scatter(x, params_lst[0] , color='blue', marker='+', label="mean")
plt.scatter(x, params_lst[1] , color='blue', marker='x', label="median")
plt.scatter(x, params_lst[2] , color='black', marker='v', label="min")
plt.scatter(x, params_lst[3] , color='black', marker='^', label="max")
plt.scatter(x, m_plus_std , color='red', marker='<', label="mean+std")
plt.scatter(x, m_minus_std , color='red', marker='>', label="mean-std")
plt.scatter(x, params_lst[5] , color='green', marker='^', label="perc25")
plt.scatter(x, params_lst[6] , color='green', marker='v', label="perc75")
y = [1,2,3,4]
empty_list = [-3,-3,-3,-3]
plt.scatter(y, empty_list , color='white', marker='.')
plt.legend()
plt.xticks([1,2,3])
plt.show()
    

    
    

# testing 2c, count the number of occurrences of each 
# integer in resaled data, 
countA = myHistWithRescale(listA)
countB = myHistWithRescale(listB)
countC = myHistWithRescale(listC)

    
print (countA)
print (countB)
print (countC)
    

# 3b. complete the following code to plot the counts using Fig 2 in HW1 
# as a template
    
    
plt.close('all')    
frequency = [list(countA.values()),list(countB.values()),list(countC.values())]
values = [list(countA.keys()),list(countB.keys()),list(countC.keys())]
plt.figure(figsize=(10,5))
plt.xticks(np.arange(0, 16, step=2))
plt.yticks(np.arange(0, 300, step=50))
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.plot(values[0], frequency[0], color='red', marker='o', linestyle='dotted', label = "Rescaled DataA")
plt.plot(	values[1], frequency[1], color='green', linestyle='solid', label = "Rescaled DataB")
plt.plot(values[2], frequency[2], color='blue', marker='x', linestyle='dashdot', label = "Rescaled DataC")
plt.legend()
plt.show()
