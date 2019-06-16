string=input()
letter=False
number=False
for z in string:
  if z.isalpha():
    letter=True
  if z.isdigit():
    number=True
if letter and number:
  print('Yes')
else:
  print('No')
