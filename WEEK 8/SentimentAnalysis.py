#!/usr/bin/python3
"""
This program does Sentimental Analysis from the given data
using -
    nltk   - to process human natural language
    vader  - to specify the intensity level of the sentiment
    pandas - to create dataframes from the Excel file
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Downloading a dictionary to test sentiment intensity
nltk.downloader.download('vader_lexicon')

# opening the Excel file
file = "/path/to/the/Excelfile"
xl   = pd.ExcelFile(file)

# parse the file and put it as a dataframe
dfs = xl.parse(xl.sheet_names[0])

# Remove blank cells in the file
dfs = list(dfs['Timeline'])

# Printing the data as a list
print(dfs)

# Initializing Sentiment analyser
sid = SentimentIntensityAnalyzer()

# Ignoring unnecessary data like time
str1 = "UTC+5:30"
for data in dfs:
    a = data.find(str1)
    
    if ( a == -1 ):        # find() returns -1 when not found
        ss = sid.polarity_scores(data)
        print(data)
        # iterating through each sentence
        for k in ss:
            print(k,":",ss[k])
            