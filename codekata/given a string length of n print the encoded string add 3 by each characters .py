z1=input()
z2='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
z3=''
for k in z1:
  if k in z2:
    a=z2.index(k)
    a=a+3
    z3=z3+z2[a]
print(z3)
