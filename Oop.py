#constructor

class Student:
    def __init__(self,name, number):
        
       print(f"my name is {name} and my number is {number}")
       
p1 = Student("saifullah","0186453484")    

#methods

class className:
    def instanceMethods(self):
       print("helo className")
       
    @classmethod
    def classMethods(cls):
        print("helo classMethods")
        
    @staticmethod
    def staticmethod():
        print("staticmethod")
        
        
v1 = className() 
v1.instanceMethods()       
v1.staticmethod()

#abstractions





#polymorphism

class Vehicle:
    def __init__(self,Model,Brand,Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component
        
class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass

p1 = Plane("BMW-5","BMW","All Components")

c1 = Car("BMW-6","BMW-6","All Components")

print(p1.Brand, p1.Model, p1.Component)  

print(c1.Brand, c1.Model, c1.Component) 
     
     
#encapsulation
   
class Parent:
    def __init__(self, name, fathername): 
        self.__name = name
        self.__fathername = fathername
        
        print(self.__fathername, self.__name)
        
p1 = Parent("saifullah", "amanullah")        
        
     
        







        
        
       
        
   