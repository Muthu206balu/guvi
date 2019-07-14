z1=int(input())
a=0
for k in range(2,z1):
  if(z1%k==0):
    a=1
if(a==1):
  print("yes")
else:
  print("no")
