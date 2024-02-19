# let's write a function that takes a string, replaces any x with
# an underscore character, and returns that new string

# input: a string (orig_str)
# process: replace x with _
# output: the new string
# name: remove_x

# we're going to start with plumbing
# when we do plumbing, we ignore the process
def remove_x(orig_str):
    # result = "something" # just something random
    # result = orig_str # now we can see the input
    # result = orig_str.upper() # now let's mess with it
    # now let's do the real thing
    result = orig_str.replace("x", "_")
    return result

# let's call the function
# print(remove_x("this is some text"))
source = "this is some text"
# print(remove_x(source))
# print(source)

###

text = "here's something! with (punctuation)--"

# how do we "remove" with replace???

# print(text.replace("!", ""))
# print(text.replace("(", ""))
# print(text.replace(")", ""))
# print(text.replace("-", ""))

text = "here's something! with (punctuation)--"

# too much work!
# text = text.replace("-", "")
# text = text.replace("!", "")
# text = text.replace("(", "")
# text = text.replace(")", "")
# print(text)

# let's use a loop
import string

print(string.punctuation)
text = "here's something! with (punctuation)--"

for punc in string.punctuation:
    text = text.replace(punc, "")
    # print(text, punc)
print("final text", text)
### in keyword

print("hell" in "hello")
print("cat" in "dog")
print("the" in "them")

if "the" in "them":
    print("yes")

text = "here's something! with (punctuation)--"

if "her" in text:
    print("found")
else:
    print("not found")