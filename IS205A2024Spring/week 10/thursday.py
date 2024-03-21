letters = ['a', 'b', 'c', 'd', 'cats']

# for lett in letters: # outer loop making file
#     for i in range(1,6): # inner loop making content
#         print(lett * i)

for lett in letters: # this one holds outfile pattern
    # print(lett + ".txt")# once this looks good
    filename = lett + ".txt"
    outfile = open(filename, 'wt', encoding='utf-8')
    # in the middle here we want the inner loop
    for i in range(1,6):
        # print(lett * i) # eyeball it
        outfile.write(lett * i + "\n")
    outfile.close() # remember this is outside and at the end