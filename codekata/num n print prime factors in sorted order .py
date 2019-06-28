z1=int(input())
for k in range(2,z1+1):
  if(z1%k==0):
      a=0
      for m in range(2,k+1):
          if(k%m==0) and (m!=k):
              a=1
              break
      if(a==0):
          print(k,end=' ')
