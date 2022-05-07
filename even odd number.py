a=[1,2,3,4,5,6,7,-9,-4,-2,-3,-1,-6,-7]
i=0
while i<len(a):
    if a[i]>0:
        print(a[i],"positive")
    else:
        print(a[i],"negative")
    i=i+1
