# Linear Search in Python


def linearSearch(array, n, x):

  
    return next((i for i in range(0, n) if (array[i] == x)), -1)


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
