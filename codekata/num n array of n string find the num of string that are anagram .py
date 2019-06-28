z1=int(input())
z2=0
z3=[]
for k in range(z1):
  z3.append(input())
for k in range(z1):
  if(sorted(z3[k])==sorted('kabali')):
    z2=z2+1
print(z2)
