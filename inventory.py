"""
NAME:Justin MUriithi N
ADM:BSCIT-05-0071/2024
"""

# Simple inventory system - stores items and their quantities in a dictionary
inventory = {}  # Dictionary to hold item names as keys and quantities as values

# Function to add new item OR update quantity of existing item
def add_or_update_item():
    name = input("Enter item name: ").strip()  # Get item name, remove extra spaces
    quantity = int(input("Enter quantity: "))  # Convert input to integer for quantity

    if name in inventory:  # Check if item already exists
        inventory[name] += quantity  # Add to existing quantity
        print(f"Updated {name}. New quantity: {inventory[name]}")
    else:
        inventory[name] = quantity  # Create new entry for new item
        print(f"Added {name} with quantity {quantity}.")

# Function to look up and display info for a specific item
def get_item_info():
    name = input("Enter item name to check: ").strip()  # Get name to search for
    if name in inventory:  # Check if item exists in inventory
        print(f"{name}: {inventory[name]} in stock.")  # Show quantity if found
    else:
        print(f"{name} is not in the inventory.")  # Message if not found

# Function to calculate and display total quantity of ALL items
def total_quantity():
    total = sum(inventory.values())  # Sum all quantities (values in dictionary)
    print(f"Total quantity of all items: {total}")

# Main program loop - keeps running until user chooses to exit
while True:
    print("\nInventory Menu")  # Clear visual separator
    print("1. Add or update item")
    print("2. Check item information")
    print("3. Show total quantity of all items")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")  # Get user's menu selection

    if choice == "1":
        add_or_update_item()  # Call function to add/update
    elif choice == "2":
        get_item_info()  # Call function to check item
    elif choice == "3":
        total_quantity()  # Call function to show total
    elif choice == "4":
        print("Exiting program.")  # Goodbye message
        break  # Exit the while loop
    else:
        print("Invalid choice. Please enter 1-4.")  # Handle bad input
