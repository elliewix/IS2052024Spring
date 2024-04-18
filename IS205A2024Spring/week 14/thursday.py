# reading/wring csv files
import csv
from collections import Counter

# in order to write a csv out you need:
# a 1D list of strings that will become the headers
# a 2D list of lists, where each list is a "row" of data

text_data = """some words
more words
still more words
cats are a thing
hello humans"""

lines = text_data.split("\n")
print(lines)
print(len(lines)) # should be 5

all_words = []
for line in lines:
    words = line.split()
    for w in words:
        all_words.append(w)

print(all_words)
print(Counter(all_words))
num_words = len(all_words)
counted_words = dict(Counter(all_words))
print(num_words,counted_words)

# making the 2D list of rows
all_rows = []
for word, count in counted_words.items():
    # print(word, count)
    row = [word, count, round(count / num_words, 2)] # still need prop
    all_rows.append(row)
print(all_rows)
# make some headers, our 1D list
headers = ["word", "word count", "prop, in decimal"]

# boilerplate for writing a csv

outfile = open('word_counts.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)

# now we can write content to csvout
csvout.writerow(headers) # takes the 1D list
csvout.writerows(all_rows) # give the plural one the 2D list
