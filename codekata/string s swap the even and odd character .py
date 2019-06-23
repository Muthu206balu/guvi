get=input()
for k in range(len(get)):
  if (k%2==0):
    print(get[k+1],end='')
  else:
    print(get[k-1],end='')
