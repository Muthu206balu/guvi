z1,z22=input().split()
z1,z2=int(z1),int(z2)
count=0
for k in range(z1,z2+1):
  a=k//2
  b=0
  for m in range(2,a+1):
    if(k%m==0):
      b=1
  if(b==0):
    count+=1
print(count)
