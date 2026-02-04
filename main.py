from menual_contacts import create_a_contact_file, show_manu, add_contact, show_all_contacts, search_contact, delete_contact, edit_contact, sorting_by_alphabet

print("Welcome To Our Contact Book!")
create_a_contact_file()

while True:
    print(show_manu())
    choice = input("Please enter your choice: ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Please enter a valid number!")
        continue

    if choice == "1":
        name = input("Enter a contact name: ")
        number = input(f"Enter {name}'s number: ")
        while True:
            email = "No email address"
            choice = input("Do you want to add a email address [y / n]? ")
            if choice.lower() not in ["y", "n"]:
                print("Please enter 'y' or 'n'")
            else:
                if choice.lower() == "y":
                    email = input("Enter an email address: ")
                break

        print(add_contact(name, number, email))

    elif choice == "2":
        contacts = show_all_contacts()
        if type(contacts) == str:
            print(contacts)
        else:
            for na, nu in contacts.items():
                print(f"name: {na} | number: {nu[0]} | email: {nu[1]}")

    elif choice == "3":
        name = input("Enter a contact name to search: ")
        print(search_contact(name))

    elif choice == "4":
        name = input("Enter a contact name to delete: ")
        print(delete_contact(name))

    elif choice == "5":
        name = input("Enter a contact's name to edit: ")
        new_number = input("Enter a new number to edit: ")
        print(edit_contact(name, new_number))

    elif choice == "6":
        contacts = sorting_by_alphabet()
        if type(contacts) == str:
            print(contacts)
        else:
            for na, nu in contacts.items():
                print(f"name : {na} - number : {nu}")

    else:
        break

print("Thank you for using our contact book.\nGood bye")