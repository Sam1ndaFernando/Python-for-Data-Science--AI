# with open("my_file.txt", "w") as file:    
#     content = file.write("hello worled\n")
#     file.write("this ie our python class")
#     print(content)


# with open("my_file.txt", "w") as file: 
#    my_list=["hello wirled\n", "this ie our python class "]    # list eka widiyata eha paththta yawanna thiyana karamayak mekath 
#    file.writelines(my_list)



# with open("my_file.txt", "w") as file: 
#    my_list=["hello wirled\n", "this ie our python class \n"]    # list eka widiyata eha paththta yawanna thiyana karamayak mekath 
#    my_list.append("suddh")
#    file.writelines(my_list)


# with open("my_file.txt", "a") as file: 
#     file.write("\n we are studdent")\
    

# ==========================================================================================================================================

#     implient the simple content System

#     1. create the programme tha store and manage contacts in the file name "contacts.txt " each contact shuld name, phonr Number, email

#     impliment the fetures
#     add the new  contact
#     append the contact to the  file 
#     view all contact 
#     read and display all contacts from the file 
#     exit the programe



#     main function

# press ... given the programe user input details 

# 1 who add the contact 
# 2. to give all contact
# 3. enter exit from the pogramme


# ============================================
# ============================================


import os

file_name = 'contacts.txt'

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if not name or not phone or not email:
        print("All fields (name, phone, email) are required!")
        return
    
    with open(file_name, 'a') as file:
        file.write(f'{name},{phone},{email}\n')
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if not os.path.exists(file_name):
        print("No contacts found. Please add some contacts first.")
        return
    
    print("\n--- List of Contacts ---")
    with open(file_name, 'r') as file:
        contacts = file.readlines()
        if contacts:
            for index, contact in enumerate(contacts, start=1):
                name, phone, email = contact.strip().split(',')
                print(f"{index}. Name: {name}, Phone: {phone}, Email: {email}")
        else:
            print("No contacts available.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()

