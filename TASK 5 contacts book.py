contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    search = input("Search by Name or Phone Number: ")
    for name, details in contacts.items():
        if search == name or search == details["Phone"]:
            print(f"Found: {name} - {details}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave blank if you don't want to update a field.")
        phone = input("New Phone Number: ")
        email = input("New Email: ")
        address = input("New Address: ")
        if phone: contacts[name]["Phone"] = phone
        if email: contacts[name]["Email"] = email
        if address: contacts[name]["Address"] = address
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ")
        if confirm.lower() == 'yes':
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Contact not found.")

def main_menu():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book
main_menu()
