f = open('motorcycleboots.jpg','rb')

f1 = open('myimg.jpg','wb')


for i in f:
    f1.write(i)