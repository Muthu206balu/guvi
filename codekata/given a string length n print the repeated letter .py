get = input()
a = []
for k in range(len(get)):
  a.append(get.count(get[k]))
k = a.index(max(a))
print (get[k])

#explanation
# consider string - aabbbc
# a list will be 2,2,3,3,3,1
# max of a will return 3
# index of 3 will give the 1st index of 3 in a list # # that is 2
# finally get[2] will be printed as the most repeated   #  character 
