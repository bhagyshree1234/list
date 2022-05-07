i=1
list=[]
sum=0
while i<5:
    num=int(input("enter the number"))
    list.append(num)
    i=i+1
print(list)
j=0
while j<len(list):
    sum+=list[j]
    j=j+1
print(sum)

i=1
while i<=10:
    i=i+1
    print(i)  

binary_number=[1,0,0,1,1,0,1,1]
i=0
c=0
sum=0
while i<len(binary_number):
    sum=(binary_number[-i]*2**c+sum)
    c=c+1
    i=i+1
print(sum)    

list=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
k=4
list1=[]
i=0
while i<len(list):
    if i==k:
        list1.append(20)
        k=k+4
    list1.append(list[i])
    i=i+1
print(list1)      

list=[1,2,3]
for i in range(len(list)):
    for  j in range(len(list)):
        for k in range(len(list)):
            if i!=j and j!=k and k!=i:
                print(list[i],list[j],list[i])

a=["n","a","v","g","u","r","u","k","u","l"]
i=0
sum=""
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(sum)

