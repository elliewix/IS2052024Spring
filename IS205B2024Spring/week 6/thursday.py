# NO DONT, don't use with
# with open('book.txt', 'rt', encoding='utf-8') as infile:
#     text = infile.read()

infile = open('book.txt', 'rt', encoding='utf-8')
#
# for line in infile:
#     print("first loop", line)
# # nothing happens here bacuse cursor is at the end
# for line2 in infile:
#     print("second loop", line2)
# infile.close()

## strings and lists

a_string = "apps are a thing that exist"
a_list = ['apple', 'banana', 'pear']

# DON'T DO THIS
# vomit_list = [1, "apple", True, str]


a_string = "apps are a thing that exist"
a_list = ['apple', 'banana', 'pear']
# indexing, index position goes in [ ]
print(a_string[0])
print(a_string[7])
print(a_list[1])
# slicing, to get a group of things out
# start:stop (start inclusive) (stop exclusive)
print(a_string[5:8])

##

a_string = "apps are a thing that exist"
a_list = ['apple', 'banana', 'pear']

print("are" in a_string) # True
print("app" in a_string)  # True
print("app" in a_list) # False
print("apple" in a_list) # True

#range function, start, stop
print(list(range(10))) # presumes 0
print(list(range(5,10)))
