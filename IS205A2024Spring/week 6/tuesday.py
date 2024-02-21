# some_text = "here's some stuff etc"

filename = "book.txt"

infile = open(filename, 'rt', encoding="utf-8")
text = infile.read()
infile.close()

print(text)

# print(text.upper())
print(text.split()) # split in default mode will give you words
print(text.split("\n"))
# what is this newline???
# print(len("\nstuff"))

# looping over the lines of a file
# we've already done .read(), making text

lines = text.split("\n") # makes a list of lines

for l in lines:
    print(len(l), len(l.split())) #each line, one at a time
    # number of characters, and the number of words
