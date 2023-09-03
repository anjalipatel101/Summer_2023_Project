import csv
from statistics import *
from pandas import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from datetime import datetime

#LUV

#Read the CSV file and convert data stored in the specific column into a list 
luv = []
a = []
data1 = read_csv("LUV.csv")
luv = data1['Low'].tolist()
luv = data1['High'].tolist()
a = data1['Date'].tolist()
luv.sort()

# Calculate the mean
luv_mean = round(mean(luv), 3)

# Calculate the median
luv_median = round(median(luv), 3)

# Calculate the mode
#luv_mode = mode(a)

#Calculate the Standard Deviation
luv_sd = round(stdev(luv), 3)

#Calculate the IQR
q3 = np.quantile(luv, 0.75)
q1 = np.quantile(luv, 0.25)
luv_iqr = round((q3 - q1),3)

# Print the results
print("\nLUV:   Mean:", luv_mean, " Median:", luv_median, " Standard Deviation:", luv_sd, "  IQR:", luv_iqr)



#################################################

#UAL

#Read the CSV file and convert data stored in the specific column into a list 

ual = []
x = []
data2 = read_csv("UAL.csv")
ual = data2['Low'].tolist()
ual = data2['High'].tolist()
x = data2['Date'].tolist()
ual.sort()

# Calculate the mean
ual_mean = round(mean(ual), 3)

# Calculate the median
ual_median = round(median(ual), 3)

# Calculate the mode
#ual_mode = round(mode(ual), 3)


#Calculate the Standard Deviation
ual_sd = round(stdev(ual), 3)

#Calculate the IQR
q3 = np.quantile(ual, 0.75)
q1 = np.quantile(ual, 0.25)
ual_iqr = round((q3 - q1),3)



# Print the results
print("UAL:   Mean:", ual_median, "  Median:", ual_median, " Standard Deviation:", ual_sd, " IQR:", ual_iqr)


#Correlation Coefficient
r = round(pearsonr(luv,ual)[0],5)
print("\nCorrelation Coefficient:", r)

#P-value
p = round(pearsonr(luv,ual)[1], 5)
print("Augmented Dicky Fuller Test -> P-value:", p, "\n")

if p < 0.05:
    print("Since the P-value =", p, ", and", p, "is less than 0.05, the two stocks are cointegrated!\n")


print("____________________________________________________________________________")

#General Statistics
print("\nLUV DATA STATS\n")
print(data1.describe())
print("\nUAL DATA STATS\n")
print(data2.describe())

#Graph setup and data generation
prompt = input('\nDo you want to view the graph? Type yes or no.')

dates1 = []
values1 = []
dates2 = []
values2 = []

with open('LUV.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists

    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')  # Assuming date format as YYYY-MM-DD
        value = float(row[1])  # Assuming the data value is in the second column
        dates1.append(date)
        values1.append(value)

        
with open('UAL.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists

    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')  # Assuming date format as YYYY-MM-DD
        value = float(row[1])  # Assuming the data value is in the second column
        dates2.append(date)
        values2.append(value)


if prompt == "yes" or "y" or "YES" or "Yes":
    
    #Plots each stock
    plt.plot(dates1, values1, color = 'red', label = 'LUV' )
    plt.plot(dates2, values2, color = 'cornflowerblue', label = 'UAL' )
    
    #Creates a legend for easy reference
    plt.legend(['LUV = Southwest Airlines', 'UAL = United Airlines'])

    #Labels the graph
    plt.xlabel('Date Progression')
    plt.ylabel('Stock Price')
    plt.title ('Pair Trading Analysis')
    plt.xticks(rotation=45)
    plt.show()
else:
    exit()        


