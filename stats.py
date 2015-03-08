import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#mean
print "The mean of alcohol for the Alcohol and Tobacco dataset is {0}".format(df['Alcohol'].mean())
print "The mean of tobacco for the Alcohol and Tobacco dataset is {0}".format(df['Tobacco'].mean())
print

#median
print "The median of alcohol for the Alcohol and Tobacco dataset is {0}".format(df['Alcohol'].median())
print "The median of tobacco for the Alcohol and Tobacco dataset is {0}".format(df['Tobacco'].median())
print

#mode
print "The mode of alcohol for the Alcohol and Tobacco dataset is {0}".format(stats.mode(df['Alcohol'])[0][0])
print "The mode of alcohol for the Alcohol and Tobacco dataset is {0}".format(stats.mode(df['Tobacco'])[0][0])
print

#range
print "The range of alcohol for the Alcohol and Tobacco dataset is {0}".format(max(df['Alcohol']) - min(df['Alcohol']))
print "The range of tobacco for the Alcohol and Tobacco dataset is {0}".format(max(df['Tobacco']) - min(df['Tobacco']))
print

#variance
print "The variance of alcohol for the Alcohol and Tobacco dataset is {0}".format(df['Alcohol'].var())
print "The variance of tobacco for the Alcohol and Tobacco dataset is {0}".format(df['Tobacco'].var())
print

#std dev
print "The standard deviation of alcohol for the Alcohol and Tobacco dataset is {0}".format(df['Alcohol'].std())
print "The standard deviation of tobacco for the Alcohol and Tobacco dataset is {0}".format(df['Tobacco'].std())
