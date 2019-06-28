z1=[]
z2=int(input())
m=input().split()
for k in m:
  z1.append(k)
z1.sort()
z1.sort(key=len)
for k in z1:
  print (k,end=' ')
