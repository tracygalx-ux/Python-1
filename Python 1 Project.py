'''
Project
You are tasked with creating a simple inventory management system for a market. The system should allow users to add,
update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and
category.
Functionality:
Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name,
price, quantity, and category of the item.
Update Item: Implement a function update_item that allows users to update the details of an existing item in the
inventory. Users should be able to update the price, quantity, and category of the item.
View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details
(name, price, quantity, and category).
Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
Search by Category: Implement a function search_by_category that allows users to search for items in the inventory
based on their category. The function should display all items belonging to the specified category.
Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented
as a dictionary with keys for name, price, quantity, and category.
Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the
inventory.
Create a main loop to interact with the user. The loop should prompt the user to choose from various options such
as adding, updating, viewing, removing items, or searching by category.
'''

# Inventory list
inventory = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category: ").strip().lower()

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category

    }
    inventory.append(item)
    print(f"Item '{name}' added successfully.\n")


def update_item():
    name = input("Enter item name to update: ")

    for item in inventory:
        if item["name"] == name:
            item["price"] = float(input("Enter item price: "))
            item["quantity"] = int(input("Enter item quantity: "))
            item["category"] = input("Enter item category: ")
            print("Item updated successfully.")
            return
    print("Item not found in the inventory.\n")


def view_inventory():
    if len(inventory) == 0:
        print("\nInventory is empty.")
        return

    print("\nCurrent Inventory:\n")
    print("-----------------------")
    for item in inventory:
        print("Name:", item["name"])
        print("Price: $", item["price"])
        print("Quantity:", item["quantity"])
        print("Category:", item["category"])
        print("-------------------")

def remove_item():
    name = input("Enter item name to remove: ")

    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print("Item removed successfully!")
            return

    print("Item not found in the inventory.")


def search_by_category():
    category = input("Enter item category to search: ").strip().lower()
    found = False

    for item in inventory:
        if item["category"] == category:
            print("Name:", item["name"])
            print("Price:", item["price"])
            print("Quantity:", item["quantity"])
            print("Category:", item["category"])
            print("-----------------")
            found = True

    if not found:
        print("No item found in that category.")
# Main menu loop

while True:
    print("Inventory Management System")
    print("1. Add Item")
    print("2. Update Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Search by Category")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice =="1":
        add_item()
    elif choice =="2":
        update_item()
    elif choice =="3":
        view_inventory()
    elif choice =="4":
        remove_item()
    elif choice =="5":
        search_by_category()
    elif choice =="6":
        print("Exiting program.Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1-6.")
