fname = "yourfilename.txt"

terms = ['cat', 'boat', 'london']

# first stage of prepop
data = {'file_name': fname,
        'num_terms': len(terms)}

# 2nd stage of prepop
for t in terms:
    # data[t] = {} # we can do more here
    data[t] = {'count': 0,
               'lines': []}

# a fake version of your existing loop

for t in terms:
    # you would actually want to loop over lines
    # but I don't have that
    # so I'm going to loop over characters
    for char in t:
        data[t]['count'] += 1
        data[t]['lines'].append(char)
print(data)