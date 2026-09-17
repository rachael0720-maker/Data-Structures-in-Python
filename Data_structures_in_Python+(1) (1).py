#!/usr/bin/env python
# coding: utf-8

# # Practice Exercise

# Question 1: Print a random integer between 100 and 135

# In[1]:


# Import required libraries:
import numpy as np
from random import seed
from random import randint
# Print a random integer in the given range:
print(randint(10,345))


# Question 2: Create a list consisting of first 10 even numbers.

# In[2]:


# Create a list according to the given condition:
list1=[2,4,6,8,10,12,14,16,18,20]


# Question 3: Create a list in the following manner: [birthyear, firstname, birthdate, lastname]

# In[3]:


# Create a list according to the given condition:
list2=['birthyear','firstname','birthdate','lastname']


# Question 4: Create a nested list which consist of 2 students and their scores in mathematics and english:
# 
# Students: Alex and Cody
# 
# Alex scores 97 and 95 in mathematics and english respectively,
# 
# Cody scores 89 and 92 in mathematics and english respectively.
# 
# The list should be such that it first stores the name of students followed by the subjects and then their scores in nested lists.

# In[4]:


# Create a list according to the given condition:
list3=[['Alex','Cody'],["Mathematics","English"],[97,95],[89,92]]
print(list3)


# Question 5: Given below is a list, find out whether is has the letter 'k' in it and print the result as true or false.

# In[5]:


# Given below is a list:
list3=[1,2,'r',7,'k',6,'o','h','d',5,9]

# Define the character you are searching for:
k='k'

# print the result:
print(k in list3)


# Question 6: In the tuple given below, print the 3rd element.

# In[6]:


# Given below is the tuple:
tuple1=(1,'hello','world','567')
 
# Print the 3rd element:
print(tuple1[2])


# Question 7: Given below is a tuple. Sort the tuple and print the result.

# In[7]:


# Given below is the tuple:
tuple2=(1,25,67,100,3,54)
tup=sorted(tuple2)

# Sort the tuple:
print(tup)
# Print the result:


# Question 8: Given below is a list, convert into a set and print the output also print the length of the set.

# In[8]:


# Given below is the list:
list4=[1,2,4,6,3,2,5,4,7,4,6,5,3,2,2,1]

# Convert the list into set:
set1=set(list4)

# Print the result:
print(set1)

# Print the length of the set:
print(len(set1))


# Question 9: Given below are two sets, perform the operations given below:
# 1. Print their union
# 2. Print their intersection
# 3. Print their difference
# 4. Print their symmetric difference

# In[9]:


# Given below are two sets:
a={1,2,3,5,6,7}
b={4,5,8,9,2,3}

# Print their union:
print(a.union(b))

# Print their intersection:
print(a.intersection(b))

# Print their difference:
print(a.difference(b))
# Print their symmetric difference:


# Question 10: Create a dictionary that stores the names and roll numbers of 5 students as given below:
# 1. Sam, 21
# 2. Cody, 12
# 3. Addy, 3
# 4. Zach, 45
# 5. Amy, 6

# In[18]:


# Create a dictionary:
dict1={'Sam':21,'Cody':12,'Addy':3,'Zach':45,'Amy':6}
# Print the result:
print(dict1)


# Question 11: Due to admission of new students the roll number of zach has changed from 45 to 47. Make the required changes and print the new dictionary.

# In[19]:


# Update the roll number:
dict1['Zach']=47
# Print the new dictionary:
print(dict1)


# Question 12: Sort the dictionary according to roll number.
# 

# In[20]:


# Sort and print the students roll number wise in ascending order:
sorted(dict1)


# In[ ]:




