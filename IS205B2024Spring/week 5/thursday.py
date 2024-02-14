numcats = 0

numcats = numcats + 0
numcats = numcats + 1
numcats = numcats + 0
numcats = numcats + 0
numcats = numcats + 3
numcats = numcats + 1
numcats = numcats + 1
numcats = numcats + 4

# print(numcats)

# let's try a for loop here
cat_data = [0, 1, 0, 0, 3, 1, 1, 4]

total_cats = 0
for cat_num in cat_data:
    # print("I'm in the loop", cat_num)
    total_cats = total_cats + cat_num
    # total_cats += cat_num # the same, just shorthand

# print("total", total_cats)

##

for character in "cat":
    print(character)

for unicorn in "cat":
    print(unicorn)

##

sentence = "some       people   have cats"

# words = sentence.split(" ") #NEVER EVER
words = sentence.split()
print(words)
print(sentence)
for w in words:
    print("line 42", w)