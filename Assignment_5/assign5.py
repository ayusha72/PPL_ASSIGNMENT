
print("Example for handling indexerror")
# Python program to handle simple runtime error 
  
a = [1, 2, 3] 
try:  
    print("Second element = %d" %(a[1])) 
  
    # Throws error since there are only 3 elements in array 
    print("Fourth element = %d" %(a[3]))  
  
except IndexError: 
    print("An error occurred")
print("handling which type of error introduced")
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
print("handling exception when file is not found")
#Raising exceptions for file handling, if the file is not found in the given directory
try:
    file = open("Assignment.txt","r")
    for line in file:
        print(line)
except:
    print("File Doesn't exist")

print("Raising an exception  ")
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 
