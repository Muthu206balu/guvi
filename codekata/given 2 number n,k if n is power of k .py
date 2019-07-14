z1,z2=map(int,input().split())
flag=0
for k in  range(1,z1):
    if z2**k==z1:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
