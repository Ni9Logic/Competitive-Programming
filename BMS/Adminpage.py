import os

class Admin:
    def admin_login():
        while True:
            adminname = input("Enter username: ")
            adminpass = input("Enter password: ")
            if adminname == "admin" and adminpass == "admin":
                pass
            else:
                print("Invalid credentials")
                os.system("PAUSE")
                os.system("CLS")
                break