
#functions in python 
def sum(x,y):
    return x+y
result=sum(3,2)
print(result)
def calculator(a,b):
    inputno=input("Enter operator(+ - * /):")
    if inputno=="+":
        return a+b
    elif inputno=="-":
        return a-b
    elif inputno=="*":
        return a*b
    elif inputno=="/":
        return a/b
    else:
        print("wrong input")
re=calculator(5,4)
print(re)
def about(fname,lname):
    print("Hey",fname,"your last name is ",lname)
about("henry","john")
def myfunc():
    print("hello guys")
myfunc()
def shopping(*items):
    print("i like", items[2], "the most")
shopping("maggi","noodels","samosa","pizza")
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=factorial(4)
print(num)
def fun(**kids):
    print("The ",kids["fname"],"is the elder")
fun(fname="john",lname="babbage")
#lamda funtion
x=lambda a,b:a+b
num1=x(2,2)
print(num1)


