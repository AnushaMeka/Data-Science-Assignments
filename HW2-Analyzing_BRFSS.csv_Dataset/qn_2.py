# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:40:53 2018

@author: Anusha
"""

import pandas as pd
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


#====================   4(a) ==========================
print("======================== 4(a) ==========================\n\n")

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

if __name__ == '__main__':
    
    data = pd.read_csv('brfss.csv', index_col=0)

    # data is a numpy array and the columns are age, current weight (kg), 
    # last year's weight (kg), height (cm), and gender (1: male; 2: female).
    data = data.drop('wtkg2',axis=1).dropna(axis=0, how='any').values
    current_weight = list(data[:,1])
    weight_a_yr_ago = list(data[:,2])
    height = list(data[:,3])
    age = list(data[:,0])
    gender = list(data[:,4])
    
    ssA = summaryStatistics(current_weight)
    ssB = summaryStatistics(weight_a_yr_ago)
    ssC = summaryStatistics(height)
   
#code for plotting
all_list = [list(ssA.values()),list(ssB.values()),list(ssC.values())]
params_lst = []
for i in range(0,7) :
    params_lst.append([x[i] for x in all_list])
m_plus_std = [x + y for x,y in zip(params_lst[0] , params_lst[4])]
m_minus_std = [x - y for x,y in zip(params_lst[0] , params_lst[4])]
    

x = [1,2,3]

plt.close('all')
plt.figure(figsize=(10,10))
plt.xticks([1, 2, 3, 4], ['current_weight', 'weight_a_yr_ago', 'height'])
plt.yticks(np.arange(0, 400, step=25))
plt.title("summary statistics")
plt.xlabel("Weights and Heights")
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
empty_list = [0,0,0,0]
plt.scatter(y, empty_list , color='white', marker='.')
plt.legend()
plt.xticks([1,2,3])
plt.show()



#======================== 4(b) ==========================
print("======================== 4(b) ==========================\n\n")


weight_change = [x1 - x2 for (x1, x2) in zip(current_weight, weight_a_yr_ago)]
print ("corrcoef values of weight_change vs cuurent_weight, weight_yr_ago, age are : ")
print (np.corrcoef(weight_change,current_weight)[0][1])
print (np.corrcoef(weight_change,weight_a_yr_ago)[0][1])
print (np.corrcoef(weight_change,age)[0][1])
print ("Few times it is taking little bit of time for scatter plot \nPlease be patient...")

def zscore(numArray): 
    return (numArray - np.mean(numArray))/np.std(numArray)
      
z_weight_change = zscore(weight_change)
z_current_weight = zscore(current_weight)
z_weight_a_yr_ago = zscore(weight_a_yr_ago)
z_age = zscore(age)

plt.close('all')
plt.figure(figsize=(10,10))
plt.scatter(z_weight_change, z_current_weight, color = 'red', label = 'current_weight')
plt.scatter(z_weight_change, z_weight_a_yr_ago, color = 'blue', label = 'wt_a_yr_ago')
plt.scatter(z_weight_change, z_age, color = 'black', label = 'age')
plt.title('weight change vs other parameters')
plt.xlabel('z_weight_change')
plt.ylabel('current_weight,wt year ago, age')
plt.legend()
plt.show()



#==========================  4(c)  ==========================
print("==========================  4(c)  ==========================\n\n")


male_indices = [i for i,x in enumerate(gender) if x == 1]
female_indices = [i for i,x in enumerate(gender) if x == 2]
male_current_weight = []
male_weight_a_yr_ago = []
male_height = []
for item in male_indices:
    male_current_weight.append(current_weight[item])
    male_weight_a_yr_ago.append(weight_a_yr_ago[item])
    male_height.append(height[item])
male_weight_change = [x1 - x2 for (x1, x2) in zip(male_current_weight, male_weight_a_yr_ago)]
mean_male_weight_change = np.mean(male_weight_change)
SEM_male_weight_change = np.std(male_weight_change)/math.sqrt(len(male_weight_change))
print ("male mean weight change is {r}" .format(r=mean_male_weight_change))
print("male SEM weight change is {r}" .format(r=SEM_male_weight_change))


female_current_weight = []
female_weight_a_yr_ago = []
female_height = []
for item in female_indices:
    female_current_weight.append(current_weight[item])
    female_weight_a_yr_ago.append(weight_a_yr_ago[item])
    female_height.append(height[item])
female_weight_change = [x1 - x2 for (x1, x2) in zip(female_current_weight, female_weight_a_yr_ago)]      
mean_female_weight_change = np.mean(female_weight_change)
SEM_female_weight_change = np.std(female_weight_change)/math.sqrt(len(female_weight_change))
print("female mean weight change is {r}" .format(r=mean_female_weight_change))
print("female SEM weight change is {r}" .format(r=SEM_female_weight_change))
x = scipy.stats.ttest_ind(male_weight_change, female_weight_change)
#y = scipy.stats.ttest_ind(male_weight_change, female_weight_change, equal_var = False)
print(x)
#print(y)
plt.close('all')
plt.xticks([0, 1], ['male','female'])
plt.title('error bar for male and female weight change')
plt.ylabel('mean')
plt.xticks([0,1])
plt.errorbar(range(2), [mean_male_weight_change, mean_female_weight_change], [SEM_male_weight_change, SEM_female_weight_change]);
plt.show()
#print("From the above results, There is significant difference between male and female weight change.\n\n")

#===========================  4(e)  ============================
print("==========================  4(e)  ==========================\n\n")

def divide_2_groups(weight_change):
    random.shuffle(weight_change)
    cut = math.floor(len(weight_change)/2)
    list_1 = weight_change[:cut]
    list_2 = weight_change[cut:]
    x = scipy.stats.ttest_ind(list_1, list_2)
    return x

male_weight_height_ratio = []
female_weight_height_ratio = []
for item in male_indices :
    male_weight_height_ratio.append(current_weight[item]/height[item])
for item in female_indices :
    female_weight_height_ratio.append(current_weight[item]/height[item])
mean_male_weight_height_ratio = np.mean(male_weight_height_ratio)
print ("male mean weight height ratio is {r}" .format(r=mean_male_weight_height_ratio))
SEM_male_weight_height_ratio = np.std(male_weight_height_ratio)/math.sqrt(len(male_weight_height_ratio))
print ("male SEM weight height ratio is {r}" .format(r=SEM_male_weight_height_ratio))
mean_female_weight_height_ratio = np.mean(female_weight_height_ratio)
print ("female mean weight height ratio is {r}" .format(r=mean_female_weight_height_ratio))
SEM_female_weight_height_ratio = np.std(female_weight_height_ratio)/math.sqrt(len(female_weight_height_ratio))
print ("female SEM weight height ratio is {r}" .format(r=SEM_female_weight_height_ratio))

x = scipy.stats.ttest_ind(male_weight_height_ratio, female_weight_height_ratio)
#y = scipy.stats.ttest_ind(male_weight_height_ratio, female_weight_height_ratio, equal_var = False)
print("t-test result of male to female wt and ht ratio is {}" .format(x))

weight_height_ratio = [x1/x2 for (x1, x2) in zip(current_weight, height)]
y = divide_2_groups(weight_height_ratio)
print("t-test result of wt and ht ratio of two groups divided randomly is {}" .format(y))
#print(y)
plt.close('all')
plt.xticks([0, 1], ['male','female'])
plt.title('error bar for male and female weight-height ratio')
plt.ylabel('mean')
plt.xticks([0, 1])
plt.errorbar(range(2), [mean_male_weight_height_ratio, mean_female_weight_height_ratio], [SEM_male_weight_height_ratio, SEM_female_weight_height_ratio]);
plt.show()
#print("ratio tests will likewise give a p-value of zero then report it as p<0.001")

#===========================  4(d)  ============================
print("==========================  4(d)  ==========================\n\n")

weight_change = [x1 - x2 for (x1, x2) in zip(current_weight, weight_a_yr_ago)]
result = []
    
def pvalues():
    for i in range(0,1000) :
        y = divide_2_groups(weight_change)
        result.append(y.pvalue)
    return result
print("ttest ind of weight change divided into 2 groups {}\n\n".format(divide_2_groups(weight_change)))

print("It takes lot of time to calculate pvalues for 1000 times. \nPlease be patient........")
z = pvalues()
plt.close('all')
plt.title('distribution of pvalues')
plt.xlabel('pvalues (log scale)')
plt.xscale('log')
plt.hist(z)
plt.show()

    





