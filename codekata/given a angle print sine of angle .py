import math 
z=float(input())
x=math.radians(z)
y=math.sin(x)
if(x<1):
    print(round(y,1))
elif(x>1):
    print(round(y))
