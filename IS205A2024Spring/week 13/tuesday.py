import json

# read in a json file

infile = open('example.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

# print(data)
print(data.keys()) # remmeber that data is a dict, so keys() will work
print(data['num_terms'])
print(data["cat"]) # first get into the node
print(data["cat"]['count'])
print(data["dome"]['count'])
print(data["cat"]["lines"])