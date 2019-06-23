z1,z2,z3=map(int,input().split())
sum=0
for i in range(1,z3+1):
 sum+=z1+(z3-i)*z2
print(sum)
