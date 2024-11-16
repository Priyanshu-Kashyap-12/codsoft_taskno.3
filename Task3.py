# Contact Book

# Introduction:
# This program simulates a simple contact book. Users can add, view, search, update, and delete contacts.
# It uses a list to store contact information, and each contact is a dictionary.

contacts = []

while True:
    # Displaying menu options
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        # Adding Contacts:
        # Highlight how users can add new contacts with all required details (name, phone, email, address).
        name = input("Enter Name of the Person: ")
        phone_no = input("Enter the phone number: ")
        email = input("Enter email address: ")
        address = input("Enter the address: ")
        contacts.append({"Name": name, "Phone": phone_no, "Email": email, "Address": address})
        print("Contact added successfully!")
        
    elif choice == "2":
        # Viewing Contact List:
        # Demonstrate how the program displays all saved contacts with names and phone numbers.
        if contacts:
            print("\nContact List:")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['Name']} - {contact['Phone']}")
        else:
            print("No contacts available.")
                
    elif choice == "3":
        # Searching Contacts:
        # Explain how users can search for a contact by name or phone number.
        search1 = input("Search by Name or Phone number: ")
        found = False
        for contact in contacts:
            if contact['Name'] == search1 or contact['Phone'] == search1:
                print("\nContact Found:")
                print(f"Name: {contact['Name']}")
                print(f"Phone: {contact['Phone']}")
                print(f"Email: {contact['Email']}")
                print(f"Address: {contact['Address']}")
                found = True
                break
        if not found:
            print("Contact not found.")
            
    elif choice == "4":
        # Updating Contacts:
        # Show how users can update a contact's details or leave fields unchanged.
        update1 = input("Enter the name of the contact to update: ")
        for contact in contacts:
            if contact['Name'] == update1:
                print("\nEnter new details (leave blank to keep unchanged):")
                new_name = input("New Name: ") or contact['Name']
                new_phone = input("New Phone Number: ") or contact['Phone']
                new_email = input("New Email: ") or contact['Email']
                new_address = input("New Address: ") or contact['Address']
                contact.update({"Name": new_name, "Phone": new_phone, "Email": new_email, "Address": new_address})
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")
    
    elif choice == "5":
        # Deleting Contacts:
        # Show how users can delete a contact by providing the contact's name.
        delete1 = input("Enter the name of the contact to delete: ")
        for contact in contacts:
            if contact['Name'] == delete1:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")
                
    elif choice == "6":
        # Conclusion:
        # End the program and thank the user for using the contact book.
        print("Exiting Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
