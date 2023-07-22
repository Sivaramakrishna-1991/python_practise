"""
 Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
file_name = input("Enter the file name: ")
i = 0
while i < len(file_name):
    if file_name[i] == '.':
        print(file_name[i+1:])
        break
    i += 1
