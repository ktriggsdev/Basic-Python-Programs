#default password is 4758
import random
class BankGame :
    @staticmethod
    def main( args):
        print("---WELCOME TO ELIX BANKING SERVICES---")
        print("")
        print("________________________")
        print("Enter your name: ")
        name = input()
        # I am inserting do loop to make the program run forever under correct inputs.
        print(f"Hi, {name}" + "\bWelcome to my program!")
        print("____________________________")
        print("Do you want to start/repeat the program?")
        print("Enter Y for Yes and N for No: ")
        temp = input()[0]
        passw = 4758
        bal = 10000
        leftbal = 0
        print("If you don\'t know the password refer the first line of the program")
        print("Please enter the password: ")
        # Condition when the statement goes true i.e.- temp equals 1
        while True:
            if temp in ['Y', 'y']:
                if (passw == 4758):
                    print("")
                    print("Your initial account balance is Rs. 10000")
                    for _ in range(7):
                        print("0. Exit")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Change passcode")
                        print("4. Check balance")
                        print("5. Customer care")
                        print("Enter the serial no. of your choice")
                        choice = int(input())
                        print("Enter captha to verify that you are not a robot.")
                        captha = random.randrange(10000)
                        print(captha)
                        print("Enter the number shown above: ")
                        verify = int(input())
                        if (verify == captha):
                            # If captha gets matched, then these switch statements are executed.
                            if choice == 0:
                                print(f"BYE!......{name} HAVE A NICE DAY!")
                                print("__________________________")
                                print("@author>[@programmer-yash")
                                print("Please comment here or open an issue if you have any queries or suggestions!")
                                print("")
                                print("#hacktoberfest")
                                return 0
                            elif choice == 1:
                                print("You have chosen to deposit.")
                                print("Enter the amount to deposit : ")
                                deposit = int(input())
                                bal = bal + deposit
                                print(f"{deposit} has been deposited to your account.")
                                print(f"Left balance is {str(bal)}")
                            elif choice == 2:
                                print("You have chosen to withdraw.")
                                print("Enter the amount to be withdrawn")
                                withdraw = int(input())
                                print(f"{str(+withdraw)} has been withdrawn from your account.")
                                bal = bal - withdraw
                                print("Check the cash printer.")
                                print(f"Left balance is {str(bal)}")
                            elif choice == 3:
                                print("You have chosen to change passcode.")
                                print("Enter the current passcode: ")
                                check = int(input())
                                if (check == passw):
                                    print("Enter the new passcode")
                                    newP = int(input())
                                    passw = newP
                                    print(f"Your new password is {passw}")
                                else:
                                    print("Wrong passcode!")
                            elif choice == 4:
                                print("You have chosen to check balanace.")
                                print(f"Your current account balance is {str(bal)}")
                            elif choice == 5:
                                print("You have chosen for customer care.")
                                print("Contact us at:")
                                print("          Email: yash197911@gmail.com")
                            else:
                                print("Wrong choice!!! Choose again...!")
                        else:
                            print("xCAPTHA NOT CORRECTx")
                continue
            elif temp in ['N', 'n']:
                print(f"BYE!......{name} HAVE A NICE DAY!")
                print("__________________________")
                print("@author>[@programmer-offbeat]")
                print("Please comment here if you have any queries or suggestions!")
                print("--OR--")
                print("create an issue")
                print("I will rightly see and reply to your messages and suggestions!")
                print()
                print("HAPPY CODING!:-)")
                return 0
            else:
                print("Err!..... You have entered a wrong choice!")
                print("Try again....!")
            # Comdition if password mismatches.
            if (passw != 4758) :
                print("You have entered wrong password.....Try again!")
            if temp >= 100:
                break
    

if __name__=="__main__":
    BankGame.main([])
