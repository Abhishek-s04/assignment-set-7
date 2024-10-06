''' Write a python function, check_anagram() which accepts two strings and returns True,
if one string is a special anagram of another string. Otherwise returns False.
The two strings are considered to be a special anagram if they contain repeating 
characters but none of the characters repeat at the same position. The length of the strings should be the same.
Note: Perform case insensitive comparison wherever applicable.'''
# Function to check if two strings are special anagrams
def check_anagram(data1, data2):
    # Perform case insensitive comparison
    data1 = data1.lower()
    data2 = data2.lower()
    
    # If lengths of strings are not equal, return False
    if len(data1) != len(data2):
        return False
    
    # Iterate over the strings to check if characters match but not at the same position
    for i in range(len(data1)):
        if data1[i] == data2[i]:
            return False
    
    # Sort both strings to check if they have the same characters irrespective of the order
    return sorted(data1) == sorted(data2)

# Test the function with given sample inputs
print(check_anagram("eat", "tea"))         # Expected: True
print(check_anagram("backward", "drawback")) # Expected: False
print(check_anagram("Reductions", "discounter"))  # Expected: True
print(check_anagram("About", "table"))     # Expected: False
