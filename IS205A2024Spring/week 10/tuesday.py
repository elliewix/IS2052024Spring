example_list = [1, 2, 3]
for element in example_list:
    print(element)

a_list_of_lists = [ [1,2,3], [4,5,6] ]
# for element in a_list_of_lists:
#     print(element)
# use better names
for inner_list in a_list_of_lists:
    print("outer loop", inner_list)
    for number in inner_list:
        print("inner loop", number)

sentence = "here are some words"
words = sentence.split()
# for w in words:
#     print('w',w)
#     for letter in w:
#         print('letter from', w,  letter)

# calculate the average word length in sentence

char_counter = 0
word_counter = 0
for w in words:
    # we're looking at the word, and we count it up
    word_counter = word_counter + 1
    # now count up the letters
    for letter in w: # remeber w is the new sequence
        char_counter = char_counter + 1

print(word_counter, char_counter, char_counter/word_counter)

# let's make a letter matrix thing

outer = []
for w in words:
    # mmmm need to get a list of letters in here?
    inner = [] # will be erased each w loop through
    for letter in w:
        # collect the letters
        inner.append(letter)
    # print(inner)
    outer.append(inner)
print(outer)
