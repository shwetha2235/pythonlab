"""
Program 5: Robust File Management and Directory Navigation Utility

This utility uses Python's built-in os and sys modules to inspect
directories, navigate through folders, create workspace folders,
list files with specific extensions, and safely read or create
text log files using context managers.
"""

import os
import sys


def show_current_directory():
    print("\n========== CURRENT DIRECTORY ==========")
    print("Current directory:", os.getcwd())

    print("\nFiles and folders:")

    items = os.listdir()

    if not items:
        print("Directory is empty.")
    else:
        for item in items:
            if os.path.isdir(item):
                print("[DIR] ", item)
            else:
                print("[FILE]", item)


def show_subdirectories():
    print("\n========== SUBDIRECTORIES ==========")

    current_directory = os.getcwd()
    items = os.listdir(current_directory)

    found = False

    for item in items:
        path = os.path.join(current_directory, item)

        if os.path.isdir(path):
            print(item)
            found = True

    if not found:
        print("No subdirectories found.")


def create_workspace():
    folder_name = input("\nEnter workspace folder name: ")

    if not folder_name.strip():
        print("Folder name cannot be empty.")
        return

    folder_path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(folder_path):
        print("Workspace folder already exists.")
    else:
        os.makedirs(folder_path)
        print("Workspace created successfully.")
        print("Location:", folder_path)


def navigate_directory():
    print("\n========== DIRECTORY NAVIGATION ==========")

    path = input("Enter directory path: ")

    if os.path.isdir(path):
        try:
            os.chdir(path)
            print("Directory changed successfully.")
            print("Current directory:", os.getcwd())

        except PermissionError:
            print("Permission denied.")

    else:
        print("Directory does not exist.")


def list_extension_files():
    print("\n========== FILE EXTENSION SEARCH ==========")

    extension = input(
        "Enter extension to search for (example: .txt): "
    ).lower()

    if not extension.startswith("."):
        extension = "." + extension

    current_directory = os.getcwd()
    found = False

    for item in os.listdir(current_directory):

        if os.path.isfile(item):
            if item.lower().endswith(extension):
                print(item)
                found = True

    if not found:
        print("No files found with extension", extension)


def create_or_read_log():
    print("\n========== TEXT LOG MANAGEMENT ==========")

    filename = input("Enter log file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        if os.path.exists(filename):

            with open(filename, "r") as file:
                content = file.read()

            print("\nExisting log content:")
            print(content)

        else:

            message = input("Enter log message: ")

            with open(filename, "w") as file:
                file.write(message)

            print("Log file created successfully.")

    except PermissionError:
        print("Permission denied.")

    except OSError as error:
        print("File error:", error)


def process_command_line():
    print("\n========== COMMAND-LINE ARGUMENTS ==========")

    if len(sys.argv) > 1:

        print("Arguments provided:")

        for argument in sys.argv:
            print(argument)

    else:
        print("No command-line arguments provided.")


def main():

    print("==========================================")
    print(" ROBUST FILE MANAGEMENT AND DIRECTORY")
    print("          NAVIGATION UTILITY")
    print("==========================================")

    process_command_line()

    while True:

        print("\n------------- MENU -------------")
        print("1. Show Current Directory")
        print("2. Show Subdirectories")
        print("3. Create Workspace Folder")
        print("4. Navigate to Directory")
        print("5. List Files by Extension")
        print("6. Create or Read Text Log")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_current_directory()

        elif choice == "2":
            show_subdirectories()

        elif choice == "3":
            create_workspace()

        elif choice == "4":
            navigate_directory()

        elif choice == "5":
            list_extension_files()

        elif choice == "6":
            create_or_read_log()

        elif choice == "7":
            print("\nProgram terminated successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()