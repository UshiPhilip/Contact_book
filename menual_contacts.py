from pathlib import Path
import json

def create_a_contact_file():
    if not Path("contacts.json").exists():
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump({ }, f, indent="\t")


def show_manu():
    return """
1. Add contact
2. Show all contacts
3. Search contact
4. Delete contact
5. Edit contact
6. Exit
    """

def add_contact(name, number):
    with Path("contacts.json").open() as f:
        contacts = json.load(f)
    for n in contacts.keys():
        if n == name:
            return f"{name} is already exist."
    contacts[name] = number

    with Path("contacts.json").open("w") as f:
        json.dump(contacts, f, indent="\t")
    return f"{name} added successfully."

def show_contacts():
    pass

def save_contact(name, number):
    pass

def search_contact(name):
    pass

def delete_contact(name):
    pass

def edit_contact(old_name, new_name, new_number):
    pass