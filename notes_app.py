while True:
    print("\n📘 Note App")
    print("1.) Add note")
    print("2.)View Note")
    print("3.) exit")

    choice = input("Enter your choice = ")

    if choice == "1":
        note = input("Enter your note = ")
        with open("text.txt", "a") as file:
            file.write(note + "\n")

    elif choice == "2":
        try:
            with open("note.txt", "r") as file:
                print("\nYour Notes : ")
                print(file.read())
        
        except FileExistsError:
            print("No Notes found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")