'''default value
fromkeys() Parameters
fromkeys() method takes two parameters:
sequence - sequence of elements which is to be used as keys for the new dictionary
value (Optional) - value which is set to each each element of the dictionary
'''


employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

# res = {}.fromkeys(employees,defaults)
res = dict.fromkeys(employees,defaults)
print(res)