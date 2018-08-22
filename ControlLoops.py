# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 06:11:38 2018

@author: vk4cs
"""

#####################Conditional statements.................
a = 10
b = 15
choice = 0
if(choice == 0):
	c = a+b 
	
print(c) #Output: 25

if(choice==1):
	c=a-b	
    
print(c) #25

if(choice>-5):
	print("yes, choice is more than -5") #Output: yes, choice is more than -5
    
if(choice<-2):
	print("hgfhjg")

#If conditional statements are not well indented, it will give a syntax error
if(choice==1):
print("jgyhgj") #SyntaxError: expected an indented block

a = True #Boolean variable
print(a) #Output: True

if(a):
	print("YES") #Output: YES
    
a = 1==2
a #Output: False

a=1<2
a #Output: True

if(True):
	print("Yes boolean") 
if(False):
	print("Something")
#Output: Yes boolean
	
myvar = 10
if(myvar<5):
	print("variable is less than 5")
else:
	print("variable is more than 5")
#Output: variable is more than 5    
    
age = 16
if(age>18):
	print("allowed")
else:
	print("underaged")	
#Output: underaged
    
age=19
if(age>18):
	print("allowed")
else:
	print("underaged")	
#Output: allowed
    
c = True or False
c #Output: True

c = True and False
c #Output: False

c = not True
c #Output: False

d = True
c = not d
d #Output: True
c #Output: False

c = 3>2 and 3<7
c #Output: True

c = 1==1 and 2==2 and 2<3 and 2>1 and 1==2
c #Output: False

c = (1==1 or 2>3) and (3==4)
c #Output: False

#Positive-Negative Number: Input a number & display if the number is positive or negative
n = float(input("Enter a number: "))    

if(n<0):
    print("The number is negative.")
elif(n==0):
    print("Zero")
else:
    print("The number is positive.")
        

#Input the marks of a student & display the grade, based on grading policy
marks = int(input("Enter the marks: "))

if(marks>=90):
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("FAIL")
    
###########################################################Loops...................
for i in range(1,5):
    for j in range(1,5):
        print(i, j)        
    
#Print some pattern:
for i in range(1,5):
    for j in range(1,6-i): 
        print(" ",end='')
    for j in range(0,2*i-1):
        print("*",end='')
    print("")
    
#Print some more pattern:
for i in range(1,10):
    for j in range(1,i):
        print("*",end='')
    print("")        
    
#Write a program that takes an input of 2 numbers & print their LCM:
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

for i in range(1,a*b+1):
    if(i%a==0) and (i%b==0):
        print("The LCM is: ",i)
        break
    
    
#WAP to count the number of digits in a number:
n = int(input("Enter a number: "))

count = 1
while n>count:
    count=count+1
    n=n//10  #integer division: // - quotient
print(count)
    
#To do: Armstrong number: Assignment - Sum of the cubes of individual digits is the same number    
    