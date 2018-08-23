# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 07:01:07 2018

@author: vk4cs
"""

#Tips...........
#1. Each real life object has 2 types of features:
    #a. Characteristics: State of an object. e.g. Speed, color, Model etc at a specific time.
    #b. Functions: Behaviour of an object. e.g. Accelearte, Brake etc.
#2. __init__()  is the constructor of a class in Python
#3. Each function of a class starts with a parameter 'self'. We don't need to pass it explicitly.
#4. 'self' parameter of an object has the responsibility to differentiate it from other objects.
#5. Python passes the reference of an object through 'self' parameter implicitly.
#6. To get address of a class object: obj1
   
class Car:
    def __init__(self,name,color): #__init__()  is the constructor of a class in Python
        self.name=name
        self.color=color
        self.speed=0
        self.model = "old"
        
    def increase_speed(self):
        self.speed = self.speed+10
        
    def decrease_speed(self):
        self.speed=self.speed-10
        
car1       #Gets address of class object  
car1 = Car("my car","black")       
car1.color
car1.model
car1.speed
car1.name
        
car1.increase_speed()
car1.speed
        
car1.decrease_speed()       
car1.speed     
        
############BankAccount class##################
class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        
    def deposit(self,amount):
        self.balance = self.balance+amount
        
    def withdraw(self,amount):
        if (amount<self.balance):
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")
            
myAccount = BankAccount("Vishal")
myAccount.deposit(1000000)
myAccount.balance
myAccount.withdraw(110000)


###############Write a class to represent complex numbers in python############
class ComplexNumber:
    def __init__(self,real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, complexNumber):
        self.real = self.real + complexNumber.real
        self.imag = self.imag + complexNumber.imag
        
    def subtract(self, complexNumber):
        self.real = self.real - complexNumber.real
        self.imag = self.imag - complexNumber.imag
        
    def __str__(self):
        return (str(self.real)+"+i"+str(self.imag))
        
c1 = ComplexNumber(3,6)
c2 = ComplexNumber(9,8)

c1.real
c1.imag

c2.subtract(c1)
print(c2)

#############Write a class to simulate an employee in a company################
class Employee:
    def __init__(self,name,salary,isSenior):
        self.name = name
        self.salary = salary
        self.isSenior = isSenior
        
    def isSeniorEmployee(self):
        if(self.isSenior):
            print("Yes!")
        else:
            print("No!")
            
e1 = Employee("Vishal",768778, True)
e1.isSenior
e1.isSeniorEmployee()

#########Write a class to implement a television in Python######################
class Television:
    def __init__(self):
        self.state = "Off"
        self.volume = 0
        self.channel = 0
        
    def change_channel(self, number):
        if self.state == "Off":
            print("TV switched OFF. First switch it ON.")
        else:
            self.channel = number
        
    def increase_volume(self):
        if self.state == "Off":
            print("TV switched OFF. First switch it ON.")
        else:
            self.volume = self.volume + 10

    def decrease_volume(self):
        if self.state == "Off":
            print("TV switched OFF. First switch it ON.")
        else:
            self.volume = self.volume - 10
            
    def toggle_tv(self):
        if self.state == "Off":
            self.state = "On"
        else:
            self.state = "Off"



tv1 = Television()
tv1.channel
tv1.state

##########Assignment: Class to write a triangle,   
        
        