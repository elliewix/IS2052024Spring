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
## strip with args
messytext = "_!_stuff! and things' are cool._() % __"
## just give one string
print(messytext.strip("_"))
# when you give it a str longer than 1
# it treats each character as a separate option
# to remove
print(messytext.strip("_!% ()")) # too much work here
import string
print(string.punctuation)
print(messytext.strip(string.punctuation))
# if I wanted the space character to be included
print(messytext.strip(string.punctuation + " "))
# you can edit if needed
edited_punc = string.punctuation.replace(".", "")
edited_punc = edited_punc + " "

print(messytext.strip(edited_punc))

# outfile pattern

## first get the file name

fname = "results.txt"

## then identify where the content is
## that you want inside the file
## in this case, let's save the results of cleanup
## so cleanuptext
cleaneduptext = messytext.strip(edited_punc)

## only when you have those 2 pieces should you proceed
# wt for write text mode!
outfile = open(fname, 'wt', encoding='utf-8')
outfile.write(cleaneduptext) # give it the content
outfile.close() # close is REQUIRED for writing

# let's see this inside a loop

print(cleaneduptext.split())

items = cleaneduptext.split() # hw: this would be your lines
# for each in items:
#     # write each item to a file
#     # one item per line
#     print(each)

# think about this as a file accumulator pattern

outfile = open('loop_results.txt', 'wt', encoding='utf-8')
for each in items:
    # note how open() etc. NOT inside the for loop
    # write each item to a file, one item per line
    # outfile.write(each) # missing newlines
    outfile.write(each + "\n")
outfile.close() # note this is outside of the for loop
