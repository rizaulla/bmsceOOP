#!/usr/bin/env python
# coding: utf-8

# In[8]:


#parent And Sub Class
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass

class Horse(animal):
    def sound(self):
        return f"{self.name} Neighss!!!!"

h=Horse("Horse1")
print(h.name)
h.sound()



# In[19]:


class person:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"{self.name} is my name")
        

class student(person):
    def display(self):
        print(f"{self.name} is my name")

p=student("Rizaulla")

p.display()


# In[18]:


#multi_Level INheritence
class animal:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(self.name)

class Dog(animal):
    def sound(self):
        return "Bark!!"

class Bulldog(Dog):
    def run(self):
        return "Running!!"

b=Bulldog("Buddy")
print(b.show())
print(b.sound())
print(b.run())

    
        
    


# In[33]:


#Multipleinheritence
class person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)

class company:
    def __init__(self,salary):
        self.salary = salary
    def show_salary(self):
        print(self.salary)


class employee(person,company):
    def __init__(self,name,salary):
        person.__init__(self,name)
        company.__init__(self,salary)
    def display(self):
        print(self.name,self.salary)

s=employee("riza","100000")
s.show_name()
s.show_salary()
s.display()


# In[31]:


#Multilevel inheritence
class Vehicle:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(self.name)

class Car(Vehicle):
    def Milage(self):
        return "low Milage"

class sports_car(Car):
    def speed(self):
        return "HighSpeed!!"

b=sports_car("Lamborgini")
print(b.show())
print(b.Milage())
print(b.speed())


#MRO

class person:
    def display(self):
        print("Person")

class father(person):
    def display(self):
        print("father")

class mother(person):
    def display(self):
        print("Mother")

class Child(mother,father):
    pass


p1=Child()
p1.display()
print(Child.mro())
print(Child.__mro__) 
        

