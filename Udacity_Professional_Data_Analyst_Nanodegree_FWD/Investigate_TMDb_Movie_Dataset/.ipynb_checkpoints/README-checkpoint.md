# Investigating The TMDb movie data set from Kaggle

![](https://miro.medium.com/max/705/1*f-bF79_zFHGXEhJvx2WPLg.jpeg)

# Table of Content
+ [Introduction](#Introduction)
+ [Prerequisites](#Prerequisites)
+ [Findings](#Findings)
+ [Conclusions](#Conclusions)

# Introduction

In this project, I analyzed the TMDb movie dataset from Kaggle and communicated the findings using visualizations. I made use of the Python libraries NumPy, pandas, and Matplotlib in this analysis. I went through a full EDA process while analyzing this dataset including the process of wrangling, cleaning, and analyzing its data to answer these questions:

### Questions:
1. Which Movie has returned the highest and lowest revenues?
2. What kinds of features are associated with high revenue?
3. What are the profitable movie genres?
4. What was the year that has the most movies with the highest profit?

# Prerequisites
The used dataset can be found [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/discussion)
## Languages and libraries
- Python 3.9
- Pandas
- NumPy
- Matplotlib 

# Findings
- ### Which Movie has returned the highest and lowest revenues?
![](imgs/hiest_rev_movie_returned.png)

> The movie Avatar has returned the highest revenue followed by Star Wars: The Force Awakens, Titanic, The Avengers and Jurassic World.

![](imgs/lowest_rev_returned.png)

> The movie Shattered Glass has returned the lowest revenue followed by Mallrats, Dr.Horrible's Sing-Along Blog, Kid's Story and Bordello of Blood.

---

- ### What kinds of features are associated with high revenue?
![](imgs\headmap_corr.png)

> The heatmap shows that the features that are correlated with a movie having a high revenue are popularity, budget and profit.

---

- ### What are the profitable movie genres?
![](imgs\top_20_genres.png)

> Movie genres Adventure, Action, Science Fiction and Family seems to be the most popular in the top 20 movies.

---

- ### What was the year that has the most movies with the highest profit?
![](imgs\year_most_profit.png)

> Year 2015 is the year that has the movies with the highest profits.

---

# Conclusions

1. Avater is the highest revenue returend movie.
2. Mallrats is the lowest revenue returend movie.
3. Popularity, budget and profit are the features that effect the movie's revenue the most.
4. Release year 2015 is the year that has the most profitable movies released.

---

 ### From analyzing the top 20 profitable movies, we conculted that in order for a movie to be profitable:

1. It should have an average runtime of 136.65 Minutes.
2. An average budget of 16,005,0000$
3. An average popularity score of 7.03671825.
4. Should be in these movie genres Adventure, action, science-fiction, and family.


## Authors
- [@Hossam El-Shabory](https://github.com/hossam-elshabory)
