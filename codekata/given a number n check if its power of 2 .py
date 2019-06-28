z = int(input())
y = 0
for k in range(1000):
  if k*k == z:
    y = 1
    break
if y == 1:
  print("yes")
else:
  print("no")
