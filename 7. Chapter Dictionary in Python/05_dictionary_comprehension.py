# dict1 = {0:"item1",1:"item1"}
# we will do above thing by using comprehensions
# dict1 = {i:f"Item{i}" for i  in range(1,10000) if i%100==0}

dict1 = {i:f"Item {i}" for i  in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)
