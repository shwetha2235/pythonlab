"""This program builds a library of higher-order matrix transformation functions designed to manipulate 2D lists
(nested lists) and tuples. By incorporating functional components like lambda expressions along with built-in
functions such as map(), filter(), and sorted(), the script filters out negative matrix noise, sorts entries
using custom keys, and returns modified computational data sequences."""

# Function to remove negative values from a matrix
def filter_matrix(matrix):
    result = []
    for row in matrix:
        filtered_row = list(filter(lambda x: x >= 0, row))
        result.append(filtered_row)
    return result


# Function to transform matrix elements
def transform_matrix(matrix):
    result = []
    for row in matrix:
        transformed_row = list(map(lambda x: x * 2, row))
        result.append(transformed_row)
    return result


# Function to sort matrix elements
def sort_matrix(matrix):
    elements = [x for row in matrix for x in row]
    return sorted(elements, key=lambda x: abs(x))


# Function to convert matrix rows into tuples
def matrix_to_tuples(matrix):
    return list(map(tuple, matrix))


# Main program
matrix = [
    [4, -2, 7],
    [3, -5, 1],
    [-8, 6, 2]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Filter negative values
filtered = filter_matrix(matrix)
print("\nMatrix After Removing Negative Values:")
for row in filtered:
    print(row)

# Transform elements by multiplying by 2
transformed = transform_matrix(filtered)
print("\nTransformed Matrix (Elements * 2):")
for row in transformed:
    print(row)

# Sort elements by absolute value
sorted_data = sort_matrix(transformed)
print("\nSorted Elements by Absolute Value:")
print(sorted_data)

# Convert matrix rows into tuples
tuple_data = matrix_to_tuples(filtered)
print("\nMatrix Rows as Tuples:")
for row in tuple_data:
    print(row)
