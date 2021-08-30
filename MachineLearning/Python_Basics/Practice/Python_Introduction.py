#####Tips:
#1. IDLE is an editor, can also be used to write Python applications.
#2. Expressions = Values + Operators
#3. To get any help on Python, we can use following options:
  #a. Stackoverflow
  #b. Pastebin.com
  #c. gist.github.com

#Expression evaluation
'Hello' #Output: 'Hello'
2+2 #Output: 4
250//2 #Output: 125

  
#Multiple variable declarartion
a,b,c = 1,2,"your_name"

# deleting memory of a variable
del a

#Multiline string 
a = """This is tom.
tom loves to play with python."""

#String - Capitalize & Upper functions.
b = "hi this is me!!!"
b.capitalize()  #Result: 'Hi this is me!!!'
b.upper()       #Result: 'HI THIS IS ME!!!
b.lower() #Result: 'hi this is me!!!'

#string - count (count() is case sensitive)
a = "this is a ball. this is a bat. This is a boy playing cricket in this field"
a.count("this") #Result: 3

a =  "www.google.com"
a.endswith(".com") #Result: True
a.endswith("dwjh") #Result: False
a.find("google") #Result: 4
a[5] #Result: 'o'
a[4] #Result: 'g'

a = "google google"
a.find("google") #Result: 0
a.islower() #Result: True
a = "this is me playing cricket on a cricket ground"
a.replace("cricket","football") #Result: 'this is me playing football on a football ground'

#String concatenation
test = 'Hello'
test + ' World' #Output: 'Hello world'

#String Multiplication
'Vishal ' * 11 #Output: 'Vishal Vishal Vishal Vishal Vishal Vishal Vishal Vishal Vishal Vishal Vishal '

'Hello'+'!'*10 #Output: 'Hello!!!!!!!!!!'


#Join.....................................
','.join(['cats','rats','bats'])
print('\n\n'.join(['cats','rats','bats']))

#Split....................................
'My name is Vishal'.split()
'My name is Vishal'.split('m')

#rjust, ljust, center
'Hello'.ljust(10)
'Hello'.rjust(10)

'Hello'.ljust(10,'*')
'Hello'.rjust(10,'*')

'Hello'.center(10)
'Hello'.center(10,'*')

#strip, lstrip, rstrip
spam = 'Hello'.center(10)
spam.strip() #It does not strip in place rather creates a brand new string
spam

spam.lstrip()
spam.rstrip()

'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')

#replace........
spam = 'Hello there!'
spam.replace('e','XYZ')

#Pyperclip - copy/paste
##########Installing pyperclip...........
##conda: conda install -c bryanwweber pyperclip 
##IDLE: 
    #cmd->cd "Program Files\Python 3.5\Scripts"
    #pip.exe install pyperclip
import pyperclip
pyperclip.copy('Hello!!!!!!!')
pyperclip.paste()
