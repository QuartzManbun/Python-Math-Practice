import pandas as pd 

# read data into Pandas datafram 
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter = ",")

# print correlations between variables 
correlations = df.corr(method = 'pearson')
print(correlations)

