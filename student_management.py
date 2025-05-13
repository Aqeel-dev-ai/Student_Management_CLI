import csv
import json
import os
from typing import List, Dict
from pathlib import Path
from tabulate import tabulate  # Add this import at the top

class StudentManagementSystem:
    def __init__(self):
        self.headers = ["id", "name", "age", "grade"]  # Default columns
        self.filename = None
        self.file_type = None
        self.default_filename = "students.csv"  # Default filename

    def set_file_path(self, file_path: str = None):
        """Set and validate the file path"""
        if not file_path:
            # Use default file path if none provided
            file_path = self.default_filename
            
        path = Path(file_path)
        
        # Convert relative path to absolute if needed
        if not path.is_absolute():
            path = Path.cwd() / path
            
        # Validate file extension
        if path.suffix.lower() not in ['.csv', '.json']:
            raise ValueError("File must be either CSV or JSON format")
            
        self.filename = str(path)
        self.file_type = path.suffix.lower()
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        if not os.path.exists(self.filename):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            if self.file_type == '.csv':
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(self.headers)
            else:  # JSON
                with open(self.filename, 'w') as file:
                    json.dump([], file)

    def validate_student_data(self, student_data: Dict) -> bool:
        """Validate student data"""
        if not all(key in student_data for key in self.headers):
            raise ValueError(f"All fields {self.headers} are required")
            
        # Validate ID (must be non-empty string)
        if not student_data['id'] or not isinstance(student_data['id'], str):
            raise ValueError("ID must be a non-empty string")
            
        # Validate name (must be non-empty string)
        if not student_data['name'] or not isinstance(student_data['name'], str):
            raise ValueError("Name must be a non-empty string")
            
        # Validate age (must be integer between 5 and 100)
        try:
            age = int(student_data['age'])
            if not 5 <= age <= 100:
                raise ValueError("Age must be between 5 and 100")
        except ValueError:
            raise ValueError("Age must be a valid number")
            
        # Validate grade (must be A, B, C, D, or F)
        if student_data['grade'] not in ['A', 'B', 'C', 'D', 'F']:
            raise ValueError("Grade must be one of: A, B, C, D, F")
            
        return True

    def add_student(self, student_data: Dict):
        if not self.filename:
            raise ValueError("File path not set. Call set_file_path() first")
            
        self.validate_student_data(student_data)
        
        if self.file_type == '.csv':
            with open(self.filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writerow(student_data)
        else:  # JSON
            students = self.read_json_file()
            students.append(student_data)
            self.write_json_file(students)
        print("Student added successfully!")

    def read_json_file(self) -> List[Dict]:
        if os.path.getsize(self.filename) == 0:
            return []
        with open(self.filename, 'r') as file:
            return json.load(file)

    def write_json_file(self, data: List[Dict]):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)

    def view_all_students(self):
        if not self.filename:
            raise ValueError("File path not set. Call set_file_path() first")
            
        if self.file_type == '.csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
        else:  # JSON
            students = self.read_json_file()
            
        if not students:
            print("No students found!")
            return
            
        # Convert list of dictionaries to list of lists for tabulate
        headers = self.headers
        table_data = [[student[h] for h in headers] for student in students]
        
        # Print table using tabulate
        print("\nStudent Records:")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_specific_columns(self, columns: List[str]):
        if self.file_type == '.csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
        else:  # JSON
            students = self.read_json_file()
            
        if not students:
            print("No students found!")
            return
            
        # Filter and prepare data for tabulate
        table_data = []
        for student in students:
            row = [student[col] for col in columns if col in student]
            table_data.append(row)
            
        # Print table using tabulate
        print("\nSelected Student Records:")
        print(tabulate(table_data, headers=columns, tablefmt='grid'))

    def update_student(self, student_id: str, updated_data: Dict):
        students = []
        updated = False
        
        if self.file_type == '.csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for student in reader:
                    if student['id'] == student_id:
                        student.update(updated_data)
                        updated = True
                    students.append(student)

            if updated:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=self.headers)
                    writer.writeheader()
                    writer.writerows(students)
        else:  # JSON
            students = self.read_json_file()
            for student in students:
                if student['id'] == student_id:
                    student.update(updated_data)
                    updated = True
            if updated:
                self.write_json_file(students)
                
        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    def delete_student(self, student_id: str):
        students = []
        deleted = False
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for student in reader:
                if student['id'] != student_id:
                    students.append(student)
                else:
                    deleted = True

        if deleted:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(students)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def add_column(self, column_name: str):
        # Convert column name to lowercase for consistency
        column_name = column_name.lower()
        
        if column_name in [h.lower() for h in self.headers]:
            print("Column already exists!")
            return

        students = []
        if self.file_type == '.csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for student in reader:
                    student[column_name] = ""  # Add new column with empty value
                    students.append(student)

            self.headers.append(column_name)
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(students)
        else:  # JSON
            students = self.read_json_file()
            for student in students:
                student[column_name] = ""
            self.headers.append(column_name)
            self.write_json_file(students)
            
        print(f"Column '{column_name}' added successfully!")

    def remove_column(self, column_name: str):
        if column_name not in self.headers:
            print("Column does not exist!")
            return
        if column_name == 'id':
            print("Cannot remove ID column!")
            return

        students = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for student in reader:
                del student[column_name]
                students.append(student)

        self.headers.remove(column_name)
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(students)
        print(f"Column '{column_name}' removed successfully!")

    def search_students(self, search_criteria: Dict[str, str]):
        """
        Search for students based on provided criteria
        Args:
            search_criteria: Dictionary with field names as keys and search terms as values
        """
        if not self.filename:
            raise ValueError("File path not set. Call set_file_path() first")
            
        if self.file_type == '.csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
        else:  # JSON
            students = self.read_json_file()
            
        if not students:
            print("No students found!")
            return
            
        # Filter students based on search criteria
        filtered_students = []
        for student in students:
            matches_all = True
            for field, value in search_criteria.items():
                if field not in student:
                    print(f"Warning: Field '{field}' not found in student records")
                    matches_all = False
                    break
                if value.lower() not in str(student[field]).lower():
                    matches_all = False
                    break
            if matches_all:
                filtered_students.append(student)
                
        if not filtered_students:
            print("No matching students found!")
            return
            
        # Display results using tabulate
        headers = self.headers
        table_data = [[student[h] for h in headers] for student in filtered_students]
        print("\nSearch Results:")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

