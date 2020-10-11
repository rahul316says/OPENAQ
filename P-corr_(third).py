#From Histogram.pdf, PM25 PM10 and CO forming a gaussian distribution. We can use Pearson's algorithm to find Pearson correlation coefficient.

'''
The Pearson correlation coefficient can be used to summarize the strength of the linear relationship between two data samples.
It is calculated as the covariance of the two variables divided by the product of the standard deviation of each data sample.
It is the normalization of the covariance between the two variables to give an interpretable score.

Pearson's correlation coefficient = covariance(X, Y) / (stdv(X) * stdv(Y))

The coefficient returns a value between -1 and 1 that represents the limits of correlation from a full negative correlation to
a full positive correlation.
A value of 0 means no correlation. The value must be interpreted, where often a value below -0.5 or above 0.5 indicates a notable
correlation, and values below those values suggests a less notable correlation.
'''

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr   #package for calculating Pearson's correlation coefficient


# Getting the CSV data into a pandas dataframe
df= pd.read_csv("OpenAQ_data.csv")

#Creating a 2x2 plot for our four parameters
fig,a =  plt.subplots(2,2,figsize=(20,15))


# Calculate Pearson's Correlation
# PM25 vs PM10
corr1,_  = pearsonr(df['PM25'], df['PM10'])
a[0][0].scatter(df['PM25'],df['PM10'])
a[0][0].text(175, 300, 'corr=%.3f' %(corr1), fontsize=15)
a[0][0].tick_params(axis='both', which='both', labelsize=15)
a[0][0].set_xlabel('PM25',fontsize=20)
a[0][0].set_ylabel('PM10',fontsize=20)

# PM25 vs CO
corr2,_  = pearsonr(df['PM25'], df['CO'])
a[0][1].scatter(df['PM25'],df['CO'])
a[0][1].text(175,2500, 'corr=%.3f' %(corr2), fontsize=15)
a[0][1].tick_params(axis='both', which='both', labelsize=15)
a[0][1].set_xlabel('PM25',fontsize=20)
a[0][1].set_ylabel('CO',fontsize=20)

# PM10 vs CO
corr3,_  = pearsonr(df['PM10'], df['CO'])
a[1][0].scatter(df['PM10'], df['CO'])
a[1][0].text(1, 2500, 'corr=%.3f' %(corr3), fontsize=15)
a[1][0].tick_params(axis='both', which='both', labelsize=15)
a[1][0].set_xlabel('PM10',fontsize=20)
a[1][0].set_ylabel('CO',fontsize=20)



fig.delaxes(a[1][1])  #deletes the last unused subplot
plt.savefig("P-Coefficient_(third).pdf", dpi=300)

