# SmartTask Manager

#### Video Demo: https://youtu.be/tmBBf8zwlwg?si=NChwisyfkpl6j5vG

#### Description:

SmartTask Manager is a command-line based task management application developed in Python. The purpose of this project is to help users organize their daily tasks efficiently by allowing them to create, manage, and track tasks with deadlines. This project was designed as a final submission for a Python programming course and demonstrates the practical application of programming concepts such as control structures, object-oriented programming (OOP), file handling, and error handling.

The application allows users to add tasks with specific deadlines, view all existing tasks, mark tasks as completed, delete tasks, and check for overdue tasks. In addition, the program supports saving tasks to a file and loading them back when the program is restarted, ensuring that user data is not lost between sessions. This makes the application more realistic and useful compared to basic lab assignments.

The core functionality of the program revolves around a Task class, which represents each individual task. This class includes attributes such as the task title, deadline, and completion status. It also includes a method to mark a task as completed. The use of object-oriented programming allows the program to be well-structured, reusable, and easier to maintain. Instead of using simple lists or dictionaries alone, encapsulating task-related data and behavior within a class improves code readability and organization.

The main file in this project is TermProject.py, which contains the main function and all supporting functions required to run the application. The main() function acts as the entry point of the program and controls the overall flow by displaying a menu and handling user input. Additional functions such as add_task(), view_tasks(), mark_complete(), delete_task(), save_tasks(), load_tasks(), and check_overdue() are defined at the same level as the main function, as required by the project guidelines. These functions are responsible for specific features of the application and help break down the logic into manageable parts.

File handling is implemented using JSON format to store tasks in a file named tasks.json. JSON was chosen instead of plain text because it allows structured storage of data, making it easier to save and reload objects. When saving tasks, each task is converted into a dictionary and written to the file. When loading tasks, the program reads the file and reconstructs Task objects from the stored data. This demonstrates an understanding of both serialization and deserialization.

Error handling is an important part of this project. The program uses try and except blocks to handle invalid inputs, such as incorrect date formats or non-numeric menu selections. This ensures that the program does not crash unexpectedly and provides user-friendly error messages instead. For example, when entering a deadline, the program validates the format using the datetime module. If the format is incorrect, the user is prompted to try again.

The project also makes use of Python’s built-in libraries such as datetime and json. The datetime module is used to validate and compare task deadlines, especially for identifying overdue tasks. The json module is used for reading and writing data to files. These libraries extend the functionality of the program and demonstrate the ability to use external modules effectively.

In terms of design decisions, a command-line interface (CLI) was chosen instead of a graphical user interface (GUI) to keep the project focused on core Python programming concepts while still delivering meaningful functionality. The menu-driven interface is simple, intuitive, and easy to demonstrate in a short video presentation. Additionally, using a global task list simplifies data sharing between functions while maintaining clarity in the program structure.

One of the challenges encountered during development was ensuring that data persisted correctly between program runs. This was solved by implementing JSON file storage and carefully handling file reading and writing operations. Another challenge was validating user input, particularly for date formats, which was addressed using the datetime.strptime() method.

Overall, SmartTask Manager is a practical and functional application that goes beyond basic programming exercises. It demonstrates a solid understanding of Python programming concepts and provides a useful tool for managing tasks effectively.
