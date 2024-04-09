import json

infile = open('example.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

# print(data)
print(data.keys())
print(data['num_terms'])
print(data['cat'])
print(data['cat']['count'] + 1)

print(data['dome']['lines'])
data['dome']['lines'].append("hi I'm new")
print(data['dome']['lines'])

# counter = counter + 1
data['cat']['count'] = data['cat']['count'] + 1

# alternatively
# counter += 1
data['cat']['count'] += 1
print(data)

# write it out

outfile = open('newexample.json', 'wt', encoding='utf-8')
json.dump(data, outfile, indent = 4)
outfile.close()