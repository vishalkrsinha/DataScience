# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:06:59 2018

@author: vk4cs
"""
import webbrowser as wb, sys, pyperclip
# Check if command line arguments were passed
if len (sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
wb.open(r'https://www.google.com/maps/place/'+address)