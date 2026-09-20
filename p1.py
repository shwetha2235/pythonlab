"""
Program 1: Dynamic Command-Line Caesar Cipher Tool

This micro-tool takes text input along with a user-specified shift
key via the command line or prompt to encode or decode messages using
the Caesar cipher encryption technique. It processes raw input strings
by shifting alphabetic characters while ignoring special symbols,
verifying valid data types using string methods, and dynamically
handling standard system parameters.
"""

import sys


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26
                              + ord('A'))

            else:
                result += chr((ord(char) - ord('a') + shift) % 26
                              + ord('a'))

        else:
            result += char

    return result


def main():
    print("===== Caesar Cipher Tool =====")

    # Get text from command line or user input
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input("Enter the message: ")

    # Check whether message is empty
    if text.strip() == "":
        print("Error: Message cannot be empty.")
        return

    # Get shift key
    if len(sys.argv) > 2:
        shift_input = sys.argv[2]
    else:
        shift_input = input("Enter shift key: ")

    # Validate shift key
    if not shift_input.lstrip("-").isdigit():
        print("Error: Shift key must be an integer.")
        return

    shift = int(shift_input)

    # Display operation choices
    print("\nSelect the operation:")
    print("1. Encode")
    print("2. Decode")

    choice = input("Enter your choice: ")

    # Validate operation choice
    if not choice.isdigit():
        print("Error: Choice must be a number.")
        return

    choice = int(choice)

    # Encode the message
    if choice == 1:
        result = caesar_cipher(text, shift)

        print("\nOriginal message:", text)
        print("Shift key:", shift)
        print("Encoded message:", result)

    # Decode the message
    elif choice == 2:
        result = caesar_cipher(text, -shift)

        print("\nEncoded message:", text)
        print("Shift key:", shift)
        print("Decoded message:", result)

    # Handle invalid choice
    else:
        print("Error: Invalid choice.")
        print("Please select 1 or 2.")
        return

    # Display final information
    print("\nSpecial characters are not changed.")
    print("Spaces are preserved.")
    print("Operation completed successfully.")


if __name__ == "__main__":
    main()