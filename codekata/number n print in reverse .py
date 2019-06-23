get=int(input())
reverse=0
while(get>0):
  reverse=reverse*10
  reminder=get%10
  reverse=reverse+reminder
  get=get//10
print(reverse)
  
