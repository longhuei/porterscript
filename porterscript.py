import sys
import string
from porter2stemmer import Porter2Stemmer

stemmer = Porter2Stemmer()
table = str.maketrans({key: None for key in string.punctuation})

for line in sys.stdin:
    words = line.rstrip().split()
    for w in words:
        w = w.translate(table)  # removes punctuation
        print(stemmer.stem(w) + ' ', end='')

    print("")
