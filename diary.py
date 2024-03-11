import sys

# Program would ask for a contact's number and their name
# These names would be stored within a list and would be sorted

# Program can start by asking one of two questions
# New contact OR View All Contacts

all_contacts = []
is_active = True

all = "all"
new = "new"
close = "close"

def add_contact():
    name = input("New contact's full name\n> ")
    while (name == ''):
        name = input("Need (contact name) to create contact\n> ")

    number = input("New contact's phone number\n> ")

    while (number == ''):
        number = input("Need (phone number) to create contact\n> ")

    contact = {
        'name': name,
        'number': number
    }
    all_contacts.append(contact)
    print(f"{name} added to diary")
    is_active = True

def show_contacts(contacts):
    if (len(contacts) == 0):
        print('No contacts found 😭')
        return

    for contact in contacts:
        print(f"{contact['name']} | {contact['number']}\n")
    is_active = True


def end_program():
    is_active = False

while (is_active):
    user_choice = input("Type (ALL)📱 to Show Contacts or (NEW)⨁ to create a new contact or (CLOSE)🔚 to close the program\n> ")

    if (user_choice.lower() == all):
        show_contacts(all_contacts)
    if (user_choice.lower() == new):
        add_contact()
    if (user_choice.lower() == close):
        print('Thanks for using AuDairies 👋🏼🌚')
        sys.exit()
