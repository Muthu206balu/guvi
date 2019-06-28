zx1=input().split()
z2=input().split()
z3=input().split()
if(zx1[0]==z2[0]==z3[0] or zx1[1]==z2[1]==z3[1] or (zx1[0]==zx1[1] and z2[0]==z2[1] and z3[0]==z3[1])):
    print('yes')
else:
    print('no')
