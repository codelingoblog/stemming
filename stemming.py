import re
from nltk.stem import *
from collections import Counter

# use the Porter2 Stemmer
stemmer = SnowballStemmer("english")

# user makes the following query (but you can inflect this to evaluate/evaluating/evaluates/etc)
searchQuery = 'evaluation'

# first we stem the query
stemmedSearchQuery = stemmer.stem(searchQuery.lower())

# fetch search results using some algorithm (reading from a file in this case)
resultsFile = open('results.txt', 'r')
results = stemmer.stem(resultsFile.read().lower())

# stem each word
splitResults = results.split()
stemmedResults = [stemmer.stem(word) for word in splitResults]
stemmedResults = ' '.join(stemmedResults)

resultsWithoutStemming = re.findall(searchQuery, results)
resultsWithStemming = re.findall(stemmedSearchQuery, stemmedResults)

countWithoutStemming = Counter(resultsWithoutStemming)
countWithStemming = Counter(resultsWithStemming)

print("By NOT stemming the search query or results, we retrieve " + str(countWithoutStemming[searchQuery]) + " result(s).")
print("By stemming the search query and results, we retrieve " + str(countWithStemming[stemmedSearchQuery]) + " result(s).")
