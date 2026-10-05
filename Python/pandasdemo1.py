import pandas as pd


#DataFrame    DataSeries

df=pd.read_table('http://bit.ly/chiporders')

print(df.shape) #(rows,columns)
s=df['item_name'] #print column in Series format , [in series , the index can be char(a,b,c...) also . unlike in numpy arry the index is standard strating with (0,1,2..)]

print(type(s))



s=df[['item_name']] #print item_name column in DataFrame format
print(type(s))
print(df.columns)  #print all column names

print(df.head())  #prints first 5 lines
print(df.tail())  #prints last 5 lines

print(df.head(12))  #prints first 12 lines
print(df.tail(7))  #prints last 7 lines

print(df.iloc[0:4,1:3])  #to retrieve data by integer position
                         #row :[0:4] : display rows 0,1,2,3 
                         #col :[1:3] : display cols 1,2 
#it will exclude 7th row
#display rows from 0-6 and columns 1 onward all
print(df.iloc[0:7,1:])

#store all columns except the last column
df1=df.iloc[:,:-1]

#It will not exclude 6 th row
print(df.loc[2:6,['order_id','item_name']]) # " loc " is by location it will include 6 th row also

print(df.info())

print(df[['order_id','quantity']].mean())  #to calculate columnwise mean
print(df.iloc[:,:2].mean())  #to calculate columnwise mean
print(df[['order_id','quantity']].std())
print(df[['order_id','quantity']].median())
print(df[['order_id','quantity']].max())

print(df.describe()) #all statistical measures for all integer columns
print(df.info())  #how many not null values and data type of all columns
# OP: print(df.info()) 
"""
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   order_id            4622 non-null   int64
 1   quantity            4622 non-null   int64
 2   item_name           4622 non-null   str  
 3   choice_description  3376 non-null   str  
 4   item_price          4622 non-null   str  
 
"""

#   item_price : type-> str ('$10'), to convert it to float for calculations , first we are replacing '$' by '0' , n then convert to float

df['item_price1']=df['item_price'].map(lambda x:x.replace('$','0')) #to replace $ with 0

df['item_price2']=df['item_price1'].astype('float') 
 #to convert from object data type to int
 
print(df.info())
# OP: print(df.info()) after converting  item_price to float
"""
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   order_id            4622 non-null   int64  
 1   quantity            4622 non-null   int64  
 2   item_name           4622 non-null   str    
 3   choice_description  3376 non-null   str    
 4   item_price          4622 non-null   str    
 5   item_price1         4622 non-null   str     item_price  
 6   item_price2         4622 non-null   float64
 
"""




df['discounted_price']=df['item_price2']*0.85  #add new column

df.pop('choice_description') # to delete the column

print(df[df['discounted_price']>3]) # Print items with discount price >3

#  gives u the indexes (row no.) where the 'discounted_price'>3
index_nm=df[df['discounted_price']>3].index
print(index_nm,len(index_nm))
df.drop(index_nm,inplace=True)  #drop all rows with discounted_price > 3 and ovewrite the original frame
df.drop([2,3,4],axis=0,inplace=True) #drop rows [2,3,4]
# axis=0, by default , axis is 0


pd.unique(df['item_price'])
df1=(df['item_price']).value_counts() #frequency of each distinct value
df1.shape
import matplotlib.pyplot as plt
plt.pie(df1,labels=df1.index,shadow=True,startangle=90,rotatelabels = 270)




