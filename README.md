# OPENAQ

Hi, Please perform the following steps in order:

1. Run the API_extract_(first).py file. That will fetch the data through API and save it locally as JSON unders name (OpenAQ_data.json). 
   Also a CSV file(OpenAQ_data.csv) is created as a part of pandas dataframes with the parameters as columns followed by measured values.


2. Run the EDA_histogram_(second).py file. That will output a pdf file(Histogram.pdf) containg 2x2 subplots histograms of each of PM25, PM10, CO, O3.


3. Run the P-corr_(third).py file. The file runs the Pearson’s Correlation between the parameters. The output is P-Coefficient_(third).pdf file, contains the scatter plot with
   the correlation coefficient.

Results:
a) Measured PM25 and PM10 clearly shows a correlation with a value of 0.693. This could change depending on the time when this code run as it will include recent data.
b) There is no other significant correlation found.



P.S- NO2 and SO2 data were not available. 

Thanks for the opportunity. Look forward to hearing from you.
