''' Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.
Sample Input : 1122334455ababzzz@@@123#*#* 
Expected Output: 12345abz@#*  
'''
# Function to remove duplicate characters from a string
def remove_duplicates(value):
    result = ""
    for char in value:
        if char not in result:
            result += char
    return result

# Test the function with the given sample input
print(remove_duplicates("1122334455ababzzz@@@123#*#*")) 
#you can also make it user input
value=input('enter the value : ')
print(remove_duplicates(value))