z1=int(input())
z2=input()
temp1=0
v=['a','e','i','o','u']
for k in v:
  if(k in v):
    z2=z2.replace(k,'')
print(z2[::-1])
