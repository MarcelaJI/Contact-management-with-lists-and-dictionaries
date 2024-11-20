contacts = []

def add_contact(name, phone, mail):
    contacts.append({"name": name, "phone": phone, "mail": mail})

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
        return None

def del_contact(name):
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            return True
        return False

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        mail = input("Mail: ")
        add_contact(name, phone, mail)
    elif option == "2":
        name = input("Contact name to search: ")
        contact = search_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found")
    elif option == "3":
        name = input("Contact name to delete ")
        if del_contact(name):
            print("Deleted contact")
        else:
            print("Contact not found")
    elif option == "4":
        break
    else:
        print("Invalid option")

