# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:17:24 2019

@author: anilk
"""
print("Hello World!");

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import seaborn as sns
# Load the data

tips = sns.load_dataset("tips")
print(tips.shape)
#x=tips["total_bill"]
# Create violinplot

sns.violinplot(x = "total_bill", data=tips)
# Show the plot
plt.show()
'''
print(tips["sex"].value_counts())
x=tips["sex"].value_counts().index
y=tips["sex"].value_counts()
plt.bar(x,y)
plt.show()
'''
#in matplotlib we needed the above line of code , which can be done 1 line shown below , using seaborn
sns.countplot(x="sex",data=tips)

sns.countplot(x="time",hue="sex",data=tips)


sns.boxplot(x="day",y="total_bill",data=tips)

sns.distplot(tips["total_bill"],kde=True,bins=10,color="darkgreen")

sns.set(style="ticks")
sns.histplot(x="total_bill",data=tips,kde=True,bins=10)

sns.countplot(x="smoker",data=tips,hue="sex")

