# Write a Python program to test whether a number is within 100 of 1000 or 2000.
def near_thousand(num):
    return (1000 - num <= 100) or (2000 - num <= 100)


print(near_thousand(950))
print(near_thousand(1000))
print(near_thousand(800))
