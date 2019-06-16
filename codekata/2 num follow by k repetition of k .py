x,y=map(int,input().split())
z=[int(k) for k in input().split()]
a=0
for m in z:
  if(m==y):
    a=a+1
print(a)

