#1st day 
print("hello","world",sep="--",end="\n")
i=1
while i<10:
    print(i)
    i+=2
for i in range(1,10):
    if i%2==0:
        continue
    else:
        print(i)
name=input("Enter your name")
age=int(input("Enter your age:"))
if age<18:
    print("You are teenager")
elif age>18:
    print("You are an adiult")
else:
    print("invalid")
x=int(input("Enter your date of birth (DD)"))
b=int(input("Enter you month (MM)"))
m=int(input("Enter you year(YYYY)"))
age=2025-m
print("You are now",age,"years old")
z=0
j=int(input("Enter how many times you want to see"))
while z<j+1:
      print("*",end="\n\n")
      z+=1
c="hafsa"
v="bali"
print(f"your name is {c} and you last name is {v}")
print("hay {} {}".format(c,v))

      
        

