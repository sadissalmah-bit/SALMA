# Task 1: Convert all uppercase letters to lowercase
def to_lowercase(s):
    return s.lower()

# Task 2: Swap uppercase and lowercase letters
def swap_case(s):
    return s.swapcase()

# Task 3: Remove all uppercase letters
def remove_uppercase(s):
    return ''.join(char for char in s if not char.isupper())

# Task 4: Count uppercase and lowercase letters
def count_case(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    return f"Uppercase: {uppercase_count}, Lowercase: {lowercase_count}"

# Task 5: Remove all non-English letters
def remove_non_letters(s):
    return ''.join(char for char in s if char.isalpha())

# Task 6: Compute triangle area using Heron's formula
def triangle_area(a, b, c):
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    # Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Task 7: Format a list of names in a table
def format_names(names):
    # Define column widths
    max_name_length = max(len(name) for name in names)
    print("Names".center(max_name_length))
    print("-" * max_name_length)
    for name in names:
        print(name.ljust(max_name_length))

# Task 8: Clean a string (strip whitespace, remove punctuation, remove spaces)
def clean_string(s):
    # Strip leading/trailing whitespace
    s = s.strip()
    # Remove punctuation
    s = ''.join(char for char in s if char.isalnum() or char.isspace())
    # Remove all spaces
    s = s.replace(" ", "")
    return s

# Test cases
if __name__ == "__main__":
    # Task 1
    print("Task 1:")
    print(to_lowercase("Ryder"))
    print(to_lowercase("here"))
    print(to_lowercase("EVELYN"))
    print()

    # Task 2
    print("Task 2:")
    print(swap_case("HeLLo WoRLd"))
    print()

    # Task 3
    print("Task 3:")
    print(remove_uppercase("HelloWorld"))
    print()

    # Task 4
    print("Task 4:")
    print(count_case("KariBOGa"))  # Output: Uppercase: 4, Lowercase: 4
    print()

    # Task 5
    print("Task 5:")
    print(remove_non_letters("Meta-Chatbot@2003!"))  # Output: DataDriven
    print()

    # Task 6
    print("Task 6:")
    print(triangle_area(7, 8, 9))  # Output: 6.0
    print()

    # Task 7
    print("Task 7:")
    names = ["Mende", "Ken", "Mikeapp"]
    format_names(names)
    print()

    # Task 8
    print("Task 8:")
    print(clean_string("   Hello, Daddy!    "))  # Output: HelloWorld