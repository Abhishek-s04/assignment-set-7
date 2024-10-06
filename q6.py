'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
Write a python program to find and display the number of circular primes less than the given limit.
'''
def check_prime(number):
    """Check if the given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def rotations(num):
    """Return a list of all circular rotations of the digits of the given number."""
    num_str = str(num)
    rotations_list = []
    for i in range(len(num_str)):
        # Rotate the digits and append to the list
        rotated_num = num_str[i:] + num_str[:i]
        rotations_list.append(int(rotated_num))
    return rotations_list

def get_circular_prime_count(limit):
    """Return the count of circular primes below the given limit."""
    circular_prime_count = 0
    
    for num in range(2, limit):
        # Get all rotations of the number
        num_rotations = rotations(num)
        
        # Check if all rotations are prime
        if all(check_prime(rot) for rot in num_rotations):
            circular_prime_count += 1
    
    return circular_prime_count

# Provide different values for limit and test the program
print(get_circular_prime_count(1000))  # Output should be the count of circular primes below 1000
