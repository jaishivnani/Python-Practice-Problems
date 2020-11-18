'''
dictionary exercise 8: Rename key city to location in the following dictionary
'''

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "location": "New york"
}

sampleDict["city"] = sampleDict["location"]
del sampleDict['location']
print(sampleDict)
