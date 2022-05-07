binary_number=[1,0,0,1,1,0,1,1]
i=0
c=0
sum=0
while i<len(binary_number):
    sum=(binary_number[-i]*2**c+sum)
    c=c+1
    i=i+1
print(sum)    