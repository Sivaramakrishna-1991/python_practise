"""Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
date1 = (2014, 7, 2)
date2 = (2014, 7, 11)
no_of_days = 0
for i, j in zip(date2, date1):
    no_of_days += i - j
print(no_of_days, "days")
