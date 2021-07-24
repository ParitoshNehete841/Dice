import random

x=int(input(" choose no of dices to roll:"))

n1= random.randint (1, 6)
n2 = random.randint (1, 6)
n3= random.randint (1, 6)
n4= random.randint (1, 6)
if x==1:
  print (n1)
elif x==2:
  print(n1,n2,"total:",n1+n2)
elif x==3:
  print (n1,n2,n3,"total:",n1+n2+n3)
elif x==4:
  print (n1,n2,n3,n4,"total:",n1+n2+n3+n4)
else:
  print("more than 4 dices chossen")
