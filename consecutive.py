list=[4,5,5,5,3,8]
n=[]
for i in list:
    c=0
    for j in list:
        if i==j:
            c=c+1
    if c>2:
        if i not in n:
            n.append(i)
print(n)                  