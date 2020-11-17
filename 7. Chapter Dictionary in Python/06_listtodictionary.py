'''keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#Using dictionary comprehension
res = {keys[i]: values[i] for i in range(len(keys))}

#Using Zip function
res = dict(zip(keys,values))
print(res)