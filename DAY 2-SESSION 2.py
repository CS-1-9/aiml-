# DAY 2 SESSION 1 

#Basics of Python :- 
'''
1. Variables 
2. Data types 
3. Operators 
4. Control flow conditional statements 
5. Transfer statements 
6. Loops
7. Function
'''

#Data types in python :-
'''
1. Numeric types:- integer, float, complex
2. Dictionary 
3. Boolean 
4. Set
5. Sequence types:- string, list, tuple
'''

# float data type
'''
f1 = 8932.83923
print(type(f1))
'''

# complex data type
'''
comp = 5 + 4j
print(type(comp))
# real no and imaginary no
print(comp.real)
print(comp.imag) 
'''

# dictionary data type
'''
dic = {'name':'Acharya', 'age':56,}
print(type(dic))
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
'''

# Write a python program to print Twinkle Twinkle little star poem 
'''
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("When the blazing sun is gone,")
print("When he nothing shines upon,")
print("Then you show your little light,")
print("Twinkle, twinkle, all the night.")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are! ")   
'''

# Use repel and print the table of 5 using it
'''
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
'''

'''
import pyttsx3
engine = pyttsx3.init()
engine.say("hey i am chandan in acharya institute of technology")
engine.runAndWait()
'''

# write a python program to 
'''
import os #importe the os module
# select the directory whose contents you want to list
directory_path = '/'
contents = os.listdir(directory_path)
# print the contents of the directory
print(contents)
''' 

# boolean data type
'''
bool = True
print(bool)
print(type(bool))
'''

# set data type
'''
s = {"a",5,7,8,'67.8'}
d ={}
print(type(d))
# print(type(s))
'''

# dictionary data type
'''
dict = {'name':'Acharya', 'age':56,}
#print(type(dict))
#print(dict)
#print(dict.keys())
#print(dict.values())
#print(dict.items())
dict['name'] = 'college'
dict['age'] = 60
print(dict) # dictionary is mutable we can change the values but not the keys 
'''

# Set data type
'''
s = {"a",5,7,8,'67.8'}
print(s)
print(type(s))
s.update([5])
s.update([10])
s.add("yb")
print(s)
# set is mutable datatype it cant contain duplicate values because of adding or update this is mutable datatype 
'''
# String data type
'''
st = "This is Acharya Institute of Technology"
print(type(st))
#st[7] = "i"
print(st)
# str datatype is immutable 
'''

# List data type
'''
li = [1,2,3,4,5,6]
print(type(li))
li[3] = 10
print(li)
# list is mutable datatype we can change the values by index number 
'''

# Tuple data type
'''
li = (1,2,3,4,5,6)
print(li)
print(type(li))
#li[2] = 10
print(li)
# tuple is immutable datatype we cant change the values by index number
'''

# write a python program to find an average of two numbers entered by user 
'''
A = float(input("Enter the first number"))
B = float(input("enter the second number"))
avg = (A + B) /2
print("The average of two numbers is:", avg)
''' 
'''
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print("The average of two numbers is:", (num1 + num2)/2)
'''
#write a python program to calculate the square of a number entered by user
'''
X =float(input("Enter a number :"))
square = X * X
print("The square of the number is:", square) 
'''

#floor division operator
'''
print("Enter two numbers:")
a = int(input())
b = int(input())
floor_div = a // b
print("The floor division of two numbers is:",floor_div) 
'''

'''
num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1>num2)
'''

'''
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print("The average of two numbers is:", (num1 + num2)/2)
'''
'''
a = int(input("Enter a number: "))
print("The square of the number is:", a**2)
'''

'''
import math 
X = 9
Y = 3 

print("Square root of 9 is:", math.sqrt(X))
print("9 to the power 3 is:", math.pow(X,Y))
print("Factorial of 5 is:", math.factorial(5))
print("floor value of 4.7 :", math.floor(4.7))
print("ceil value of 4.7 :", math.ceil(4.7))
'''