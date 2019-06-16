z=int(input())
x,y=map(int,input().split())
for k in range(x+1,y):
  if(k==z):
    print('yes')
    break
else:
  print('no')    
