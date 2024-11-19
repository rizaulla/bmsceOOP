#!/usr/bin/env python
# coding: utf-8

# In[2]:


class WrongAge(Exception):
    pass

class InvalidAge(Exception):
    pass


class Father:
    def __init__(self, age):
        if age < 0:
            raise WrongAge("Age must be positive")
        self.age = age


class Son(Father):
    def __init__(self, fathers_age, sons_age):
        super().__init__(fathers_age)  
        if sons_age >= fathers_age:
            raise InvalidAge("Son's age cannot be equal to or more than father's age")
        self.sons_age = sons_age
        print("Son's age is:", self.sons_age)


try:
    father = Father(30) 
    print("Father's age is:", father.age) 
    son = Son(30, 35) 
except WrongAge as e:
    print("Value Error:", e)
except InvalidAge as e:
    print("Exception:", e)


try:
    father = Father(30) 
    print("Father's age is:", father.age) 
    son = Son(30, 15) 
except WrongAge as e:
    print("Value Error:", e)
except InvalidAge as e:
    print("Exception:", e)


# In[16]:


class FormulaError(Exception):
    pass
def calculate(user_input):
    try:
        parts=user_input.split()
        if len(parts)<3:
            raise FormulaError("Invalid format- Input should consist of three elements separated by white spaces")
        num1=float(parts[0])
        operator=parts[1]
        num2=float(parts[2])
        if operator not in ['+','-']:
            raise FormulaError("Invalid operator")
        if operator =="+":
            result= num1+ num2
        elif operator =="-":
            result= num1-num2
        print("Result:",result)
    except ValueError:
        raise FormulaError("Invalid input:both numbers should be valid")
while True:
    try:
        formula=input("Enter a formula or type 'quit' to exit:")
        if formula.lower()=='quit':
            break
        calculate(formula)
    except FormulaError as e:
        print("Error",e)


# In[ ]:




