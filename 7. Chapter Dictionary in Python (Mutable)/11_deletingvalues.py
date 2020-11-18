'''
dictionary exercise 6: Delete set of keys from Python Dictionary

'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

# sampleDict = {key:sampleDict[key] for key in sampleDict.keys()- keysToRemove}

for i in keysToRemove:
    del sampleDict[i]

print(sampleDict)
