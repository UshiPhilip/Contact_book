from menual_contacts import create_a_contact_file, show_manu, add_contact, show_all_contacts, search_contact, delete_contact, edit_contact

print("Welcome To Our Contact Book!")
create_a_contact_file()

while True:
    print(show_manu())
    choice = input("Please enter your choice: ")

    if choice not in ["1","2","3","4","5","6"]:
        print("Please enter a valid number!")
        continue

    if choice == "1":
        name = input("Enter a contact name: ")
        number = input(f"Enter {name}'s number: ")
        print(add_contact(name, number))

    elif choice == "2":
        contacts = show_all_contacts()
        for na, nu in contacts.items():
            print(f"name : {na} - number : {na}")

    elif choice == "3":
        name = input("Enter a contact name to search: ")
        print(search_contact(name))

    elif choice == "4":
        name = input("Enter a contact name to delete: ")
        print(delete_contact(name))

    elif choice == "5":
        old_name = input("Enter a contact name to edit: ")
        new_name = input("Enter a new name to edit: ")
        new_number = input("Enter a new number to edit: ")
        print(edit_contact(old_name, new_name, new_number))

    else:
        break

print("Thank you for using our contact book.\nGood bye")