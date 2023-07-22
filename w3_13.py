# Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.
a, b, c = input("Enter the values: ").split()
a, b, c = int(a), int(b), int(c)
if a == b == c:
    print(3 * (a + b + c))
else:
    print(a + b + c)

"""
 Write a Python program to get a newly-generated string from a given string 
 where "Is" has been added to the front. 
 Return the string unchanged if the given string already begins with "Is".
"""
str1 = input("Enter a string: ")
if str1.startswith('Is'):
    print(str1)
else:
    print(f"Is{str1}")
