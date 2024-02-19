# input: a string
# process: replace any x with _
# output: the new string
# let's call this remove_x

# two big things: plumbing and process

# func defs should be right at the top

# let's see plumbing first
# in this step you ignore process

def remove_x(orig_str):
    # do the stuff where I remove x and replace with _
    # result = "something" # hard coding it for now
    # result = orig_str # here's where you mess with it
    # result = orig_str.upper() + "!!!!" # so we can see we can do stuff
    result = orig_str.replace("x", "_")
    return result

def add_one(orig_str):

    result = orig_str + "11!"
    return result

# print(remove_x("here's a thing of text bbebxxxuu"))
clean_text = remove_x("here's a thing of text bbebxxxuu")
# print(clean_text)
final_text = add_one(clean_text)
print(clean_text)
print(final_text)

### how to "remove" with replace()

example = "here's some stuff (kind of)!"

# print(example.replace("(", "")) # okay kinda
# print(example.replace(")", ""))
# we need to save the intermediate results
example = example.replace("(", "")
example = example.replace(")", "")
# print(example)
# let's use a loop to avoid repeating

import string
example = "here's some stuff (kind of)!"
print(string.punctuation)

for punc in string.punctuation:
    print("results so far:", example)
    example = example.replace(punc, "")

print(example)