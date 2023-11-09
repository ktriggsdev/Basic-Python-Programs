a=dict()
key_list = []
def readFile():
    with open("vendingitems.txt",'r') as f:
        for line in f:
            (k,v)=line.strip().split('|')
            a[k]=int(v)
    key_list=a.keys()
    print("Items available in vending machine",key_list)
    
def vendingMachine():
    readFile()
    while True:
        item=input("Enter item name\n")
        if (item in a.keys()):
            print("Valid Item Name")
            #break
            cash=int(input("Enter money to deposit\n"))
            if not isinstance(cash, int):
                print(f"Bad Input {cash}\n Try Again!")
                            #continue
            elif (cash>a[item]):
                print("Thank you for your purchase.Enjoy\n")
                print(f"Do not forget to collect your change,{cash - a[item]} Rs")
                break
            else:
                print("Not enough Money to but the item\n")
        else:
            print(f"Available Items are {a.keys()} ,\nTry Again!")
            continue
            

vendingMachine()