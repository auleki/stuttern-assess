import sys

# list that holds all contacts
all_contacts = []

is_active = True

all = "all"
new = "new"
close = "close"

# method to handle adding contact to list and validating user entries
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

# Method to show and format all contacts
def show_contacts(contacts):
    if (len(contacts) == 0):
        print('No contacts found 😭')
        return

    for contact in contacts:
        print(f"{contact['name']} | {contact['number']}\n")
    is_active = True

# Method to end program and exit script instance
def end_program():
    print('Thanks for using AuDairies 👋🏼🌚')
    sys.exit()

# Loop that controls the program flow based on what the user selects
while (is_active):
    user_choice = input("Type (ALL)📱 to Show Contacts or (NEW)⨁ to create a new contact or (CLOSE)🔚 to close the program\n> ")

    if (user_choice.lower() == all):
        show_contacts(all_contacts)
    if (user_choice.lower() == new):
        add_contact()
    if (user_choice.lower() == close):
        end_program()
