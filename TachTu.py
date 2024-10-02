a = input()
arr = list(i for i in a) 
j = 0 
for i in range( j , len(arr) , 3) :
    if i == j+3 :
        arr.append(',')
    j += 3 ;
for i in arr :
    print(i,end='')     
       
