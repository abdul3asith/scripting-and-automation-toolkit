def show_menu():
    print("AutoPro Toolkit")
    print("1. Organize Files")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        from scripts.file_organizer import organize_folder
        folder = input("Enter folder path to organize: ")
        organize_folder(folder)
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()
