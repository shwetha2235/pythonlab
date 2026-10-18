"""This task takes input words or textual phrases to determine whether they form valid anagram pairs across
distinct sequences. Using list sorting algorithms, dictionary counting techniques, and immutable tuple keys,
the tool cleans formatting variances to perform fast lookup matchings."""


def clean(text):
    return tuple(sorted(c.lower() for c in text if c.isalnum()))


def are_anagrams(a, b):
    return clean(a) == clean(b)


def main():
    words = input("Enter words separated by spaces: ").split()
    groups = {}

    for word in words:
        key = clean(word)
        groups.setdefault(key, []).append(word)

    print("\nAnagram Groups:")
    for key, group in groups.items():
        if len(group) > 1:
            print(group, "Key:", key)

    a = input("\nEnter first word or phrase: ")
    b = input("Enter second word or phrase: ")

    print("Anagrams" if are_anagrams(a, b)
          else "Not Anagrams")


if __name__ == "__main__":
    main()
