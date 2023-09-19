#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK 01

import random

def guessing_game():
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()


# In[ ]:


#TASK 02

import random

def number_guesser(min_value, max_value):
    secret_number = random.randint(min_value, max_value)
    
    print(f"Welcome to the Number Guesser Game! Guess a number between {min_value} and {max_value}.")
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    min_range = 1  # Minimum value of the range
    max_range = 100  # Maximum value of the range
    number_guesser(min_range, max_range)


# In[1]:


#TASK 03

import re

def password_strength(password):
    if len(password) < 8:
        return "Weak: Password should have at least 8 characters"
    if not any(char.isupper() for char in password):
        return "Weak: Password should include at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: Password should include at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return "Weak: Password should include at least one digit"
    if not re.search(r'[!@#$%^&*()-_=+[\]{}|;:\'",.<>?/]', password):
        return "Weak: Password should include at least one special character"
    
    return "Strong: Password meets all criteria"
user_password = input("Enter your password: ")
strength = password_strength(user_password)
print(strength)


# In[3]:


#TASK 04

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci_sequence(num_terms)
        print(f"Fibonacci sequence up to {num_terms} terms: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")


# In[4]:


#TASK 05

def count_words(filename):
    word_counts = {}
    
    try:
        with open(filename, 'r') as file:
            # Read the file line by line
            for line in file:
                # Split the line into words
                words = line.strip().split()
                for word in words:
                    # Remove punctuation and convert to lowercase for consistency
                    word = word.strip(".,!?\"'()-[]{}")
                    word = word.lower()
                    
                    # Update the word count
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    
        # Sort the word counts alphabetically and display
        sorted_word_counts = sorted(word_counts.items())
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = "sample.txt"  # Replace with the name of your text file
count_words(filename)


# In[ ]:




