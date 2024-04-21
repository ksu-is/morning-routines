name = input("Hello! Please tell me your name")
print("Hello ", name, " Would you like a morning routine or night routine? Please press 1 for morning or 2 for night")
morn= input("Enter the number corresponding to your choice: ")
def display_morning_menu():
    print("Morning Routine Menu:")
    print("1. Exercise")
    print("2. Meditate")
    print("3. Read")
    print("4. Breakfast")
    print("5. Take a Shower")
    print("6. Quit")
def create_morning_routine():
    routine = []
    while continue = True:
        display_morning_menu()
        choice = input("Enter the number corresponding to your choice: ")
        if choice == '6':
            continue = False
        elif choice in ['1', '2', '3', '4', '5']:
            routine.append(choice)
        else:
            print("Invalid choice! Please select a number from the menu.")
    return routine
