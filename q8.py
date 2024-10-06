'''Use Luhn algorithm to validate a credit card number.
A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:
Step 1a: From the second last digit (inclusive), double the value of every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2
Note: If any number is greater than 9, then sum the digits of that number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2
Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34
Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72
Step 3: If the total is divisible by 10 then the number is valid else it is not valid.
Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. 
'''
def validate_credit_card_number(card_number):
    # Convert the card number to a string to process each digit
    card_number_str = str(card_number)
    
    # Check if the length of the card number is 16 digits
    if len(card_number_str) != 16:
        return False
    
    total_sum = 0
    length = len(card_number_str)
    
    # Iterate through the card number from the end
    for i in range(length - 1, -1, -1):
        digit = int(card_number_str[i])
        
        # Double every second digit starting from the second last
        if (length - i) % 2 == 0:  # Check if position is even from the right
            digit *= 2
            # If the digit is greater than 9, sum its digits
            if digit > 9:
                digit = digit - 9  # Equivalent to summing the digits (e.g., 18 -> 1 + 8)

        # Add to total sum
        total_sum += digit
    
    # Step 3: Check if total_sum is divisible by 10
    return total_sum % 10 == 0

# Test the function with the provided card number
card_number = 5239512608615007  # Change this number to test different cases
result = validate_credit_card_number(card_number)

if result:
    print("Credit card number is valid")
else:
    print("Credit card number is invalid")
