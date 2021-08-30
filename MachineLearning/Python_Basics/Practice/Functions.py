#System defined functions..
s = "this is a string"
len(s)


#Userdefined Function - 1
def my_function():
    print("I am a function")
    
my_function()


#Userdefined Function - 2
def square(n):
    print("The square of ",n,"is",n*n)

square(5,7)


#Userdefined Function - 3
def product(x,y):
    print("The product is ",x*y)
    
product(4,6)


#Userdefined Function - 4
def foo(x):
    return x+1;

a = foo(3)


#Global-local variables in a function
myvar = 10
def foow():
    global myvar #Global variable
    myvar = myvar+1
    print(myvar)
    
print("Before function call, value is: ",myvar)
foow()
print("After function call, value is: ",myvar)


#Lambda functions:
product = lambda x1,x2:x1*x2

product(4,5)


#Function - Function that takes a number & checks for its equality with a global variable 
var = 10
def f1(x):
    global var
    if x== var:
        print("Yes")
    else:
        print("No")
        
        
f1(1)
f1(10)        


#WAF that takes inputs a string & a number, then it prints that string those many number of times
def print_string(string_name, times):
    for i in range(0,times):
        print(string_name)
        
print_string("I am a good programmer",3)
print_string("You guys are really doing great", 10)

#WAF that calls itself(recursion):
def recursion_function(n):
    if n>0:
        print(n)
        recursion_function()
        
recursion_function(10)


#WAF that generates sum of digits in the input number
def sum_of_digits(n,store):
    if n>0:
        sum_of_digits(n//10,store+n%10)
    else:
        print(store)

sum_of_digits(123,0)
sum_of_digits(98,0)


#To do: WAP for factorial
















        
        
        






