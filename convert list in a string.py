list=["red","maroon","yellow","olive"]
i=0
a=[]
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        b.append(list[i][j])
        j=j+1
        a.append(b)
        print()
        i=i+1
print(a)        

# account=[[1,2,3],[33,2,1]]
# i=0
# sum=0
# while i<len(account):
#     j=0
#     while j<len(account[i]):
#         sum+=account[i][j]
#         j=j+1
#     i=i+1
#     s=sum[i]
#     while i<sum:
#         t=sum[i]
#         if s<t:
#             s=t
#         i=i+1
# print(s)            