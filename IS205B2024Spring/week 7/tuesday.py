text = "here is some text and such"
remove_these = "ext"

for letter in remove_these:
    text = text.replace(letter, "")
print(text)

## counter pattern, integer accumulator

count = 0 # base
# count how many characters are in it
for char in text:
    count = count + 1
    # shorthand is count += 1

print(count)
## string accumulator

new_text = "" # base

for char in text:
    # new_text = new_text + char
    new_text = char + new_text # flipped around
    print(new_text) # inside the loop, watch it grow
print(new_text) # see just the final version

# list accumulator

my_list = []

for char in text:
    # don't do all 3
    # unless you enjoy bad life choices
    my_list.append(char) # no assignment!
    # my_list.append(1) # collect 1s instead
    # my_list.append([]) # collect empty list
    # my_list = my_list.append(char) #NOOOOO
    # print(my_list) # see it grow

####

vowels = "aeiou"
not_vowels = []

for char in text:
    # messy if statement but you can clean it up later
    # an honest first try at something like this
    if char in vowels:
        continue
    elif char.isalnum():
        not_vowels.append(char)
    else:
        continue
        # not_vowels.append(char)

print(not_vowels)



