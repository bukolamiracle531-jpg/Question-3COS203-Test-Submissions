import student_module
import file_module

def main():
    while True:
        print("\n======================================")
        print("    ASSIGNMENT SUBMISSION SYSTEM     ")
        print("======================================")
        print("1. Accept and Save Student Details")
        print("2. Display All Submitted Records")
        print("3. Search Submission by Matric Number")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Input Student Details ---")
            name = input("Enter Student Name: ").strip()
            matric = input("Enter Matric Number: ").strip()
            course = input("Enter Course Code: ").strip()
            
            # Instantiating the object from the class structure
            new_student = student_module.Student(name, matric, course)
            file_module.save_record(new_student)
            print("Assignment submission record saved successfully!")
            
        elif choice == "2":
            print("\n--- All Assignment Submissions ---")
            records = file_module.get_all_records()
            if not records:
                print("No submissions found in records.")
            else:
                print(f"{'Student Name':<25} | {'Matric Number':<20} | {'Course Code':<12}")
                print("-" * 63)
                for student in records:
                    print(f"{student.name:<25} | {student.matric_number:<20} | {student.course_code:<12}")
                    
        elif choice == "3":
            print("\n--- Search Record ---")
            search_matric = input("Enter target Matric Number to search: ").strip()
            match = file_module.search_by_matric(search_matric)
            
            if match:
                print("\nRecord Located!")
                print(f"Name:        {match.name}")
                print(f"Matric No:   {match.matric_number}")
                print(f"Course Code: {match.course_code}")
            else:
                print(f"\nNo assignment record found for Matric Number: '{search_matric}'.")
                
        elif choice == "4":
            print("Exiting System. System closed.")
            break
        else:
            print("Invalid choice! Enter a valid selection from 1 to 4.")

if __name__ == "__main__":
    main()
