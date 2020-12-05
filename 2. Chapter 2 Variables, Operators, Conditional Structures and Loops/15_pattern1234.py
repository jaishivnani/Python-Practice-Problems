for i in range(1,5):
    for j in range(1,5):
        k = i + j - 1
        if k>4:
            print("",end="")
        else:
            print(k,end="")
    print()