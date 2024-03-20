# sometext = "here's a string of some text"
filename = "book.txt"
# tells python it exists
infile = open(filename, 'rt', encoding='utf-8')
# now we want to read the content
text = infile.read()
infile.close()
print(text)
# totally done with infile

print(text.split()) # give you all the words
print(text.split("\n")) #split on newlines, getting all the lines
print(len("\n"))

# loop over all the lines
# presuming that you've done text = infile.read()

lines = text.split("\n")

# for l in lines:
#     print(len(l), len(l.split()), l)
for l in lines:
