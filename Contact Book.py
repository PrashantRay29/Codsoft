class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone} - {contact.email} - {contact.address}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found!")
        else:
            for i, contact in enumerate(found_contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}- {contact.email} - {contact.address}")

    def update_contact(self):
        search_term = input("Enter name or phone number to update: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found!")
        else:
            contact = found_contacts[0]
            print(f"Updating contact: {contact.name} - {contact.phone}")
            contact.name = input("Enter new name: ") or contact.name
            contact.phone = input("Enter new phone number: ") or contact.phone
            contact.email = input("Enter new email: ") or contact.email
            contact.address = input("Enter new address: ") or contact.address
            print("Contact updated successfully!")

    def delete_contact(self):
        search_term = input("Enter name or phone number to delete: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found!")
        else:
            contact = found_contacts[0]
            self.contacts.remove(contact)
            print(f"Contact {contact.name} - {contact.phone} deleted successfully!")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Information Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
