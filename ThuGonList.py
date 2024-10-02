n = int(input())
list = [int(i) for i in input().split()]
i = 1
while i < len(list):
      if (list[i-1]+list[i]) % 2 == 0:
          list.pop(i)
          list.pop(i-1)
          for j in list :
               print(j , end = ' ')
          print()     
          print(len(list))     
      if i > 1:
            i -= 1
        
      else:
        i += 1        
