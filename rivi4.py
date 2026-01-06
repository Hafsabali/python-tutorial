file=open("C:/Users/LENOVO/Desktop/git operations.txt","r")
print(file.read())
file.close()
with open("C:/Users/LENOVO/Desktop/git operations.txt","r") as file:
    print(file.readline())
with open("C:/Users/LENOVO/Desktop/git operations.txt","r") as x:
    print(x.read(5))
with open("C:/Users/LENOVO/Desktop/git operations.txt","r") as file:
    for x in file:
        print(x)
with open("C:/Users/LENOVO/Desktop/git operations.txt","a")as file:
    file.write("Appending")
with open("C:/Users/LENOVO/Desktop/git operations.txt","r")as file:
    print(file.read())
with open("C:/Users/LENOVO/Desktop/git operations.txt","r") as file:
    file.seek(10)
    print(file.tell())
    
