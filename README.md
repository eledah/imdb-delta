# imdb-delta
![](https://img.shields.io/badge/BASED%20DEPARTMENT%20CHECK-PASSED-green) ![](https://img.shields.io/badge/category-datamining-blue)

Looking for a guaranteed Woman Moment™ in a movie? Or perhaps you are looking forward to some real violence against women and/or minorities in a testostrone-fueled Filmbro™ epic? Either way, this is the perfect movie directory for you. The cutting edge technology allows the user to delve deep into the collective minds of the gifted IMDb users in order to see the most (and least) divisive movies based on their genders.


## Table of contents
* [What?](#What?)
* [Why?](#Why?)
* [How?](#How?)
* [Who?](#Who?)

## What?
Alright. Imagine that we go over to [the highest rated feature films on IMDb](https://www.imdb.com/search/title/?at=0&num_votes=25000,&sort=user_rating,desc&title_type=feature&count=250"), filter out the ones with less than enough ratings (anything above 25K or even 100K) and then, start gathering the data for the first 2000 movies.
Little does everyone know that IMDb has a [detailed rating page](https://www.imdb.com/title/tt0111161/ratings) dedicated to each movie. Here is where we find the scoring distribution and how men and women in different age groups have rated the movie. By acquiring the data from this page we create a weighted average for each gender and re-rank the movies based on each gender.
The Final step in the process is to calculate the difference between the rankings given by men and women and then sort this "Delta" value in ascending order. the results will show an approximate spectrum of different levels of enjoyment between men and women. Here are a few well-known movies for an example:

Movie Name | Male Rank | Female Rank | Delta
------------ | ------------- | ------------- | -------------
[Tangled](https://www.imdb.com/title/tt0398286) | 960 | 297 | 663
[Dogville](https://www.imdb.com/title/tt0276919) | 444 | 234 | 210
[Joker](https://www.imdb.com/title/tt7286456) | 73 | 50 | 23
[Fantastic Mr. Fox](https://www.imdb.com/title/tt0432283) | 608 | 607 | 1
[The Good, the Bad and the Ugly](https://www.imdb.com/title/tt0060196) | 10 | 76 | -66
[Memories of Murder](https://www.imdb.com/title/tt0353969) | 197 | 465 | -268
[No Country for Old Men](https://www.imdb.com/title/tt0477348) | 208 | 799 | -591

I also have uploaded the spreadsheet to [Google Drive](https://drive.google.com/file/d/1JRYj-Lwhcla9YVVCbYAD5gClsOsbuVex/view?usp=sharing) for better viewing experience. I have also applied two different filters (Ratings > 100K & Score > 7.5) in order to create a more familiar movie list. I will also try to create additional ways of conevying the spredsheet information but until then you have to wait.

Note that a high Delta value doesn't necessarily mean that a certain gender liked or hated a movie. My personal thoughts are that they had a higher level of enjoyment or empathy towards the movie and its main themes. Also, just know that this way of calculating the preferences is not completely accurate and what you is but an approximation.


## Why 
Because I wanted to know this stuff(???) also Letterboxd didn't respond to my emails regarding their API so had to use the next best thing 😩
Meaning that this is fun project of mine so let's not take it seriously

## Who?
[@eledah](https://www.t.me/eledah)
