text = "a sentence of stuff"
# how we might approach it, but no
# a = 0
# space = 0
# s = 0
# e = 0

text = "a sentence of stuff"
# what are all the unique characters?
# not counting, just collecing
uniques = []
for char in text:
    # print(char)
    if char in uniques:
        print("already have", char)
    else: # so when we don't have it yet
        uniques.append(char)
print(uniques)

##

# dict accumulator

## start with empty dict
counted_chars = {}

for char in text:
    print(char)
    # in works with dicts, checks key membership
    if char in counted_chars: # if it's already in
        print('increment up existing key')
        # think about counted_chars[char] as your "counter"
        counted_chars[char] = counted_chars[char] + 1
    else:
        print('create the key in the dictionary')
        # use an assignment-like sytax
        # where char will have the key
        counted_chars[char] = 1
    print(counted_chars)


print(counted_chars)

###

## make an empty dictionary
d = {} # dict()
## make a dict with a key/value pair in it
x = {"fish": 0}
## create a new key value pair
key = "cat"
value = 5
d[key] = value # sometimes you have variables
d["dog"] = 10 # sometimes it is direct
print(d)
## update an existing value
d["cat"] = 7 # where you just change it
d["dog"] = d["dog"] + 1
d[key] = d[key] + 1
## to see a value
print(d[key])

# prepopulating a dict

## so you have some content, let's text again

random_letters = "udidudidudidudidudiiududidudidud"
known_values = ['u', 'd', 'i']
counts = {}
## we want a dict set up with these key/values before we search
## in this case, we'll set the "counts" to 0
## use char as key, set initial val to 0, put them in counts
for char in known_values:
    counts[char] = 0
print(counts)