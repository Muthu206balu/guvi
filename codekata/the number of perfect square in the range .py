z1, z2 = list(map(int,input().split()))
count = 0
for k in range(1,101):
if k*k >= z1 and k*k <= z2:
count += 1
print(count)
