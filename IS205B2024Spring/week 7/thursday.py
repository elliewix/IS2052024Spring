text = "   here    is a sentence.   \t\n"

# split
## default mode breaks into chunks on
## groups of spaces
## always returns a list

print(text.split()) # () empty!
# can give an arg
print(text.`split`("e"))

# replace takes 2 args: old, new
print(text.replace(" ", "_"))

## string.punctuation

import string
moretext = "here's more text!!!  $$$%@#$%"
for punc in string.punctuation:
    moretext = moretext.replace(punc, "") # "remove"

print(moretext)

# strip()
## strip() in the default mode

print(text)
print(text.strip())
print([text])
print([text.strip()])

# you can also give in an argument

print([text.strip(" ")])
print("(( * _hello! cat's are cool.  )(! ".strip())
print("(( * _hello! cat's are cool.  )(! ".strip("(!)* _"))
print("(( * _hello! cat's are cool.  )(! ".strip(string.punctuation + " "))

# outfile pattern
## 2 things you need to have in order before
## you write a file out or use outfile
## filename
fname = "results.catpoop.ihatezoom.itscold"
## content to go in the file
## let's use the text variable

# wt for write text
outfile = open(fname, 'wt', encoding='utf-8')
outfile.write(text) # give it the content in ()
outfile.close() # do this 2nd and work in the middle

lines = ["sentence 1", "another one", "yet another", "etc"]

outfile = open("list_results.txt", 'wt', encoding='utf-8')

for l in lines:
    outfile.write(l + "\n")

outfile.close()
