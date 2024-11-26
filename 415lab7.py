#!/usr/bin/env python
# coding: utf-8

# In[10]:


class parent:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print(f"The Car {self.brand} {self.model} is Moveing Towards Jayanager")
    
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print(f"The Boat {self.brand} {self.model} is Sailing")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print(f"The plane {self.brand} {self.model} Just took of")
        
        
car1=Car("Lamborgini","Urus")
boat1=Boat("Boston", "Whale")
plane1=plane("Airbus","A320")

vehicless=(car1,boat1,plane1)

for i in vehicless:
    i.move()

    

        


# In[15]:


class parent:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(parent):
   
    def move(self):
        print(f"The Car {self.brand} {self.model} is Moveing Towards Jayanager")
    
class Boat(parent):
    
    def move(self):
        print(f"The Boat {self.brand} {self.model} is Sailing")
class plane(parent):
    
    def move(self):
        print(f"The plane {self.brand} {self.model} Just took offf")
        
        
car1=Car("Lamborgini","Urus")
boat1=Boat("Boston", "Whale")
plane1=plane("Airbus","A320")

vehicless=(car1,boat1,plane1)

for i in vehicless:
    i.move()


# In[ ]:




