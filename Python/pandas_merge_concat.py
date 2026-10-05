
import pandas as pd
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2']) 

dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])
print(df2.columns)
df1['city']='Pune'
df2['city']="mumbai"

print(df1,df2)
''' df1:
 id Feature1 Feature2  city
0  1        A        B  Pune
1  2        C        D  Pune
2  3        E        F  Pune
3  4        G        H  Pune
4  5        I        J  Pune
'''

df3=pd.concat([df1,df2],ignore_index=True)
print(df3.loc[0]) # shows 1st row

print(df3)

dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df4 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])
print(df4)

# Joins
df5=pd.merge(df3,df4,on="id",how="outer")
print(df5)
df6=pd.merge(df3,df4,on="id",how="inner")
print(df6)
df7=pd.merge(df3,df4,on="id",how="right")
print(df7)
df8=pd.merge(df3,df4,on="id",how="left")
print(df8)

#df5=pd.merge(df3,df4,left_on="id",right_on="myid",how="outer")










