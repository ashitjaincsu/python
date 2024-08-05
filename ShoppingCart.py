import ItemToPurchase
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
        for item in self.cart_items:
            if item.name == item.name:
                if item.description != "none":
                    item.description = item.description
                if item.price != 0:
                    item.price = item.price
                if item.quantity != 0:
                    item.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def print_total(self):
        total_cost = 0
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("OUTPUT SHOPPING CART")
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.get_item_cost()}")
                total_cost += item.get_item_cost()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase.ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter the item name to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name to modify: ")
            description = input("Enter the new description (or 'none' to leave unchanged): ")
            price = int(input("Enter the new price (or 0 to leave unchanged): "))
            quantity = int(input("Enter the new quantity (or 0 to leave unchanged): "))
            item = ItemToPurchase.ItemToPurchase(name, description, price, quantity)
            cart.modify_item(item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()