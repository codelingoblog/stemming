from nltk.stem import *

# create a new Porter stemmer
stemmer = PorterStemmer()

# you could also use the Porter2 Stemmer
# stemmer = SnowballStemmer("english")

wordToStem = 'teleportation'
stemmedWord = stemmer.stem(wordToStem)
print(stemmedWord)
