z1,z2=input().split()
count=0
for k in range(0,len(z2)):
  if(z2[k]!=z1[k]):
    count=count+1
if(count==1):
  print('yes')
else:
  print('no')
