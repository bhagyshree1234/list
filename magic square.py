magic_square=[[8,3,4],[5,1,9],[6,7,2]]
i=0
row_sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        row_sum=row_sum+magic_square[i][j]
        j=j+1
    i=i+1
    print(row_sum)
    print()
i=0
colum_sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        colum_sum=colum_sum+magic_square[i][j]
        j=j+1
    i=i+1
    print(colum_sum)
    print()
i=0
left_diagonal=0
while i<len(magic_square):
    left_daigonal=left_daigonal+magic_square[i][j]
    i=i+1
print(left_diagonal)
i=0
j=2
right_diagonal=0
while i<len(magic_square):
    right_daigonal=right_daigonal+magic_square[i][j]
    i=i+1
    j=j-1
print(right_daigonal)  
print()
print(row_sum,colum_sum,left_daigonal,right_daigonal)
if row_sum==colum_sum and left_daigonal==right_daigonal:
    print("it is a magic_square",row_sum,colum_sum,left_daigonal,right_daigonal)
else:
    print("it is not magic_square",row_sum,colum_sum,left_daigonal,right_diagonal)     


    
