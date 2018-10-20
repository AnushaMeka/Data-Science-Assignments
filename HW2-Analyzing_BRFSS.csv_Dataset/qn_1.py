#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:03:38 2018

@author: anusha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


#===========================  3(a) ============================
print("========================  3(a) ===========================")


experiments = np.random.binomial(n=100, p=0.5, size=10**5)
plt.close('all')
plt.hist(experiments, bins=range(min(experiments), max(experiments)))
plt.xlabel('heads count')
plt.ylabel('frequency')
plt.show()
plt.close('all')
experiments_sort = np.sort(experiments)
dataCdf = np.linspace(0,1,len(experiments_sort))
plt.plot(experiments_sort, dataCdf)
plt.gca().set_yscale('linear')
plt.title('coin simulation')
plt.xlabel('heads count')
plt.ylabel('probability')
plt.show()

#========================  3(b) ===========================
print("========================  3(b) ===========================\n\n")


def binom_dist_cdf():
    k = 0
    binom_cdf_result = []
    for a in range(11):
        binom_cdf_result.append(scipy.stats.binom.cdf(k, 100, 0.5))
        k += 10
    #print(binom_cdf_result)
    return binom_cdf_result
k=0
result = []
def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr
for i in range(11):
    result.append(count_range_in_list(experiments_sort, 0, k))
    k = k+10
result[:] = [x / 100000 for x in result]
plt.close('all')
plt.xscale('log')
plt.yscale('log')
plt.plot(binom_dist_cdf(), result, 'o-b')
plt.title('Theoritical vs Simulation Probabilities')
plt.xlabel('Theoritical probabilities (log scale)')
plt.ylabel('Simulation probabilities (log scale)')
plt.show()
    
#========================  3(c) =============================
print("========================  3(c) =============================\n\n")


plt.close('all')
scipy.stats.probplot(experiments_sort, dist="norm", plot=plt)
plt.title('normal probability plot for heads count')
plt.ylabel('heads count')
plt.show()


#==========================  3(d) ============================
print("========================  3(d) =============================\n\n")

def norm_dist_cdf():
    k = 0
    norm_cdf_result = []
    for a in range(11):
        norm_cdf_result.append(scipy.stats.norm.cdf(k,50,5))
        k += 10
    return norm_cdf_result

plt.close('all')
plt.yscale('log')
x = np.linspace(-5, 5, 11)
binom_cdf = binom_dist_cdf()
normal_cdf = norm_dist_cdf()
plt.plot(x,binom_cdf,'o-', label='binomCDF', color='red')
plt.plot(x,normal_cdf,'o-', label='normalCDF', color='blue')
plt.xlabel('heads count')
plt.ylabel('CDF')
plt.title('normal distribution')
plt.legend()
plt.show()




