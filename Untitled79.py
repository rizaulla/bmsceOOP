#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Student:
    
    School_name = 'ABCD School'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        return('NAme:',self.name,"Age:",self.age)

s1=Student("Harry",12)
print("Before->" "Name:" +s1.name, "age:",s1.age)

s1.name="Jessa"
s1.age= 14
print( "After-->" "Name:" ,s1.name, "age:",s1.age)

print(Student.School_name)

Student.School_name = 'ABCDefg School'
print(Student.School_name)


# In[27]:


s1.name="Jessa"
s1.age= 14
s1.show()


# In[85]:


class Student:
    
    School = 'teluska'
    Schools = 'BMSCE'
    
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def Avg(self):
            return("Name:",self.name,"Average:" ,(self.m1+self.m2+self.m3)/3)
    
   
    def info(cls):
        print(Studen.School)
        return cls.Schools
            


# In[86]:


s1=Student("riza:",34,45,32)
s2=Student("fazzi:",10,10,10)
s3=Student("Razza:",10,10,10)
s3=Student("Yash:",10,10,10)
s4=Student("YAhu:",10,10,10)
s5=Student("Fdt:",10,10,10)

print(s1.Avg())
print(s2.Avg())
print(s3.Avg())
print(s4.Avg())
print(s5.Avg())
print(s5.m1)
print(tudent)


# In[87]:


class Student:
    
    Count = 0
    
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        Student.count +=1
    def get(self):
            return("Name:",self.name,"Average:" ,(self.m1+self.m2+self.m3)/3)
    
 
    def info(cls):
        return Student.School


# In[90]:


s1=Student("riza:",34)
s2=Student("fazzi:",10)


print(s1.Avg())
print(s2.Avg())
print(s3.Avg())
print(s4.Avg())
print(s5.Avg())
print(s5.m1)


# In[94]:


class myclass:
    def __init__(self):
        self.x=x
        
    @staticmethod
    def staticMethod():
        return "i am a static Method"
    


# In[96]:


p=myclass
p.staticMethod()


# In[ ]:




