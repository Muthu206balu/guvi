z1,z2=map(str,input().split())
list1=list(map(int,input().split()))
a=0
for k in list1:
    if k==int(z2):
        a=1
if a==1:    
     print("Yes")
else:
    print("No")
