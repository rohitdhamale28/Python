
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Question 1

col_names = ['movieId', 'title', 'genres']

df1 = pd.read_csv('/home/pgcp-esd/Downloads/PYTHON/movie assignment/movies11.csv')

df2 = pd.read_csv(
    '/home/pgcp-esd/Downloads/PYTHON/movie assignment/movies12.csv', 
    header=None, 
    names=col_names
)
df3 = pd.read_csv(
    '/home/pgcp-esd/Downloads/PYTHON/movie assignment/movies13.csv', 
    header=None, 
    names=col_names
)

rdf = pd.read_csv('/home/pgcp-esd/Downloads/PYTHON/movie assignment/rating11.csv') 

print(df1)
print(df2)
print(df3)
print(rdf)


mdf = pd.concat([df1, df2, df3], ignore_index=True)

print(mdf)
g = rdf.groupby("movieId")
print(g)
print(g[['rating']].mean())  #to calculate columnwise mean
m=g[['rating']].mean()
print(m)
fdf=pd.merge(mdf,m,on="movieId",how="left")

# Question 2

masala_mdf=mdf[mdf['genres'].str.contains('Action',case=False,na=False) &
     mdf['genres'].str.contains('Romance',case=False,na=False) &
     mdf['genres'].str.contains('Comedy',case=False,na=False) &
     mdf['genres'].str.contains('Thriller',case=False,na=False)]



print(masala_mdf.info())

# Question 3 : plot a pie chart to represent genre and frequency of movie count



genre_counts = mdf["genres"].str.split("|").explode().value_counts()
print(genre_counts)



plt.figure(figsize=(9, 9))
plt.pie(
    genre_counts,         
    labels=genre_counts.index,  # Genre names
    autopct='%1.1f%%',          # Automatically shows the percentage on each slice
    shadow=True,
    startangle=90,
    rotatelabels=True         
)
plt.show()








# Question 4. find average rating for each movie then merge 2 frames, display movieid,name,rating

print(mdf)
g = rdf.groupby("movieId")
print(g)
print(g[['rating']].mean())  #to calculate columnwise mean
m=g[['rating']].mean()
print(m)
fdf=pd.merge(mdf,m,on="movieId",how="inner")

print(fdf)



# Question 5. draw pie chart for each genre and average rating

genre_avg_rating = (
    fdf.assign(genres=fdf["genres"].str.split("|"))
    .explode("genres")
    .groupby("genres")["rating"].mean().round(2))

print(genre_avg_rating)

plt.figure(figsize=(9, 9))
plt.pie(
    genre_avg_rating,         
    labels=genre_avg_rating.index,  # Genre names
    autopct=lambda val: f"{val:.2f}",           # Automatically shows the percentage on each slice
    shadow=True,
    startangle=90,
    rotatelabels=True         
)

plt.title("Average Rating by Genre", fontsize=14)
plt.show()


##### 6. draw bar graph for each rating and number of movies
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser" 

rating_count = fdf["rating"].round().value_counts().reset_index()
rating_count.columns = ['rating', 'count'] # Name the columns

plt.figure(figsize=(8, 5))
plt.bar(rating_count['rating'], rating_count['count'], color='skyblue', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.title('Rating v/s Number of Movies (Matplotlib)')
plt.show()


fig = px.bar(
    rating_count,
    x='rating',
    y='count',
    title="Rating v/s Number of movies (Plotly)"
)
fig.show()




fdf["rating"]=fdf["rating"].round()

rating_count_demo = pd.DataFrame(fdf.groupby('rating').values_count)
print(rating_count_demo)