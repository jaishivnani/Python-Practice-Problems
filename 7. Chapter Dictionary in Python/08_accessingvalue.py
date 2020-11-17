'''Accessing value'''

sampleDict = {"class":{"student":{"name":"Mike", "marks":{ "physics":70,"history":80}} }}

res =sampleDict['class']['student']['marks']['history']
print(res)