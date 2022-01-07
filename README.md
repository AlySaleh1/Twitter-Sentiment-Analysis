# Discussion Analysis regarding COVID-19 Vaccines
This is a data science report that analyzes tweets to identify people's sentiment towards Covid-19 vaccines and the main topics surrounding the pandemic. This report was made with two other people: Jessica Pizzuco and Nuri Ege Zararsiz.

### Purpose of this report:
This report aims to discover the salient topics discussed around the COVID-19 pandemic. It also seeks to identify the relative engagement with these topics and if these responses are negative or positive.

For example, When a tweet is talking about the pandemic, **how often do people mention COVID-19 restrictions? And if the tweet is discussing COIVD-19 restrictions, is it in support of restrictions or against restrictions?**

## My role in this project
My main two roles were **Data Collection and Data Formatting**. I also took part in refining the typology.
I used Twitter's API to collect Tweets with certain Covid-related keywords (Code can be found under src/collect_tweets.py). Each tweet returned a lot of metadata, so I had to extract only the relevant data need for the project and format it in a CSV format (code is in src/json_to_csv.py).
My other roles in the project:
- Data annotation
- Data analysis and discussion (Retweets and Favourite count)
- Writing data collection section
- Writing part of results and discussion
