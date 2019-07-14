z=int(input())
b=list(map(int,input().split()))
c=b
b.sort()
if b==c:
    print("yes")
else:
    print("no")
