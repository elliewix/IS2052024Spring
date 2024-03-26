letters = ['a', 'b', 'c', 'd', 'cats']

# for lett in letters:
#     # print(lett)
#     for i in range(5):
#         print(lett * i)

for lett in letters:
    # print(lett + ".txt")
    filename = lett + ".txt"
    outfile = open(filename, 'wt', encoding='utf-8')
    # work in the middle for content
    for i in range(5):
        # instead of printing, we write
        outfile.write(lett * i + "\n")

    outfile.close() # close at the same indent as creating