# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:27:52 2018

@author: vk4cs
"""

"""List"""
#Defining & Initializing a 1D list
zoo_animals = ["sdjhs","erewrew","erewrew","erewr"]

zoo_animals[0] #Accessing individual list item
zoo_animals[1]
zoo_animals[2]
zoo_animals[3]
zoo_animals[-1]
zoo_animals[-2]

#2D list...
spam = [['cat','bat'], [10,20,30,40,50]]
spam[0]
spam[0][1]
spam[1][4]
spam[-1]

#Another example: List can contain hetrogeneous data items
lst = ["One","Two","Three",4,5,6,4.5,5.6,True,False]
lst[0]
lst[1]
lst[2]
lst[4]
lst[7]
lst[9]
lst[-1]
lst[-2]

#Iterating list items directly
for i in lst:
    print (i)
    
#Iterating list items through range
for i in range(0,10,4):
    print (lst[i])
    

#Search the item in list
for i in range(0,10):
    if lst[i] == True:
        print("Matching Index: ",i)
        
#######################################################################
"""Tuple...."""
##A Tuple has 2 advantages over a list:
#1. Once values declared in a tuple, can't be changed later
#2. A Tuple is faster than a List
x = ("One","Two","Three",4,5,6,4.5,5.6,True,False)
for i in x:
    print(i)
    
x[5] = 9

y = ((1,2,3),(5,6,7))
y[1][2]

#######################################################################
"""Dictionary"""
myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'} #Dictionary
myCat['color']

myCat.pop('size') #Deleting an item from the dictionary
myCat

#Verifying if a key exists in the dictionary
'size1' not in myCat 
'size' in myCat

#Getting dictionary keys
myCat.keys()

#Getting dictionary keys
myCat.values()

#Getting dictionary keys & values together
for k, v in myCat.items():
    print (k, v)
    
#Getting dictionary keys & values together
for i in myCat.items():
    print (i)
    
myCat['coloqr']

if 'coloqr' in myCat:
    print(myCat['coloqr'])

###Appending items to Dictionary
allCats=[]
allCats.append({'name':'Zophie','age':7,'color':'gray'})
allCats.append({'name':'Pooka','age':5,'color':'black'})
allCats.append({'name':'Fat-tail','age':7,'color':'gray'})
allCats.append({'name':'???','age':-1,'color':'orange'})
allCats
