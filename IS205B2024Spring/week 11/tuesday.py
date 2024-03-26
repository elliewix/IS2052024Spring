text = "a sentence of stuff"
# you could at it like this, but no
a = 0
space = 0
s = 0

##

text = "a sentence of stuff"

# make a list of all the unique chars
# "have you seen this or not pattern"
letters = []
for char in text:
    # print(char)
    if char in letters:
        print("skipping", char)
    else: # okay so if it's not in there
        letters.append(char)
print(letters)

##

# dict accumulator

# say you've got some text or whatever
print(text)
# let's count up the characters inside
# and put that into a dict
counted = {} # dict() is an alt
for char in text:
    if char in counted: # check membership within keys
        print("here's where increment")
        # counted = counted + 1
        counted[char] = counted[char] + 1
    else: # haven't seen it yet
        print("here's where we create it")
        counted[char] = 1
print(counted)

## prepopulating a dict

data = "idididuduididudiduidudiduduidud"

terms = ['i', 'd', 'u']
counted_terms = {}
# step 1: populate
for t in terms:
    # add t as a key set with a value 0 into counted_terms
    counted_terms[t] = 0
print(counted_terms)

for char in data:
    # print(char)
    counted_terms[char] = counted_terms[char] + 1
print(counted_terms)

# dict reference
## create an empty dict
d = {} # dict() is the same
# add key/value pair
key = "cat"
value = 4
d[key] = value
d["dog"] = 3
# change a value for an existing key
d["dog"] = 10
# increment a value for an existing key
d["dog"] = d["dog"] + 1
d[key] = d[key] + 1
# to see a value
print(d[key])


