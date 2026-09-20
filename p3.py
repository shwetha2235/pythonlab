"""
Program 3: Automated CSV File Inspector and Data Exporter

This micro-tool uses the pandas library to read CSV or
tab-separated files, inspect the structure of the dataset,
display dimensions and data types, filter rows according
to a specified condition, and export the filtered data
into a new CSV file.
"""

import pandas as pd

# Read the CSV file
filename = "students.csv"

try:
    data = pd.read_csv(filename)

    # Display the complete dataset
    print("\n========== DATASET ==========")
    print(data)

    # Display number of rows and columns
    rows, columns = data.shape

    print("\n========== DATASET INFORMATION ==========")
    print("Number of rows    :", rows)
    print("Number of columns :", columns)

    # Display column names
    print("\nColumn Names:")
    for column in data.columns:
        print(column)

    # Display data types
    print("\n========== DATA TYPES ==========")
    print(data.dtypes)

    # Display summary statistics
    print("\n========== SUMMARY STATISTICS ==========")
    print(data.describe())

    # Check for missing values
    print("\n========== MISSING VALUES ==========")
    print(data.isnull().sum())

    # Filter rows according to condition
    # Example: students having marks greater than or equal to 60
    filtered_data = data[data["Marks"] >= 60]

    print("\n========== FILTERED DATA ==========")
    print(filtered_data)

    # Display number of filtered records
    print("\nNumber of selected records:",
          len(filtered_data))

    # Export filtered data to a new CSV file
    output_file = "filtered_students.csv"
    filtered_data.to_csv(output_file, index=False)

    print("\nFiltered data successfully exported.")
    print("Output file:", output_file)

except FileNotFoundError:
    print("Error: CSV file not found.")

except KeyError:
    print("Error: Required column 'Marks' not found.")

except Exception as error:
    print("An error occurred:", error)