#!/usr/bin/env python
# coding: utf-8

# In[10]:


class person:
    age=15
    name="riza"

p1=person()
print(p1.name)


# In[26]:


#1A
class Student:
    pass

class Marks(Student):
    pass

s1=Student()
print(isinstance(s1,Student))


m1=Marks()
print(isinstance(m1,Marks))

issubclass(Marks,Student)



# In[30]:


#1B
class COMPLEX:
    def __init__(self,real_part=0,img_part=0):
        self.real_part=real_part
        self.img_part=img_part


        
c1=

        


# In[36]:


#2A
class Songs:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    
    def sing(self):
        for i in range(len(self.lyrics)):
            print(self.lyrics[i])
        
l=["meow","boww","leee","koooo",]#add song lyrics
s1=Songs(l)
s1.sing()


# In[ ]:


class Dog:
    

