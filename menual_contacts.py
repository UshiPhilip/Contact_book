from pathlib import Path
import json
import datetime

def create_a_contact_file():
    if not Path("contacts.json").exists():
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump({ }, f, indent="\t")

def get_contacts():
    with Path("contacts.json").open() as f:
        return json.load(f)

def show_manu():
    return """
    1. Add contact
    2. Show all contacts
    3. Search contact
    4. Delete contact
    5. Edit contact
    6. Sorting contacts book by alphabet
    7. Create backup
    8. Exit
"""

def add_contact(name, number, email):
    contacts = get_contacts()
    for n in contacts.keys():
        if n == name:
            return f"{name} is already exist."
    contacts[name] = [number, email]

    with Path("contacts.json").open("w") as f:
        json.dump(contacts, f, indent="\t")
    return f"{name} added successfully."

def show_all_contacts():
    contacts = get_contacts()
    return contacts if contacts else "The contacts book is empty..."

def search_contact(name):
    contacts = get_contacts()
    try:
        return f"{name}'s phone number is: {contacts[name]}"
    except:
        return f"I can't find {name}'s number..."

def delete_contact(name):
    contacts = get_contacts()
    try:
        del contacts[name]
        with Path("contacts.json").open("w") as f:
            json.dump(contacts, f, indent="\t")
            return f"{name} was deleted successfully."
    except KeyError:
        return f"{name} not exist."
    except:
        return "delete contact failed..."

def edit_contact(name, number):
    contacts = get_contacts()
    if name not in contacts.keys():
        return f"I can't find {name} in the contacts book"
    try:
        contacts[name] = number
        with Path("contacts.json").open("w") as f:
            json.dump(contacts, f, indent="\t")
            return f"{name}'s new number is {number}"
    except:
        return f"Edit {name}'s number failed..."

def sorting_by_alphabet():
    contacts = get_contacts()
    contacts = sorted(contacts.items())
    contacts = dict(contacts)
    return contacts if contacts else "The contacts book is empty..."

def create_backup():
    if not Path("contacts.json").exists():
        return "The contacts book doesn't exist."
    contacts = get_contacts()
    time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
    backup = str(time)+".txt"
    with open(Path(backup), "w", encoding="utf-8") as f:
        for line in contacts.items():
            f.write(str(line))
            f.write("\n")
    return f"Backup file created as '{time}.txt' file."
