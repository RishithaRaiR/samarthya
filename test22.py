# class Person:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
#     def myfunc(self):
#         print("hello my name is" + self.name)
#     def __str__(self):
#         return "Name:" + self.name + ",Age:" + str(self.age)

# p1=Person("John", 36)
# p1.myfunc()
# print(p1)

# class Person:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
#     def myfunc(self):
#         print(f"Hello my name is {self.name} and my age is {self.age}")
#     def __str__(self):
#         return "Name:" + self.name + ",Age:" + str(self.age)

# p1=Person("John", 36)
# p1.myfunc()
# print(p1)

class Car:
    def __init__(self,brand,colour,hp):
       self.brand=brand
       self.colour=colour
       self.hp=hp
    def myfunc(self):
        print(f"brand of my car is {self.brand} and colour is {self.colour} and hp {self.hp}")
    def __str__(self):
        return "Brand:" + self.brand + ",Colour:" + str(self.colour) + ",hp:" + str(self.hp)

p1=Car("kia","white")
p1.myfunc()
print(p1)



