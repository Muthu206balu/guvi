z,z1=map(int,input().split())
input()
m1=list(map(int,input().split()))
m2=list(map(int,input().split()))
for a in m2:
    m1.append(a)
    print(max(m1),end=' ')
