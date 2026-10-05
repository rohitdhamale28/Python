# pip install plotly

import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"  # or "iframe", "notebook", etc.

# Line graph
months= ["Jan","Feb","Mar","Apr","May"]
sales=[100,150,120,180,200]

fig= px.line(
    x=months,
    y=sales,
    markers=True,
    title="Monthly Sales")

fig.show()

# Bar graph

products = ["Laptop","Mobile","Tablet","Printer"]
sales1=[50,120,80,40]

barfig = px.bar(
    x=products,
    y=sales1,
    title="Product Sales",
    labels={"x": "Products", "y":"Sales"})

barfig.show()

# Scatter Plot , only plots dots !

products = ["Laptop","Mobile","Tablet","Printer"]
sales1=[50,120,80,40]

barfig = px.scatter(
    x=products,
    y=sales1,
    title="Product Sales",
    labels={"x": "Produc", "y":"Sales"})

barfig.show()

## Using Pandas Dataframe

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Sales":[100,150,120]})

fig = px.line(
    df,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales")

fig.show()


######### using matplotlib

import matplotlib.pyplot as plt

plt.plot(months,sales,marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# To turn on interactive mode we use ion function
#or 

# to see the interactive graph , run this file with below function in terminal 
import matplotlib.pyplot as plt
import time

plt.ion()

x=[]
y=[]
fig,ax=plt.subplots()

for i in range(10):
    x.append(i)
    y.append(i*i)
    
    ax.clear()
    ax.plot(x,y,marker="o")
    ax.set_title("Updating Graph")
    
    plt.pause(0.5)
    
    

#plt.plot(months,sales,marker="o")
#plt.title("Monthly Sales")
#plt.xlabel("Month")
#plt.ylabel("Sales")
plt.ioff()
plt.show()



