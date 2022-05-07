list=[3,45,23,67,3,2,2,]
i=0
a=list[0]
while i<len(list):
    if list[i]>a:
        a=list[i]
    i=i+1
print(a)
i=0
b=list[0]
while i<len(list):
    if list[i]>b and list[i]!=a:
        b=list[i]
    i=i+1
print(b)
i=0
c=list[0]
while i<len(list):
    if list[i]>c and list[i]!=b and list[i]!=a:
        c=list[i]
    i=i+1
print(c)