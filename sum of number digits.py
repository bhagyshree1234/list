list=[12,67,98,34]
i=0
while i<len(list):
    a=str(list[i])
    j=0
    sum=0
    while j<len(a):
        sum=sum+int(a[j])
        j=j+1
    i=i+1
    print(sum)    