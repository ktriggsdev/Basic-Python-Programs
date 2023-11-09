def power_of_a_linear(x, n):
    return 1 if n == 0 else x * power_of_a_linear(x, n-1)

x = int(input("Enter the number:"))
n = int(input("Enter the power:"))
print(power_of_a_linear(x, n))
