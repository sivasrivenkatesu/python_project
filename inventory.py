import random
import tkinter as tk
from tkinter import messagebox

class Product:
    def _init_(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def _init_(self, low_stock_threshold=10):
        self.products = []
        self.low_stock_threshold = low_stock_threshold

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to inventory.")

    def display_inventory(self):
        print("Inventory:")
        print("ID      | Name         | Price  | Quantity")
        print("-" * 45)
        for product in self.products:
            print(f"{product.id: <8} | {product.name: <12} | ${product.price:.2f} | {product.quantity: <8}")
            if product.quantity < self.low_stock_threshold:
                self.show_low_stock_warning(product.name)

    def sell_product(self, product_id, quantity_sold):
        for product in self.products:
            if product.id == product_id:
                if product.quantity >= quantity_sold:
                    product.quantity -= quantity_sold
                    print(f"{quantity_sold} {product.name}(s) sold.")
                    if product.quantity < self.low_stock_threshold:
                        self.show_low_stock_warning(product.name)
                else:
                    print(f"Not enough {product.name} in stock to sell.")
                return
        print("Product not found in inventory.")

    def show_low_stock_warning(self, product_name):
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showwarning("Low Stock Warning", f"WARNING: Quantity of {product_name} is below the low stock threshold!")
        root.destroy()

# Function to create a product object from user input
def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = 50 + random.randint(1, 50)  # Initial quantity as 50 + random number between 1 and 50
    id = random.randint(1000, 9999)  # Random 4-digit ID
    return Product(id, name, price, quantity)

# Sample usage
if __name__ == "_main_":
    inventory = Inventory()

    # Predefined smartphone names and prices
    smartphones = [
        ("iPhone 13", 999.99),
        ("Samsung Galaxy S21", 899.99),
        ("Google Pixel 6", 799.99),
        ("OnePlus 9 Pro", 899.99),
        ("Xiaomi Mi 11", 699.99),
        ("Huawei P50 Pro", 1099.99),
        ("Sony Xperia 1 III", 1199.99),
        ("LG Velvet", 699.99),
        ("Motorola Edge+", 799.99),
        ("Nokia 9 PureView", 699.99)
    ]

    # Adding predefined smartphones to inventory
    for name, price in smartphones:
        id = random.randint(1000, 9999)  # Random 4-digit ID
        quantity = 50 + random.randint(1, 50)  # Initial quantity as 50 + random number between 1 and 50
        inventory.add_product(Product(id, name, price, quantity))

    while True:
        print("\n1. Add Product\n2. Display Inventory\n3. Sell Product\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product = create_product()
            inventory.add_product(product)
        elif choice == "2":
            inventory.display_inventory()
        elif choice == "3":
            product_id = int(input("Enter product ID to sell: "))
            quantity_sold = int(input("Enter quantity to sell: "))
            inventory.sell_product(product_id, quantity_sold)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")