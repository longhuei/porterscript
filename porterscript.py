import sys
from porter2stemmer import Porter2Stemmer

stemmer = Porter2Stemmer()

for line in sys.stdin:
    stemmed = stemmer.stem(line.rstrip())
    print(stemmed)
