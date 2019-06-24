l1,r1=map(int,input().split())
for k in range(1,100001):
  if((k%l1==0) and (k%r1==0)):
    print(k)
    break
