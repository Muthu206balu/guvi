z1=list(map(int,input().split()))
z2=list(map(int,input().split()))
for k in range(0,z1[1]):
  z2=[z2[-1]] + z2[:-1]
print(*z2,end=' ')
