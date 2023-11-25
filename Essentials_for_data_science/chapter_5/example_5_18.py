import pandas as pd 

# read data into pandas datafram 
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# print correlations between variables 
coeff_determiination = df.corr(method ='pearson')**2
print(coeff_determiination)

