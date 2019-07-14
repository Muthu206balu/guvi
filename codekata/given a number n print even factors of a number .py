z=int(input())
for k in range(1,z+1):
  if((z%k==0) and (k%2==0)):
      print(k,end=' ')
