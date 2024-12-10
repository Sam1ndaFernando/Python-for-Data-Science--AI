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

# import os

# FILE_NAME = 'contacts.txt'

# def add_contact():
#     """Add a new contact to the contacts file."""
#     name = input("Enter contact name: ").strip()
#     phone = input("Enter phone number: ").strip()
#     email = input("Enter email address: ").strip()
    
#     if not name or not phone or not email:
#         print("All fields (name, phone, email) are required!")
#         return
    
#     with open(FILE_NAME, 'a') as file:
#         file.write(f'{name},{phone},{email}\n')
#     print(f"Contact for {name} added successfully!")

# def view_contacts():
#     if not os.path.exists(FILE_NAME):
#         print("No contacts found. Please add some contacts first.")
#         return
    
#     print("\n--- List of Contacts ---")
#     with open(FILE_NAME, 'r') as file:
#         contacts = file.readlines()
        
#         if contacts:
#             for index, contact in enumerate(contacts, start=1):
#                 try:
#                     name, phone, email = contact.strip().split(',')
#                     print(f"{index}. Name: {name}, Phone: {phone}, Email: {email}")
#                 except ValueError:
#                     print(f"Error in contact format on line {index}. Skipping this entry.")
#         else:
#             print("No contacts available.")

# def main():
#     while True:
#         print("\n--- Contact Management System ---")
#         print("1. Add New Contact")
#         print("2. View All Contacts")
#         print("3. Exit")
        
#         choice = input("Enter your choice (1, 2, or 3): ").strip()
        
#         if choice == '1':
#             add_contact()
#         elif choice == '2':
#             view_contacts()
#         elif choice == '3':
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, or 3.")

# if __name__ == '__main__':
#     main()

# ================================================================

# he code you've provided is a good start for handling the tasks you've outlined. I'll guide you through each of the steps and ensure everything works as expected.

# Here’s how we can extend it to meet your requirements:

# Read the JSON file: This is already handled by read_json(file_path).
# Display all students: The function display_students(data) works for this.
# Display students who scored above 75: The function display_above_75(data) achieves this.
# Add a new student to the file: add_student(data, new_student) is there to append a new student to the list.
# Save the file back to JSON: save_json(file_path, data) does this by saving the modified data.


# import json

# def read_json(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# def display_students(data):
#     print("All Students:")
#     for student in data:
#         print(student)

# def display_above_75(data):
#     print("\nStudents who scored above 75:")
#     for student in data:
#         if student['score'] > 75:
#             print(student)

# def add_student(data, new_student):
#     data.append(new_student)

# def save_json(file_path, data):
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)

# file_path = 'students.json'

# students_data = read_json(file_path)

# display_students(students_data)

# display_above_75(students_data)

# new_student = {
#     "name": "John Doe",
#     "score": 88
# }

# add_student(students_data, new_student)

# save_json(file_path, students_data)

# print("\nUpdated Students List:")
# display_students(students_data)


# import csv

# csv_file = "Organizations-100.csv"

# with open(csv_file, "r", newline='') as file: 
#     reader = csv.reader(file)  
#     print(reader, type(reader))


# =========================================================================================================

# Task: Create a Python Program to Manage Employee Records
# The goal is to create a Python program that manages company employee records stored in a CSV file. The program should perform the following tasks:

# Read the Input File

# Use the csv.reader to read employee.csv, which contains the following fields:
# employeeId
# name
# department
# salary
# Display all employee records on the console.
# Filter the Records

# Identify employees whose salary is above 57,000.
# Write the Filtered Records to a New File

# Use csv.DictWriter to write the filtered records to a new file named high_salary_employee.csv.
# The new file should retain the same fields as the input file:
# employeeId
# name
# department
# salary



import csv

def read_employee_records(filename):
    """Reads employee records from a CSV file and displays them."""
    employees = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            print("All Employee Records:")
            for row in reader:
                print(row)  
                
                row['salary'] = float(row['salary'])  
                employees.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
    return employees


def filter_high_salary_employees(employees, salary_threshold=57000):
    """
    Filters employee records based on the salary threshold.
    :param employees: List of employee records (dictionaries)
    :param salary_threshold: Minimum salary to filter employees
    :return: Filtered list of employee records
    """
    try:
        filtered_employees = [employee for employee in employees if employee['salary'] > salary_threshold]
    except Exception as e:
        print(f"Error filtering employees: {e}")
        filtered_employees = []
    return filtered_employees


def write_employee_records(filename, employees):
    """Writes employee records to a new CSV file."""
    if not employees:
        print(f"No records to write to '{filename}'")
        return
    
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['employeeId', 'name', 'department', 'salary']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()  
            for employee in employees:
                writer.writerow(employee)  
        print(f"Filtered records successfully written to '{filename}'")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")


if __name__ == "__main__":
    input_filename = 'employee.csv'
    
    output_filename = 'high_salary_employee.csv'
    
    employees = read_employee_records(input_filename)
    
    if employees:
        print(f"\nSuccessfully read {len(employees)} employee records.\n")
        
        filtered_employees = filter_high_salary_employees(employees, salary_threshold=57000)
        
        print(f"\n{len(filtered_employees)} records matched the filter condition (salary > 57,000).\n")
        
        write_employee_records(output_filename, filtered_employees)
