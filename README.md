# Stemming

This repository contains the code for the rudimentary search engine described on our blog in this post. 

#### Note that this may not be how Google's search engine actually stems. The purpose of this code is just to show how search queries and search results can be stemmed so as to incorporate word inflections and derivations in a search.

- In this code, we first stem the search query.
- We then "perform a search" (we actually just read from a file in this case)
- Next, we stem the results. This is done because if we only stemmed the query and searched for that, some results could be missed because of some word stems not being exact substrings of their inflections. For example, if the query were "happiness", it is stemmed to "happi", and the result "happy" would then be missed out. We need to ensure that "happy" gets stemmed to "happi". 
- Finally, we count the number of occurrences of the search query in the results, both with and without stemming to compare their performance. 
