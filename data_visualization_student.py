# -*- coding: utf-8 -*-

#@title Loading in our data and importing necessary packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Our data is stored on Google Cloud.
# We can use a command like this to upload it into Google Colab's file system
!wget -q --show-progress "https://storage.googleapis.com/inspirit-ai-data-bucket-1/Data/AI%20%2B%20X/Independent/Main%20Curriculum/Numerical%20Data%20Preprocessing/weather_costs.csv"

# Let's load in our dataset as a pandas dataframe
weather_data = pd.read_csv("new_tokyo.csv")


weather_data.head(5)


weather_data.shape

import numpy as np

np.mean(weather_data['tempmax'])


# YOUR CODE HERE
np.std(weather_data['tempmax'])

# YOUR CODE HERE
weather_data.describe()

max_bmi = '' #@param {type:"string"}
min_charges = '' #@param {type:"string"}
median_children = '' #@param {type:"string"}
std_bmi = '' #@param {type:"string"}

if max_bmi:
  if int(float(max_bmi)) == int(float("53.13")):
    print("max_bmi Correct!")
  else:
    print("max_bmi Incorrect! Try Again!")
else:
  print("Enter a value for max_bmi.")

if min_charges:
  if int(float(min_charges)) == int(float("1121.8739")):
    print("min_charges Correct!")
  else:
    print("min_charges Incorrect! Try Again!")
else:
  print("Enter a value for min_charges.")

if median_children:
  if int(float(median_children)) == int(float("1.0")):
    print("median_children Correct!")
  else:
    print("median_children Incorrect! Try Again!")
else:
  print("Enter a value for median_children.")

if std_bmi:
  if int(float(std_bmi)) == int(float("6.1288")):
    print("std_bmi Correct!")
  else:
    print("std_bmi Incorrect! Try Again!")
else:
  print("Enter a value for std_bmi.")

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(weather_data['tempmax'], edgecolor = 'black')
plt.xlabel('tempmax')
plt.show()


import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.hist(weather_data['feelslikemin'], edgecolor='black', bins=20)
plt.xlabel('FeelsLikeMin')
plt.title('FeelsLikeMin Distribution')

plt.subplot(132)
plt.hist(weather_data['solarenergy'], edgecolor='black', bins=10)
plt.xlabel('SolarEnergy')
plt.title('SolarEnergy Distribution')

plt.subplot(133)
plt.hist(weather_data['uvindex'], edgecolor='black', bins=20)
plt.xlabel('Uvindex')
plt.title('Uvindex Distribution')

plt.tight_layout()

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.boxplot(x=weather_data['precip'], color='skyblue')

plt.title('Boxplot of PRECIP in Weather Data')
plt.xlabel('PRECIP')

plt.show()


plt.figure(figsize=(12,10))
sns.scatterplot(weather_data['bmi'], weather_data['charges'])
plt.show()


plt.figure(figsize=(12,10))
sns.scatterplot(weather_data['bmi'], weather_data['charges'], hue=weather_data['sex'])
plt.show()