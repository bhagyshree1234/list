list=[23,46,32,25,46,33,71,90]
i=0
a=[]
b=[]
while i<len(list):
    if list[i]%2==0:
        a.append(list[i])
    elif list[i]%2!=0:
        b.append(list[i])
    i=i+1
print(a,b)            