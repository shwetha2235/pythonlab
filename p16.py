"""This task builds a fault-tolerant file parsing pipeline that gracefully catches potential runtime errors using
explicit try-except-else-finally execution blocks. The script defines custom application-specific
exception classes to flag invalid file formatting, log tracebacks, and guarantee that open file resources are
safely cleaned up."""
import traceback

# Custom exception classes
class FileProcessorError(Exception):
    pass

class InvalidFileFormatError(FileProcessorError):
    pass

class EmptyFileError(FileProcessorError):
    pass

def process_file(filename):
    file = None

    try:
        # Open the file
        file = open(filename, "r")

        # Read file contents
        content = file.read()

        if not content.strip():
            raise EmptyFileError("The file is empty.")

        # Validate file format
        lines = content.splitlines()

        for line_number, line in enumerate(lines, start=1):
            if "," not in line:
                raise InvalidFileFormatError(
                    f"Invalid format at line {line_number}: {line}"
                )

        # Process the file
        print("File opened successfully.")
        print("File content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    except InvalidFileFormatError as e:
        print("Format Error:", e)
        print("Traceback information:")
        traceback.print_exc()

    except EmptyFileError as e:
        print("Empty File Error:", e)

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)
        traceback.print_exc()

    else:
        print("File processed successfully.")

    finally:
        if file is not None:
            file.close()
            print("File closed safely.")

        print("File processing completed.")


# Main program
filename = input("Enter filename: ")
process_file(filename)