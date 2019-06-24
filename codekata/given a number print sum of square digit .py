num1=int(input())
sum=0
while(num1!=0):
  d1=num1%10
  sum=sum+(d1*d1)
  num1=num1//10
print(sum)
