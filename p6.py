"""
Program 6: Dynamic Phonebook and Contact Directory Manager

This micro-tool uses a dictionary-based phonebook to store,
search, update, and delete contact records dynamically.
It uses dictionary methods such as keys(), values(), and
items(), along with list comprehensions for searching and
updating contact information.
"""

# Create an empty phonebook
phonebook = {}


def add_contact():
    print("\n========== ADD CONTACT ==========")

    name = input("Enter contact name: ").strip()

    if name in phonebook:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    phonebook[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def display_contacts():
    print("\n========== ALL CONTACTS ==========")

    if not phonebook:
        print("Phonebook is empty.")
        return

    for name, details in phonebook.items():
        print("\nName :", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_contact():
    print("\n========== SEARCH CONTACT ==========")

    search = input("Enter name to search: ").lower()

    # List comprehension for dynamic lookup
    results = [
        name for name in phonebook.keys()
        if search in name.lower()
    ]

    if results:
        for name in results:
            print("\nName :", name)
            print("Phone:", phonebook[name]["phone"])
            print("Email:", phonebook[name]["email"])
    else:
        print("No matching contact found.")


def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    name = input("Enter contact name: ").strip()

    if name not in phonebook:
        print("Contact not found.")
        return

    print("\nCurrent details:")
    print("Phone:", phonebook[name]["phone"])
    print("Email:", phonebook[name]["email"])

    print("\n1. Update Phone")
    print("2. Update Email")
    print("3. Update Both")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_phone = input("Enter new phone number: ")
        phonebook[name]["phone"] = new_phone
        print("Phone number updated successfully.")

    elif choice == "2":
        new_email = input("Enter new email: ")
        phonebook[name]["email"] = new_email
        print("Email updated successfully.")

    elif choice == "3":
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")

        phonebook[name]["phone"] = new_phone
        phonebook[name]["email"] = new_email

        print("Contact details updated successfully.")

    else:
        print("Invalid choice.")


def delete_contact():
    print("\n========== DELETE CONTACT ==========")

    name = input("Enter contact name: ").strip()

    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def show_phone_numbers():
    print("\n========== PHONE NUMBERS ==========")

    if not phonebook:
        print("Phonebook is empty.")
        return

    # Using dictionary values()
    phone_numbers = [
        details["phone"]
        for details in phonebook.values()
    ]

    for phone in phone_numbers:
        print(phone)


def show_contact_names():
    print("\n========== CONTACT NAMES ==========")

    if not phonebook:
        print("Phonebook is empty.")
        return

    # Using dictionary keys()
    names = list(phonebook.keys())

    for name in names:
        print(name)


def show_contact_records():
    print("\n========== CONTACT RECORDS ==========")

    if not phonebook:
        print("Phonebook is empty.")
        return

    # Using dictionary items()
    for name, details in phonebook.items():
        print(
            name,
            "->",
            details["phone"],
            "|",
            details["email"]
        )


def main():
    print("==========================================")
    print("   DYNAMIC PHONEBOOK AND CONTACT")
    print("        DIRECTORY MANAGER")
    print("==========================================")

    while True:

        print("\n------------- MENU -------------")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Show Contact Names")
        print("7. Show Phone Numbers")
        print("8. Show Contact Records")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            show_contact_names()

        elif choice == "7":
            show_phone_numbers()

        elif choice == "8":
            show_contact_records()

        elif choice == "9":
            print("\nPhonebook closed successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()