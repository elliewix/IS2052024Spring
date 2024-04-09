terms = ["cat", "boat", "london"]

fname = 'wouldbeathingifitwerehere.txt'

# make dict with file name an num terms

data = {'file_name': fname,
        'num_terms': len(terms)}

# now we can loop to prepopulate the rest

for term in terms:
    # data[term] = {} # we can add more in
    data[term] = {'count': 0, 'lines': []}

print(data)
# don't copypaste this, it's just a toy, you use your existing hw4 loop
for term in terms:
    # you normally would loop over lines here, but we aren't
    # for this example
    for c in term: # don't do this, we are looping over chars
        data[term]['count'] += 1
        data[term]['lines'].append(c)

print(data)