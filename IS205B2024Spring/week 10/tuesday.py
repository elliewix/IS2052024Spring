one_list = [1,2,3] #1D list

a_list_of_lists = [ [1,2,3], [4,5,6] ] # a 2D list
# # starting point, what's in here?
# for each in a_list_of_lists:
#     print(each)

for inner in a_list_of_lists: #outer loop
    print("inner list is:", inner)
    for number in inner: # inner loop
        print("from", inner, 'we get', number)

sentence = "here are some words"
words = sentence.split() # this is now a list
# calc the avg word length
# step 1 just dig in
# for w in words:
#     print(w)
#     for letter in w:
#         print(letter)

word_count = 0
char_count = 0
for w in words:
    # print #this is where our words at, one at time
    word_count = word_count + 1
    for letter in w:
        # print(letter)
        char_count = char_count + 1

print(word_count, char_count, char_count / word_count)

# let's collect a 2D list of characters
outer = []
for w in words: # outer loop
    inner = []
    for letter in w:
        # print(w, letter)
        inner.append(letter)
    # print(inner)
    outer.append(inner) # add the final version of inner
    print(outer) # see outer grow
print(outer) # see the final result