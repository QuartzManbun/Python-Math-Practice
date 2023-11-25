from scipy.stats import t 
from math import sqrt

n = 10 
lower_cv = t(n-1).ppf(.025)
upper_cv = t(n-1).ppf(.975)

print(lower_cv, upper_cv)

# correlation coefficient 
#  derived from data https://bitly/2kf29bd 
r = .957586  

# perform the test 
test_value = r / sqrt((1-r**2) / (n-2))

print("test value: {}".format(test_value))

print("critical range: {}, {}".format(lower_cv, upper_cv))

if test_value < lower_cv or test_value > upper_cv:
    print("Correlation proven, reject H0")
else:
    print("correlation not proven, failed to reject H0")

# calculate p_value 
if test_value > 0: 
    p_value = 1.0 - t(n-1).cdf(test_value)
else:
    p_value = t(n-1).cdf(test_value)

# tow tailed, so multiply by 2
p_value = p_value * 2 
print("Pvalue: {}".format(p_value))
