'''Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 
'''
def nearest_palindrome(number):
    # Increment the number to find the next palindrome
    number += 1
    while True:
        # Convert the number to a string to check if it reads the same forward and backward
        if str(number) == str(number)[::-1]:
            return number
        number += 1

# Test the function
number = 12300
print(nearest_palindrome(number))  # Output: 12321
