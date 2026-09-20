"""
Program 2: Automated Word Frequency and
Pattern Analyzer

This micro-tool takes multiline text input and analyzes
the text to calculate total word count, word frequency,
and palindrome words. It removes punctuation, converts
text to lowercase, and uses string methods to generate
a simple text analysis report.
"""

import string

# Read multiline text
text = """Python is easy.
Python is powerful.
Madam is a palindrome.
Level is another palindrome."""

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Convert text into individual words
words = text.split()

# Count total words
total_words = len(words)

# Create frequency table
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Find palindromes
palindromes = []

for word in words:
    if len(word) > 1 and word == word[::-1]:
        if word not in palindromes:
            palindromes.append(word)

# Display the report
print("\n========== TEXT ANALYSIS REPORT ==========")

print("\nTotal words:", total_words)

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])

print("\nPalindrome Words:")

if len(palindromes) > 0:
    for word in palindromes:
        print(word)
else:
    print("No palindrome words found.")