k = int(input())
matrix = [[]] *  k 
for i in range(k) :
    matrix[i] = [int(i) for  i in input().split()] 


up , down = 0 , 0 
for  i in range(k) :
    for  j in range(k):
        if i < j :
            down += matrix[i][j]
        elif i > j :
            up += matrix[i][j] 

k = int(input())
sub = abs(up - down)
print('YES' if sub <= k else 'NO')
print(sub)