def main():
    sms = StudentManagementSystem()
    
    # Get file path from user
    while True:
        file_path = input("Enter the file path (CSV or JSON) or press Enter for default: ").strip()
        try:
            sms.set_file_path(file_path if file_path else None)
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Specific Columns")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Column")
        print("7. Remove Column")
        print("8. Change File")
        print("9. Search Students")  # New option
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        try:
            if choice == '1':
                student_data = {}
                for header in sms.headers:
                    value = input(f"Enter student {header}: ")
                    student_data[header] = value
                sms.add_student(student_data)

            elif choice == '2':
                sms.view_all_students()

            elif choice == '3':
                print("Available columns:", sms.headers)
                columns = input("Enter column names (comma-separated): ").split(',')
                columns = [col.strip() for col in columns]
                sms.view_specific_columns(columns)

            elif choice == '4':
                student_id = input("Enter student ID to update: ")
                update_data = {}
                for header in sms.headers:
                    value = input(f"Enter new {header} (press enter to skip): ")
                    if value:
                        update_data[header] = value
                sms.update_student(student_id, update_data)

            elif choice == '5':
                student_id = input("Enter student ID to delete: ")
                sms.delete_student(student_id)

            elif choice == '6':
                column_name = input("Enter new column name: ")
                sms.add_column(column_name)

            elif choice == '7':
                print("Available columns:", sms.headers)
                column_name = input("Enter column name to remove: ")
                sms.remove_column(column_name)

            elif choice == '8':
                file_path = input("Enter new file path (CSV or JSON): ")
                sms.set_file_path(file_path)
                print("File changed successfully!")

            elif choice == '9':
                search_data = {}
                print("\nEnter search criteria (press Enter to skip a field):")
                for header in sms.headers:
                    value = input(f"Search by {header}: ")
                    if value:
                        search_data[header] = value
                if search_data:
                    sms.search_students(search_data)
                else:
                    print("No search criteria provided!")

            elif choice == '10':
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()