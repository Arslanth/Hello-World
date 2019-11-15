# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:15:40 2019

@author: Arslanth
"""
"""
print("hello world!")
inputs= "hahaha"

type(inputs)

input("aras")

"""

name = "yeet"
 
"""if else"""   
if(name=="yeet"):
 print("this is if")
elif(name=="tiara"):
 print("this is elif")
else:
 print("this is else")
 
"""for"""
x = 0
for x in range(0,5):
 print("x")    

"""while"""
i=0
while(i<5):
 print("i")
 i+=1


""" nyoba fungsi """
def test_function_return_value(input_value):
 return input_value * 2

print(test_function_return_value(input_value = 5))


"""manipulate variabel"""
global_var = 10
def test_namespace():
 private_var = 5
 global_var = 6
 
 print("private_val", private_var)
 print("global_val", global_var)
 
test_namespace()
print("global val", global_var)

"""String operator"""

String1 = "nama "
String2 = "Aras Maulana"
String3 = "are you lis ten ing"

"""concat"""

print(String1 + String2)

"""slicing"""

print(String2[3:6])

"""lower"""

print(String2.lower())

"""upper"""

print(String2.upper())

"""Length atau len"""
print(len(String2))

"""Strip"""

print(String2.strip("A"))

"""split"""

print(String3.split(" "))




