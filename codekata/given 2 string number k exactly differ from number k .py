z1, z2, z3 = list(map(str,input().split()))
z3 = int(z3)
count = 0
for k in range(len(z1)):
  if z1[k] != z2[k]:
     count += 1
  if count == z3:
     print("yes")
  else:
     print("no")
