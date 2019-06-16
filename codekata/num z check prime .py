z=int(input())
if z>0:
  for k in range(2,z):
    if(z%k==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
