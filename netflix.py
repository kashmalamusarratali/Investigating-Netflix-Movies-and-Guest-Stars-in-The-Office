import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
years = [2011, 2012, 2013 ,2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90]
movie_dict ={ "years" : years , "durations" :durations}
print(movie_dict)
durations_df = pd.DataFrame(movie_dict)
print(durations_df)
plt.plot(durations_df['years'], durations_df['durations'])
plt.title( "Netflix Movie Durations 2011-2020")
plt.show()
netflix_df= pd.read_csv("C:/Users/Mughals/Desktop/netflix_data.csv")
print(netflix_df[0:5])
netflix_df_movies_only= netflix_df[netflix_df['type'] == 'Movie']
print(netflix_df_movies_only[0:5])
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_movies_col_subset[0:5])
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
print(short_movies[0:20])
colors=[]
for lab,row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

print(colors[0:10])
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8)) 
plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"], color= colors ) 
plt.xlabel("Release year")
plt.ylabel("Duration (min)")  
plt.show()






