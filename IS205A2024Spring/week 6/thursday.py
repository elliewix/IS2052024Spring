
#DON'T USE
# with open('book.txt', 'rt',encoding='utf-8') as infile:
#     text = infile.read()

# infile = open('book.txt', 'rt', encoding='utf-8')
# for line in infile:
#     print("doing noting")
#
# for line in infile: # we'll see nothing come from here
#     print("second round", line)
#


### strings vs lists

a_string = "apps are things that exist"
# your lists should have a single data type
a_list = ["apple", "banana", "pear"]

# in keyword
print("app" in a_string) # True, because substrings
print("app" in a_list) # False, because no exact match
print("apple" in a_list) # True
# don't do this!
# vomit_list = [1, "banana", True, str]

a_string = "apps are things that exist"
# your lists should have a single data type
a_list = ["apple", "banana", "pear"]
# indexing
# for when you want one "thing"
print(a_string[0]) # index pos in [] on the end
print(a_list[0])
# slicing: when you want more or a group of things
# start:stop  start (inclusive) stop (exclusive)
print(a_string[5:8])
print(a_list[1:3])

# range function

print(list(range(10))) # one argument, presumes 0 at the start
print(list(range(5, 10))) # start, stop