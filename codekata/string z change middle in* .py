z=list(input())
if len(z)%2==0:
  z[int(len(z)/2)]='*'
  z[int(len(z)/2)-1]='*'
else:
  z[int(len(z)/2)]='*'
for k in range(0,len(z)):
  print(z[k],end='')
