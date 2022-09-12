def greeting():
  name = input("Please enter your name")
  print("Hi {} , Deloitte likes to extend a heart warming welcome and geertings!!". format(name))
  
greeting()

a = int(input("number?"))
i = 2
j=0
while(i<a):
    if a%i == 0:
        j+=1
    i+=1
if j>0:
    print("Non-prime")
else:
    print("prime")
