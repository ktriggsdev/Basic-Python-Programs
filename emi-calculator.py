def emi_calculator(p:float, r:float, t:float):
    """EMI Calculator for one months
    --------------------------------
    Parameters:
      p - principal 
      r - interest rate per month
      t - time period (in years)
    """
    r /= 12 * 100
    t *= 12
    return (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
 

principal = float(input("Enter principal amount (in ₹):"))
rate = float(input("Enter Interest Rate per month (%):"))
time = float(input("Enter Time period (in years):"))
emi = emi_calculator(principal, rate, time)
print("Your Monthly EMI is ₹", round(emi,2))
 
