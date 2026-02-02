"""
NAME:Justin MUriithi N
ADM:BSCIT-05-0071/2024
"""

# Get input from user
user_input = input("Enter a list of names (separated by commas): ")

# Split the input into a list of names and strip whitespace
names_list = [name.strip() for name in user_input.split(',')]

# Remove duplicates while preserving order, then sort alphabetically
unique_sorted_names = sorted(list(set(names_list)))

# Display results
print("\nFinal sorted list (no duplicates):")
for i, name in enumerate(unique_sorted_names, 1):
    print(f"{i}. {name}")

# Count and display total
print(f"\nTotal unique names: {len(unique_sorted_names)}")
print(f"Original entries: {len(names_list)} (including {len(names_list) - len(unique_sorted_names)} duplicates)")
