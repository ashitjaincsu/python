class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            total_items = self.get_num_items_in_cart()
            print(f"Number of Items: {total_items}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            total_cost = self.get_cost_of_cart()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
m - Modify item in cart
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
"""
    while True:
        print(menu)
        choice = input().strip()
        if choice == 'a':
            add_item_to_cart(cart)
        elif choice == 'r':
            remove_item_from_cart(cart)
        elif choice == 'm':
            modify_item_in_cart(cart)
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose again.")

def add_item_to_cart(cart):
    print("ADD ITEM TO CART")
    name = input("Enter the item name:\n")
    description = input("Enter the item description:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    item = ItemToPurchase(name, price, quantity, description)
    cart.add_item(item)

def remove_item_from_cart(cart):
    print("REMOVE ITEM FROM CART")
    item_name = input("Enter the item name to remove:\n")
    cart.remove_item(item_name)

def modify_item_in_cart(cart):
    print("MODIFY ITEM IN CART")
    name = input("Enter the item name:\n")
    description = input("Enter the new description (or leave empty to keep current):\n")
    price = input("Enter the new price (or leave empty to keep current):\n")
    quantity = input("Enter the new quantity (or leave empty to keep current):\n")

    description = description if description else "none"
    price = int(price) if price else 0
    quantity = int(quantity) if quantity else 0

    item = ItemToPurchase(name, price, quantity, description)
    cart.modify_item(item)

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()
