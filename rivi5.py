import os
import shutil
cwd=os.getcwd()
print("Current working directory is:",cwd)
cwd1=os.chdir("C:/Users/LENOVO/Desktop")
print(os.getcwd())
print(os.path.exists("C:/Users/LENOVO/Documents/rivi.py"))
x=os.mkdir("HELLO")
print(os.path.exists("HELLO"))
print(os.listdir())
print(os.getcwd())
print(os.path.getsize("C://Users/LENOVO/Documents/rivi.py"))
os.rmdir("HELLO")
