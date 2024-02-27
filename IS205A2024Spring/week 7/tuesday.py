# reminder: iterative update

text = "here's some text and such"
remove_these = "ext" # remove the characters
# expected result: hr's som  and such
for letter in remove_these:
    text = text.replace(letter, "")
# print(text)

# quick counter reminder

count = 0 #base
for char in text:
    count = count + 1
    # count += 1 #shorthand

# print(count)
# print(len(text))

# string accumultor pattern
# "smallest" version, no fussing
new_text = "" # base
for char in text:
    #new_text = new_text + char # a copy
    new_text = char + new_text # hmmm
    print(new_text)
# sort of making a copy of text
# print(text)
# print(new_text)

####

my_list = [] # base, an empty list

for char in text:
    # append method
    # you could do multiple if you wanted
    # but don't mix data types
    my_list.append(char)
    # my_list.append(1) # collect 1s if you want
    # my_list.append([]) # collect empty lists
    # print(my_list) # watch it grow
# print(my_list) # see the final version

####

# let's play with list accum patterns again

vowels = "aeiou"
text = "here's some new text stuff and such"
# collect a list of not_vowels
not_vowels = []
for char in text:
    if char in vowels:
        continue # forcing it to move forward
    elif char.isalnum():
        not_vowels.append(char) # yes!
        # not_vowels = not_vowels.append(char) # problems
    else:
        print("skipping", char)

print(not_vowels)
