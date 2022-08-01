import source_code

if __name__ == "__main__":
    while True:
        print("What type of pdf is created: ")
        print("1 --> Merged Pages")
        print("2 --> Un-Merged Pages")
        print("3 --> Exit")
        
        choice = input("Enter: ")
        if choice == "1":
            source_code.program()
        elif choice == "3":
            break
        else:
            continue