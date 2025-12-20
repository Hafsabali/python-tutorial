#list operations
shopping=["noodles","wafers","colddrinks"]
print(shopping[0])
print(shopping[-1])
shopping.insert(1,"ice_cream")
print(shopping)
shopping.append("macroni")
print(shopping)
print(shopping[1:3])
print(shopping[0:4:2])
shopping2=["sweets","chocolates"]
shopping.extend(shopping2)
print(shopping)
#Tuple operatios
city=("kuwait","Germany","USA")
print(city[-2])
print(city[0:3])
x=list(city)
x.append("Dubai")
city=tuple(x)
print(x)
y=list(city)
y.insert(0,"Qatar")
city=tuple(y)
print(city)
z=list(city)
z.remove("Qatar")
city=tuple(z)
print(city)
w=list(city)
w.pop()
city=tuple(city)
print(city)
city2=("india","Pakistan","Afganistan")
city+=city2
print(city)
#set operations
Degree={"BSc","Bcom","Btech"}
print(Degree)
Degree.add("BMS")
print(Degree)
Degree.add("BCA")
print(Degree)
Degree.remove("Bcom")
print(Degree)
Degree.discard("Msc")
print(Degree)
v={"BBA","BE"}
Degree.update(v)
print(Degree)
#Dictionary operations
Student={"name":"riva","Roll_no":15,"grade":"a"}
print(Student["name"])
p=Student["grade"]="O"
print(p)
q=Student.keys()
print(q)
r=Student.values()
print(r)
t=Student.items()
print(t)
Student.update({"name":"riya"})
print(Student)
Student.pop("Roll_no")
print(Student)








              














           


