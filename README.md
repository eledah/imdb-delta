# imdb-delta

[Live Demo](https://eledah.github.io/imdb-delta)

This project is no longer recieving updates due to IMDB's decision to remove the demographic ratings for every movie.

## The Goal

The goal of is project is to determine the most boyish and girlish movies there are and find the common ground inbetween. The data comes from IMDB's ratings. First we rank all the top 2000 movies in IMDB by gender and then, we calculate the difference between the rankings given by men and women which gives of a **Delta** value. And for the last part, we sort by Delta value in ascending order. the results will show an approximate spectrum of different levels of enjoyment between men and women. Here are a few well-known movies as an example:

Movie Name | Male Rank | Female Rank | Delta
------------ | ------------- | ------------- | -------------
[Tangled](https://www.imdb.com/title/tt0398286) | 960 | 297 | 663
[Dogville](https://www.imdb.com/title/tt0276919) | 444 | 234 | 210
[Joker](https://www.imdb.com/title/tt7286456) | 73 | 50 | 23
[Fantastic Mr. Fox](https://www.imdb.com/title/tt0432283) | 608 | 607 | 1
[The Good, the Bad and the Ugly](https://www.imdb.com/title/tt0060196) | 10 | 76 | -66
[Memories of Murder](https://www.imdb.com/title/tt0353969) | 197 | 465 | -268
[No Country for Old Men](https://www.imdb.com/title/tt0477348) | 208 | 799 | -591

Note that a high Delta value doesn't necessarily mean that a certain gender liked or hated a movie. My personal thoughts are that they had a higher level of enjoyment or empathy towards the movie and its main themes. Also, just know that this way of calculating the preferences is not completely accurate and what you is but an approximation.

## See the data for yourself

I also have uploaded the spreadsheet to [Google Drive](https://drive.google.com/file/d/1JRYj-Lwhcla9YVVCbYAD5gClsOsbuVex/view?usp=sharing) for better viewing experience. I have also applied two different filters (Ratings > 100K & Score > 7.5) in order to create a more familiar movie list.



