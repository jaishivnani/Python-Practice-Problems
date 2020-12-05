f = open('sample.txt','r')

f1 = open('another.txt','w')

for data in f:
    f1.write(data)
    