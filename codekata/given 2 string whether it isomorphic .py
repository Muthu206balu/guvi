get1,get2 = input().split()
count = 0
for k in range(len(get1)):
  if get1.count1(get1[k]) == get2.count1(get2[k]):
    count += 1
if count == len(get1):
  print ("yes")
else:
  print ("no")
