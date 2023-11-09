#This file generates a CSV file with integer values, 
# Use cases: you can use it for eg. input for testing your sroting algorithms and other program inputs when you need to test with large data.

import random as rd; 

minNum = 0;
maxNum = 1000
lengthOfItems= 500
with open("newFile.csv", "a") as file:
    for _ in range(lengthOfItems):
        file.write(str(f"{str(rd.randint(minNum, maxNum))},"))
#note - you will have to split first line at "," and convert to int 
