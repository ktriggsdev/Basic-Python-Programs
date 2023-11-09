def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 175;
rem = sum = 0;
len = calculateLength(num);
n = num;
while (num > 0):    
    rem = num%10;
    sum = sum + int(rem**len);
    num //= 10;
    len = len - 1;
if (sum == n):    
    print(f"{n} is a disarium number");
else:    
    print(f"{n} is not a disarium number");    
