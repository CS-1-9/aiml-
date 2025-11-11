## write a program to find if the given number is a odd number

'''num = 5
if (num % 2 != 0):
    print(num, "is an odd number")
else:
    print(num, "is not an odd number")
'''


## write a program to find the square root of the number

'''num = float(input("Enter a number: ")) 
sqrt = num ** 0.5   
print("The Square Root of the Number is :",sqrt)
'''


## write a program to find the perfect square root of a numbe
'''
num = 64
num2 = 65
sqrt1 = num ** 0.5
sqrt2 = num2 ** 0.5

print(sqrt1 * sqrt1 == num, sqrt1 * sqrt1)
print(sqrt2 * sqrt2 == num2, sqrt2 * sqrt2)

print(num ** 0.5 % 1 == 0)
print(num2 ** 0.5 % 1 == 0)
'''

## write a program to check if the given string is a palindrome
#step 1: reverse the string
#step 2: compare with the original string
#step 3: if both are same it's a palindrome and  return true, else false.

'''
String = input("Enter a string: ")
rev_string = String[::-1]
if String == rev_string:
    print(f"{String} is a palindrome")
else:
    print(f"{String} is not a palindrome")
'''
