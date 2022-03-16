import os

class Admin:
    def admin_login():
        while True:
            adminname = input("Enter username: ")
            adminpass = input("Enter password: ")
            
            if adminname == "admin" and adminpass == "admin":
                print("Successfully logged in")
                os.system("PAUSE")
                os.system("CLS")
                break
            
            else:
                print("Invalid credentials")
                os.system("PAUSE")
                os.system("CLS")
                break