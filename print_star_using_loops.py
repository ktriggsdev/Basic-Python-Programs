print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if not new:
    for i in range(one,0,-1):
        for _ in range(1,i+1):
            print("*", end="")
        print()

else:
    for i in range(1,one+1):
        for _ in range(1,i+1):
            print("*",end=" ")
        print()
