z=input()
l1=list(p)
if(l1[0]=='(' and l1[-1]==')'):
    if(l1.count('(')==l1.count(')')):
        print("yes")
    else:
        print("no")
else:
    print("no")
