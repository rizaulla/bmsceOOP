#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math

n=365
k=1
x=[]

for i in range(n,0,-1):
    j=i/365
    x.append(j)
    k=math.prod(x)
    if k<=0.5:
        break

print("the minimum",len(x))



# In[16]:


from abc import ABC,abstractmethod

class polygon(ABC):
    @abstractmethod
    def noofside(self):
        pass


class Triangle(polygon):
    def noofside(self):
        print("I have 3 sidees")
        
class quadrilateral(polygon):
    def noofside(self):
        print("I have 4 sidees")

class Pentagon(polygon):
    def noofside(self):
        print("I have 5 sidees")
        
class Hexagon(polygon):
    def noofside(self):
        print("I have 6 sidees")

class octagon(polygon):
    def noofside(self):
        print("I have 8 sidees")
        
        
k=Triangle()
k.noofside()

q=quadrilateral()
q.noofside()

p=Pentagon()
p.noofside()

h=Hexagon()
h.noofside()




# In[15]:


from abc import ABC,abstractmethod

class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
    def color(self):
        pass
    
    
class Apple(Fruit):
    def taste(self):
        print("Tangy")
    def color(self):
        print("Tangerine")
        
class Mangoe(Fruit):
    def taste(self):
        print("Sweeet")
    def color(self):
        print("yellow")   

        
a=Apple()
a.taste()
a.color()

m=Mangoe()
m.taste()
m.color()


# In[ ]:




