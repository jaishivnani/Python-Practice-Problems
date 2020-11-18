'''Accessing value'''

sampleDict = {"class":{"student":{"name":"Mike", "marks":{ "physics":70,"history":80}} }}

res =sampleDict['class']['student']['marks']['history']
print(res)

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary'] = 8500

print(sampleDict)