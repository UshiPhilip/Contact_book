from pathlib import Path

def create_a_contact_file():
    if not Path("contacts.txt").exists():
        with open("contacts.txt", "w", encoding="utf-8") as f:
            f.write("Welcome To Our Contacts book!\n\n")


def show_manu():
    return """
1. Add contact
2. Show all contacts
3. Search contact
4. Delete contact
5. Edit contact
6. Exit
    """

def show_contacts():
    pass

def add_contact(name, number):
    pass

def save_contact(name, number):
    pass

def search_contact(name):
    pass

def delete_contact(name):
    pass

def edit_contact(old_name, new_name, new_number):
    pass