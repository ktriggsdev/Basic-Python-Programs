print("An Armstrong Number is a number which is equal to the sum of the cubes of it's digits.")
inputNumber = input("Enter a number to check if it's an Armstrong Number or not: ")
sumOfCubes = sum(int(digit)**3 for digit in inputNumber)
if sumOfCubes==int(inputNumber): print(inputNumber,"is an Armstrong Number.")
else: print(inputNumber,"is NOT an Armstrong Number.")
