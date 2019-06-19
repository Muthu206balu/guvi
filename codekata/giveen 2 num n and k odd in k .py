z1,z2=map(int,input().split())
m=[int(k) for k in input().split()]
n=[]
for l in m:
  if(l%2!=0):
    n.append(l)
print(n[z2-1])
