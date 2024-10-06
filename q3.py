''' Write a python function to check whether the given number is a perfect number or not. 
The function should returns true if the number is a perfect number, else it should returns false.
Hint: Perfect number is a positive whole number that is equal to the sum of its proper divisors.
The first perfect number is 6 as the sum of its proper positive divisors, 1,2 and 3 is 6. Other perfect numbers are 28, 496, 8128 ...
Extend the program written for the above problem to write another function to find all perfect numbers in a given list of numbers.
Populate the perfect numbers in a list and return the list.
If no perfect numbers found, return an empty list.
Note- Reuse the code wherever possible.'''
# Function to check if a number is a perfect number
def check_perfect_number(number):
    if number < 2:
        return False
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number

# Function to check for perfect numbers in a list
def check_perfectno_from_list(no_list):
    perfect_numbers = [num for num in no_list if check_perfect_number(num)]
    return perfect_numbers

# Test the function with the given sample input
perfectno_list = check_perfectno_from_list([18, 6, 4, 2, 1, 28])
print(perfectno_list)  # Expected: [6, 28]
