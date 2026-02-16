# Address Book System
# Ibrahim AlMalihi 
# ibrahimalmalihi@gmail.com



def show_menu():
    print("Welcome to our Address book, please to find what you want")
    print("1. Add new contact.")
    print("2. Search by name.")
    print("3. Search by number.")
    print("4. Delete contact by name.")
    print("5. Delete contact by number.")
    print("6. Show all contacts.")
    print("7. Exit")
    print("Please to enter your choice:")


def user_input(message, numeric=False):
    while True:
        user_value = input(message).strip()
        
        if not user_value:
            print("Error: The field cannot be left blank!")
            continue 
         
        if numeric:
            if user_value.isdigit():
                return user_value
            else:
                print("Error: Please enter numbers only!")
        else:
            return user_value
        


def main():
    contacts = []

    while True:
        show_menu()
        choice = user_input("-->> ", numeric=True)

        if choice == '1':
            name = user_input("Enter contact name: ",numeric=False)
            contact_type = user_input("Enter type (Family, Personal, Work, Other): ",numeric=False).capitalize()
            valid_types = ["Family", "Personal", "Work", "Other"]
            
            if contact_type not in valid_types:
                print("Note: Invalid type. System will consider it as 'Other'.")
                contact_type = "Other"

            number = user_input("Enter phone number: ",numeric=True)
            
            is_reserved = False
            for c in contacts:
                if number in c['numbers']:
                    is_reserved = True
                    break
            
            if is_reserved:
                print("Error: This number is already reserved. Process rejected.")
            else:
                found_existing = False
                for c in contacts:
                    if c['name'].lower() == name.lower():
                        c['numbers'].append(number)
                        found_existing = True
                        break
                
                if not found_existing:
                    contacts.append({'name': name, 'type': contact_type, 'numbers': [number]})
                
                print("Process success: Contact stored.")

        elif choice == '2':
            search_name = user_input("Enter contact's name to find: ", numeric=False).lower()
            
            exact_matches = [c for c in contacts if search_name in c['name'].lower()]
            
            similar_matches = []
            for c in contacts:
                name_in_list = c['name'].lower()
                if c in exact_matches:
                    continue
                
                if len(search_name) == len(name_in_list):
                    differences = 0
                    for i in range(len(search_name)):
                        if search_name[i] != name_in_list[i]:
                            differences += 1
                    if differences == 1:
                        similar_matches.append(c)

            if not exact_matches and not similar_matches:
                print("Not found")
            else:
                if exact_matches:
                    print("--- Related Contacts ---")
                    for c in exact_matches:
                        print(f"Name: {c['name']}, Type: {c['type']}, Numbers: {', '.join(c['numbers'])}")
                
                if similar_matches:
                    print("--- Similar Names (Suggested) ---")
                    for c in similar_matches:
                        print(f"Name: {c['name']}, Type: {c['type']}, Numbers: {', '.join(c['numbers'])}")
                
                print("Process success: Search completed.")

        elif choice == '3':
            search_num = user_input("Enter contact's number to find: ",numeric=True)
            found = False
            for c in contacts:
                if search_num in c['numbers']:
                    print(f"Found: Name: {c['name']}, Type: {c['type']}, Number: {search_num}")
                    found = True
                    break
            if not found:
                print("Not found")

        elif choice == '4':
            del_name = user_input("Enter contact's name to delete: ",numeric=False)
            original_len = len(contacts)
            contacts = [c for c in contacts if c['name'].lower() != del_name.lower()]
            deleted_count = original_len - len(contacts)
            if deleted_count > 0:
                print(f"Process success: {deleted_count} record(s) deleted.")
            else:
                print("Not found")

        elif choice == '5':
            del_num = user_input("Enter contact's number to delete: ",numeric=True)
            target_contact = None
            for c in contacts:
                if del_num in c['numbers']:
                    target_contact = c
                    break
            if target_contact:
                target_contact['numbers'].remove(del_num)
                if not target_contact['numbers']:
                    contacts.remove(target_contact)
                print("Process success: Number deleted.")
            else:
                print("Not found")

        elif choice == '6':
            if not contacts:
                print("The address book is empty.")
            else:
                for c in contacts:
                    for num in c['numbers']:
                        print(f"({c['name']}, {c['type']}, {num})")

        elif choice == '7':
            print("Exit system")
            break
        else:
            print("Error: Invalid choice. Please try again.")


main()