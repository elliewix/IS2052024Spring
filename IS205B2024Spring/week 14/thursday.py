import csv
from collections import Counter

text_data = """here are some words
more words
even more words
cats exist without words
words are cool"""

lines = text_data.split("\n")
print(lines)
print(len(lines))

all_words = []
for l in lines:
    words = l.split()
    for w in words:
        all_words.append(w)

print(all_words)
num_words = len(all_words)
print(num_words)

print(Counter(all_words))
counted_words = dict(Counter(all_words))
## to write a csv file you need:
# a 1D list that will become the headers, the content should be strings
# a 2D list of lists that are the rows
all_rows = []
for word, count in counted_words.items():
    # print(word, count)
    row = [word, count, round(count / num_words,2)]
    # print(row)
    all_rows.append(row)
print(all_rows)

headers = ["word", "word count", "prop, in decimal"]

# only now do I want to do outfile things

outfile = open('word_counts.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)

csvout.writerow(headers) # takes the 1d lst for headers
csvout.writerows(all_rows) # takes the 2 d list for all the data
