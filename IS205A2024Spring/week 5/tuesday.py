numcats = 0

numcats = numcats + 0
numcats = numcats + 1
numcats = numcats + 0
numcats = numcats + 0
numcats = numcats + 2
numcats = numcats + 3
numcats = numcats + 1
numcats += 2 # same thing

# okay that worked, but was long and repetitive
# let's do this in a for loop

# first, I need to have some data
cat_data = [0, 1, 0, 0, 2, 3, 1, 2]

numcats = 0
for cats in cat_data:
    # print(cats)
    numcats = numcats + cats

# print("total", numcats)

# let's do a string example

for unicorns in "cat":
    print(unicorns)

# let's do a sentence

sentence = "some people have cats"
words = sentence.split()
print(words)
for word in words:
    print(word)