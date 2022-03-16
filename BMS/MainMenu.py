import os
from Adminpage import Admin

class mainpage:
    def menu():
        while True:
            os.system('CLS') #? Clears the terminal for ease
            print("Select any of the below: ")
            print("1 --> Login as admin")
            print("2 --> Login as user")
            print("3 --> Create a new account")
            print("4 --> Exit")
            
            choice = input("Enter: ")
            
            if choice <= "0" or len(choice) == "0" or choice > "4": #? iF USER tries to just hit the enter key!
                print("Kindly choose the correct option!")
                os.system("PAUSE")
                os.system("CLS")
                
            elif choice == "1": #? Admin Menu!
                Admin.admin_login()
                
            elif choice == "4":
                break
            

    
    
if __name__ == "__main__":
    mainpage.menu()