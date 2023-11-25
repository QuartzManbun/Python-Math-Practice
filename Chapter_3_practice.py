# from math import sqrt
# from scipy.stats import norm, t
# import random

# # mean = 64.43
# # std_dev = 2.99

# # x = norm.cdf(66, mean, std_dev) - norm.cdf(62, mean, std_dev) 
# # print(x)


# # # Random numbers--------------------

# # # def normal_pdf(x: float, mean: float, std_dev: float) -> float: 
# # #     return ( 1.0/(2.0*math.pi * std_dev **) **.5) *  math.exP(-1.*((x-mean)**2 / (2.0* std_dev **2)))


# # # for i in range(0,1000):
# # #     random_p = random.uniform(0.0, 1.0) 
# # #     random_weight = norm.ppf(random_p, loc=64.43, scale=2.99)
# # #     print(random_weight)

# # # Z-Scores: --------------------

# # def z_score(x, mean, std):
# #     return (x-mean) / std

# # def z_to_x(z, mean, std):
# #     return (z * std) + mean 

# # mean = 140000
# # std_dev = 3000
# # x = 150000

# # z = z_score(x, mean, std_dev) 
# # back_to_x = z_to_x(z, mean, std_dev)

# # print("z-score: {}".format(z))
# # print("back to X: {}".format(back_to_x))

# # def critical_z_value(p):
# #     norm_dist = norm(loc = 0.0, scale = 1.0);
# #     left_tail_area = (1.0 - p) / 2.0 
# #     upper_area = 1.0 - ((1.0 - p)/2.0)
# #     return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

# # def confidence_interval(p, sample_mean, sample_std, n ): 
# #     lower, upper = critical_z_value(p)
# #     lower_ci = lower * (sample_std / sqrt(n))
# #     upper_ci = upper * (sample_std / sqrt(n))
# #     return sample_mean + lower_ci, sample_mean + upper_ci
# # print(confidence_interval(p = .95, sample_mean=64.408, sample_std= 2.05, n=31))
    


# # Calculating the probability of recovery between 15 and 21 days 
# # cold has 18 day mean recover time, 1.5 st dev
# # mean = 18 
# # std_dev = 1.5 

# # # what x-value has 5% of are abehind it?  
# # x=norm.ppf(.05, mean, std_dev)
# # print(x)

# # this is using a p-value of .05, the minimum standard for statistical significance.  Thus, the drug woud have to have a recovery time of 15.53 or less to show statistically significant reduction in recovery.    You only need the one tail test, as the drug is not intended to EXTEND recovery time.  

# # CALCULATING THE ONE TAILED P-VALUE 

# # PROBABILITY OF 16 OR LESS DAYS 
# # p_value = norm.cdf(16, mean, std_dev)
# # print(p_value)

# # # Speaking in mathematics- we have a p-value of .05 or less to yield significance.  Our calculated p-value is .0912, and thsu it is not statistically significant.  

# # CALCULATING A RANGE FOR A STATISTICAL SIGNIFICANCE OF 5% 

# # what x-value has a 2.5% chance of area behind it?  
# # x1 = norm.ppf(.025, mean, std_dev)

# # # what x-value has a 97.5% chance of area behind it?  
# # x2 = norm.ppf(.975, mean, std_dev)

# # print(x1) 
# # print(x2) 

# # the retruned values are 15.060 and 20.9399.  Thus, the drug test group x-vaue of 16  does not meet statistical significance, as it is not outside of these bounds.  

# # CALCULATING THE TWO TAILED P-VAUE 
# # mean = 18 
# # std_dev = 1.5  

# # # probability of 1 o less days)  
# # p1 = norm.cdf(16, mean, std_dev)

# # # probabiltiy of 20 or more days
# # p2 = 1- norm.cdf(20, mean, std_dev)

# # # p-value of both tails 
# # p_value = p1 + p2 
# # print(p_value)

# # GETTING A CRITICAL VALUE RANGE WITH T-DISTRIBUTION:

# # n = 25 
# # lower = t.ppf(.025, df =n-1)  
# # upper = t.ppf(.975, df =n-1)
# # print(lower, upper) 

# # CHAPTER 3 EXERCISE 1
# # caliper_list = [1.78, 1.75, 1.72, 1.74, 1.77]
# # easier_list = [1,2,3]

# # # def mean(data):
# # #     i = 0
# # #     for i in data:
# # #         i+=i
# # #     _mean = i/len(data)
# # #     print(_mean)

# # #     return(_mean)
# # caliper_mean = sum(caliper_list) / len(caliper_list)
# # # print(caliper_mean)

# # def standard_deviation(p):
# #     mean = sum(p)/len(p)
# #     _std_dev = sqrt((sum((i - mean) **2 for i in p)/ len(p)))
# #     return _std_dev
     
# # print(standard_deviation(caliper_list))

# # CHAPTER 3 EXERCISE 2
# # phone_mmean = 42 
# # phone_standard_dev = 8 

# # x1 = norm.cdf(30, phone_mmean,phone_standard_dev)
# # x2 = norm.cdf(20, phone_mmean, phone_standard_dev)

# # phone_probability = x1-x2
# # print(phone_probability)

# # CHAPTER 3 EXDERCISE 3
# # sample_mean = 1.715588
# # sample_std_dev = 0.029252
# # n = 34

# # def critical_z_value(p):
# #     norm_dist = norm(loc = 0.0, scale=1.0)
# #     left_tail_area = (1-p) / 2.0
# #     upper_area = 1.0-((1.0-p)/2.0)
# #     return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

# # def confidence_interval(p, sample_mean, sample_std_dev, n):
# #     lower, upper = critical_z_value(p)
# #     lower_ci = lower * (sample_std_dev / sqrt(n))
# #     upper_ci = upper * (sample_std_dev / sqrt(n))
# #     return sample_mean + lower_ci, sample_mean + upper_ci

# # print(confidence_interval(.99, sample_mean, sample_std_dev, n))

# # CHAPTER 3 EXERCISE 4:
# mean = 10345 
# std_dev = 552 
# add_Campaign_mean = 11461

# p1 = 1 -  norm.cdf(11641, mean, std_dev)
# p2 = p1 

# p_value = p1 + p2 
# print ("two-tailed p-value", p_value)
# if p_value <= .05:
#     print("passes twotailed test")
# else:
#     print("failes two-tailed test")



# # The  following x-values were generated: 9263.09988053389 11426.9001194661, therefore the add campaign had a statistically significant affect.  

