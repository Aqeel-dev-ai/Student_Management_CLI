# Student Management System

A simple Python-based CLI application for managing student records. This system allows you to:
- Add new student records.
- Update existing student records.
- Delete student records.
- Search students by any field or specific field.
- Display students, either all or specific columns.
- Manage student data stored in **CSV** or **JSON** format.

## Features

- **Add Students**: Add new student records with fields such as ID, name, age, grade, etc.
- **Update Students**: Update existing student records by student ID.
- **Delete Students**: Delete student records by student ID.
- **Search Students**: Search students based on any provided criteria.
- **Display Students**: Display all students or specific columns (e.g., ID, Name, Age, Grade).
- **Manage Columns**: Add or remove columns in CSV and JSON files.
- **Change Data File**: Change the file path to switch between different CSV or JSON files.
  
## Supported File Formats

- **CSV Format**: Stores records in a CSV file with columns such as `id`, `name`, `age`, `grade`, etc.
- **JSON Format**: Stores records as a list of JSON objects with the same field names as the CSV format.

## Installation

### Requirements:
- Python 3.x
- `tabulate` module (for displaying student records in a table format)

To install the necessary dependencies, run:

```bash
pip install tabulate
````

## Usage

### Running the Application

1. Clone the repository to your local machine.

```bash
git clone https://github.com/YourUsername/Student_Management_System.git
```

2. Navigate to the project directory.

```bash
cd Student_Management_System
```

3. Run the Python script:

```bash
python student_management.py
```

4. The system will prompt you to set the file path (CSV or JSON) for student data.
5. You can choose various operations from the menu (e.g., add, update, delete, search students).

### Available Operations:

1. **Add Student**: Adds a new student to the system by entering the required details.
2. **View All Students**: Displays all student records.
3. **View Specific Columns**: Displays specific columns (e.g., `name`, `grade`, etc.).
4. **Update Student**: Update the student information by providing the student ID.
5. **Delete Student**: Deletes a student record by providing the student ID.
6. **Add Column**: Adds a new column to the CSV/JSON file for all students.
7. **Remove Column**: Removes an existing column from the CSV/JSON file.
8. **Change File**: Change the file path (CSV or JSON) to a different file.
9. **Search Students**: Search students based on multiple criteria (e.g., age, grade).
10. **Exit**: Exit the system.

## Example Data (CSV Format):

The CSV file stores student records with the following columns:

```
id, name, age, grade
1, John Doe, 20, A
2, Jane Doe, 22, B
```

## Example Data (JSON Format):

The JSON file stores student records in the following format:

```json
[
  {
    "id": "1",
    "name": "John Doe",
    "age": "20",
    "grade": "A"
  },
  {
    "id": "2",
    "name": "Jane Doe",
    "age": "22",
    "grade": "B"
  }
]
```

## How to Search Students:

The system allows you to search students based on any field (e.g., `name`, `age`, `grade`). You can enter search criteria such as:

```json
{
  "name": "John"
}
```

This will return all students whose name matches the search term.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a description of your changes.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.


### **Explanation of the README Sections**:
- **Title**: The title of the project is mentioned at the top.
- **Features**: This section lists all the features of the application, such as adding students, updating records, and managing columns.
- **Supported File Formats**: Mentions the file formats (CSV and JSON) supported by the system for storing student data.
- **Installation**: Describes the prerequisites for running the program and how to install the required dependencies (`tabulate`).
- **Usage**: Walks through the steps to run the program, including setting the file path and available operations that users can perform.
- **Example Data**: Provides sample data in both CSV and JSON formats for understanding the structure of the data.
- **Search Students**: Explains how the user can search for students based on different fields.
- **Contributing**: Gives instructions for people who want to contribute to the project.
- **License**: States the license under which the project is distributed.
