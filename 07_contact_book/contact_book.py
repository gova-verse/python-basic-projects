# contact_book.py
# Concepts: OOP, classes, objects, methods, __init__, list of objects

class Contact:
    def __init__(self, name, phone, email):
        # __init__ is the constructor — runs automatically when object is created
        self.name  = name
        self.phone = phone
        self.email = email

    def display(self):
        # method to print contact details neatly
        print(f"\n  Name  : {self.name}")
        print(f"  Phone : {self.phone}")
        print(f"  Email : {self.email}")

    def update(self, phone=None, email=None):
        # only update fields that are provided
        if phone:
            self.phone = phone
        if email:
            self.email = email
        print(f"Contact '{self.name}' updated successfully!")


class ContactBook:
    def __init__(self):
        # list to store all Contact objects
        self.contacts = []

    def add_contact(self, name, phone, email):
        # check if contact already exists
        if self.find_contact(name):
            print(f"Contact '{name}' already exists!")
            return
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def find_contact(self, name):
        # search contacts by name (case insensitive)
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def view_all(self):
        if len(self.contacts) == 0:
            print("\nNo contacts found!")
            return
        print("\n--- All Contacts ---")
        print(f"  {'NO.':<5} {'NAME':<20} {'PHONE':<15} {'EMAIL'}")
        print("  " + "-" * 55)
        for i, contact in enumerate(self.contacts, start=1):
            print(f"  {i:<5} {contact.name:<20} {contact.phone:<15} {contact.email}")

    def search_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            print("\n--- Contact Found ---")
            contact.display()
        else:
            print(f"Contact '{name}' not found!")

    def update_contact(self, name):
        contact = self.find_contact(name)
        if not contact:
            print(f"Contact '{name}' not found!")
            return
        print(f"\nUpdating '{name}' — press Enter to keep current value")
        new_phone = input(f"  New phone (current: {contact.phone}): ").strip()
        new_email = input(f"  New email (current: {contact.email}): ").strip()
        contact.update(
            phone=new_phone if new_phone else None,
            email=new_email if new_email else None
        )

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def total_contacts(self):
        return len(self.contacts)


def show_menu():
    print("\n" + "=" * 40)
    print("          Contact Book")
    print("=" * 40)
    print("  1. Add contact")
    print("  2. View all contacts")
    print("  3. Search contact")
    print("  4. Update contact")
    print("  5. Delete contact")
    print("  6. Exit")
    print("=" * 40)
    print(f"  Total contacts stored: {book.total_contacts()}")


def get_input(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  This field cannot be empty!")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Add New Contact ---")
            name  = get_input("  Name  : ").title()
            phone = get_input("  Phone : ")
            email = get_input("  Email : ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_all()

        elif choice == "3":
            name = input("\nEnter name to search: ").strip()
            book.search_contact(name)

        elif choice == "4":
            name = input("\nEnter name to update: ").strip()
            book.update_contact(name)

        elif choice == "5":
            name = input("\nEnter name to delete: ").strip()
            book.delete_contact(name)

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice! Enter 1 to 6.")


# create a single global ContactBook object
book = ContactBook()

if __name__ == "__main__":
    main()