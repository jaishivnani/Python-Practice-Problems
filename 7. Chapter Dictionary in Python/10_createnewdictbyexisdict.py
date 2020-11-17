'''dictionary exercise 5: Create a new dictionary by extracting the following keys
from a given dictionary'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys=['name','salary']
res = {key:sampleDict[key] for key in keys}

print(res)


# dict1 = {i:f"Item {i}" for i  in range(5)}

# res = {}.fromkeys(employees,defaults)

