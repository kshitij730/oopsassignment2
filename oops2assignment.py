#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example."""


# In[2]:


"""
In Object-Oriented Programming (OOP), an "object" refers to a fundamental concept that represents a real-world entity or concept within a software program. It is a self-contained unit that combines data (attributes) and functions (methods) that operate on that data. Objects are instances of classes, which are blueprint or template definitions that describe the structure and behavior of objects"""
"""
In Object-Oriented Programming (OOP), a "class" is a blueprint or template that defines the structure and behavior of objects. It serves as a prototype for creating instances of objects with similar characteristics and behaviors. A class defines the attributes (data members) and methods (functions) that the objects of that class will have."""

class class1:
    def student(self, name, rollno):
        self.name = name
        self.rollno = rollno


# In[6]:


stu1 = class1()


# In[7]:


"""Name the four pillars of OOPs."""


# In[8]:


"""1. Encapsulation
   2. Abstraction
   3. Inheritance
   4. Polymorphism"""


# In[9]:


"""Explain why the __init__() function is used. Give a suitable example."""


# In[10]:


"""__init__() is a constructor"""

class vehicles:
    def __init__(self, year, make, model, speed):
        self.year = year
        self.make = make
        self.model = model
        self.speed = speed


# In[18]:


c = vehicles(2021, "toyota", "fotuner", 300)


# In[19]:


c.speed


# In[14]:


c.model


# In[15]:


c.make


# In[16]:


c.year


# In[20]:


"""Why self is used in OOPs?"""


# In[21]:


"""In Object-Oriented Programming (OOP), the term "self" is commonly used to refer to the instance of the class within the class's own methods and attributes. It's essentially a way for an object to refer to itself, allowing it to access its own attributes and methods. The usage of "self" varies based on the programming language you're using"""


# In[22]:


"""What is inheritance? Give an example for each type of inheritance."""


# In[23]:


"""SINGLE INHERITANCE"""

class Parent:
    def method(self):
        print("Method from Parent class")

class Child(Parent):
    pass

child_obj = Child()
child_obj.method()  


# In[24]:


"""MULTIPLE INHERITANCE"""

class Parent1:
    def method(self):
        print("Method from Parent1 class")

class Parent2:
    def method(self):
        print("Method from Parent2 class")

class Child(Parent1, Parent2):
    pass

child_obj = Child()
child_obj.method()  


# In[25]:


"""MULTILEVEL INHERITANCE"""

class Grandparent:
    def method(self):
        print("Method from Grandparent class")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child_obj = Child()
child_obj.method()  

