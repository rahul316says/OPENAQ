# Data Visulization in form of Histograms. Mean and Standard Deviation are also calculated.

import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy.stats import norm   #To calculate Mean and Standard Deviation

#Getting the CSV data into a pandas dataframe
df= pd.read_csv("OpenAQ_data.csv")

#Creating a 2x2 plot for our four parameters
fig,a =  plt.subplots(2,2,figsize=(20,15))


#PM25
a[0][0].hist(df['PM25'], bins=10, alpha=0.5)
mu, sigma = scipy.stats.norm.fit(df['PM25'])
a[0][0].set_title('PM25', fontsize=20)
a[0][0].text(175, 40, '$\mu$=%.2f, $\sigma$=%.2f' %(mu,sigma), fontsize=15)
a[0][0].tick_params(axis='both', which='both', labelsize=15)


#PM10
a[0][1].hist(df['PM10'], bins=10, alpha=0.5)
mu, sigma = scipy.stats.norm.fit(df['PM10'])
a[0][1].set_title('PM10', fontsize=20)
a[0][1].text(200, 45, '$\mu$=%.2f, $\sigma$=%.2f' %(mu,sigma), fontsize=15)
a[0][1].tick_params(axis='both', which='both', labelsize=15)


#CO
a[1][0].hist(df['CO'], bins=10, alpha=0.5)
mu, sigma = scipy.stats.norm.fit(df['CO'])
a[1][0].set_title('CO', fontsize=20,y=-0.15)
a[1][0].text(1800, 37, '$\mu$=%.2f, $\sigma$=%.2f' %(mu,sigma), fontsize=15)
a[1][0].tick_params(axis='both', which='both', labelsize=15)


#O3
a[1][1].hist(df['O3'], bins=10, alpha=0.5)
mu, sigma = scipy.stats.norm.fit(df['O3'])
a[1][1].set_title('O3', fontsize=20,y=-0.15)
a[1][1].text(85, 70, '$\mu$=%.2f, $\sigma$=%.2f' %(mu,sigma), fontsize=15)
a[1][1].tick_params(axis='both', which='both', labelsize=15)


# adding axes labels
fig.text(0.5,0.04, "Measurement Values", ha="center", va="center", fontsize=20)
fig.text(0.05,0.5, "Counts", ha="center", va="center", rotation=90, fontsize=20)


plt.savefig("Histogram.pdf", dpi=300)

