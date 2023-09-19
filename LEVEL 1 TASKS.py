#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 01:

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
input_str = "hello"
reversed_str = reverse_string(input_str)
print(reversed_str)  


# In[2]:


#TASK 02:

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {converted_temperature:.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {converted_temperature:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()


# In[3]:


#TASK 03:

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = "alishbah@email.com"
email2 = "invalid-email"
print(f"{email1} is valid: {is_valid_email(email1)}")
print(f"{email2} is valid: {is_valid_email(email2)}")


# In[4]:


#TASK 04:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero"
    return x % y

def calculator():
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '%' for modulus")
    
    choice = input("Enter operator: ")
    
    if choice not in ('+', '-', '*', '/', '%'):
        print("Invalid operator")
        return
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
    elif choice == '%':
        print("Result:", modulus(num1, num2))

if __name__ == "__main__":
    calculator()


# In[6]:


#TASK 05

def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]
string1 = "alishbah"
string2 = "racecar"
string3 = "hello"
string4 = "hello its me Alishbah"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")
print(f"'{string4}' is a palindrome: {is_palindrome(string4)}")


# In[ ]:




