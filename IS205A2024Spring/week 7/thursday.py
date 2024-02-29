text = " here   is a sentence.   \t\n "
print(text)

# split()
## in default mode, will break apart
print(text.split()) # () empty!
print(text.split(" ")) # :-(

# replace 2 arguments: old, new

print(text.replace(" ", ""))
print(text.replace(" ", "_"))
cleantext = text # this will a copy because a str
# don't do this with lists
replacethese = " \t"
for char in replacethese:
    cleantext = cleantext.replace(char, "_")

print(cleantext)

# strip: cleaning stuff off the sides

## strip() in default mode will take off
## any of the spacing characters

print(text.strip()) # () empty!
# a little hard to see
# print(text.strip().split())
print(text.strip())
print([text.strip()])
print([text])