list=[1,2,3]
for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if i!=j and j!=k and j!=1:
                print(list[i],list[j],list[k])
                