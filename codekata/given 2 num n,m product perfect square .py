z1,z2=map(int,input().split())
mul=z1*z2
for k in range(0,mul+1):
  if(k**2==mul):
    print('yes')
    break
else:
  print('no')
