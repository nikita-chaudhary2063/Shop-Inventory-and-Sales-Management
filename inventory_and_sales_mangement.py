
inventory = {
    "P101": {"name": "Notebook", "price": 120, "quantity": 25},
    "P102": {"name": "Pen", "price": 20, "quantity": 50},
    "P103": {"name": "Backpack", "price": 1500, "quantity": 8}
}
sales = {}
transaction_id = 1

while True:
    print("**** SHOP INVENTORY MANAGER ****")
    print("1. Display all products")
    print("2. Search for a product")
    print("3. Add a new product")
    print("4. Update product details")
    print("5. Delete a product")
    print("6. Check if a product exists")
    print("7. Count total products")
    print("8. Show total inventory value")
    print("9. Record a sale")
    print("10. View sales transactions")
    print("11. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(inventory) == 0:
            print("Inventory is empty!")
        else:
            for product_id, details in inventory.items():
                print("Product ID:", product_id)
                print("Name:", details["name"])
                print("Price:", details["price"])
                print("Quantity:", details["quantity"])
                print("--------------------")

    elif choice == "2":
        product_id = input("Enter product ID: ")

        if product_id in inventory:
            product = inventory[product_id]
            print("Product found!")
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
        else:
            print("Product not found!")

    elif choice == "3":
        product_id = input("Enter new product ID: ")

        if product_id in inventory:
            print("This product ID already exists!")
        else:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            if price > 0 and quantity >= 0:
                inventory[product_id] = {
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }
                print("Product added successfully!")
            else:
                print("Invalid price or quantity!")

    elif choice == "4":
        product_id = input("Enter product ID to update: ")

        if product_id in inventory:
            print("1. Update name")
            print("2. Update price")
            print("3. Update quantity")

            update_choice = input("Choose what to update: ")

            if update_choice == "1":
                inventory[product_id]["name"] = input("Enter new name: ")
                print("Name updated!")

            elif update_choice == "2":
                new_price = float(input("Enter new price: "))

                if new_price > 0:
                    inventory[product_id]["price"] = new_price
                    print("Price updated!")
                else:
                    print("Price must be positive!")

            elif update_choice == "3":
                new_quantity = int(input("Enter new quantity: "))

                if new_quantity >= 0:
                    inventory[product_id]["quantity"] = new_quantity
                    print("Quantity updated!")
                else:
                    print("Quantity cannot be negative!")

            else:
                print("Invalid update option!")
        else:
            print("Product not found!")

    elif choice == "5":
        product_id = input("Enter product ID to delete: ")

        if product_id in inventory:
            del inventory[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    elif choice == "6":
        product_id = input("Enter product ID: ")

        if product_id in inventory:
            print("Product exists in inventory.")
        else:
            print("Product does not exist.")

    elif choice == "7":
        print("Total different products:", len(inventory))

    elif choice == "8":
        total_value = 0

        for product_id, details in inventory.items():
            total_value += details["price"] * details["quantity"]

        print("Total inventory value:", total_value)

    elif choice == "9":
        product_id = input("Enter product ID to sell: ")

        if product_id in inventory:
            quantity_sold = int(input("Enter quantity to sell: "))

            if quantity_sold <= 0:
                print("Quantity must be positive!")

            elif quantity_sold <= inventory[product_id]["quantity"]:
                product = inventory[product_id]
                total_price = product["price"] * quantity_sold

                product["quantity"] -= quantity_sold

                sales[transaction_id] = {
                    "product_id": product_id,
                    "name": product["name"],
                    "quantity": quantity_sold,
                    "unit_price": product["price"],
                    "total": total_price
                }

                print("\n===== SALES RECEIPT =====")
                print("Transaction ID:", transaction_id)
                print("Product:", product["name"])
                print("Quantity:", quantity_sold)
                print("Unit price:", product["price"])
                print("Total amount:", total_price)
                print("Remaining stock:", product["quantity"])

                transaction_id += 1

            else:
                print("Not enough stock available!")

        else:
            print("Product not found!")

    elif choice == "10":
        if len(sales) == 0:
            print("No sales transactions yet.")
        else:
            for sale_id, details in sales.items():
                print("\nTransaction ID:", sale_id)
                print("Product ID:", details["product_id"])
                print("Product:", details["name"])
                print("Quantity sold:", details["quantity"])
                print("Unit price:", details["unit_price"])
                print("Total:", details["total"])
                print("--------------------")

    elif choice == "11":
        print("Thank you for using Shop Inventory Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
