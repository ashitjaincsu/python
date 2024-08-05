class ItemToPurchase:
    def __init__(self, name="none", description = '', price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.__cost = price * quantity

    def get_item_cost(self):
        return self.price * self.quantity

    def print_item_cost(self):
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${self.__cost:.2f}")

# Function to get item details from the user
def get_item_details():
    item_name = input("Enter the item name:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(item_name, item_name, item_price, item_quantity)

def main():
    print("Item 1")
    item1 = get_item_details()

    print("\nItem 2")
    item2 = get_item_details()

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = item1.get_item_cost() + item2.get_item_cost()
    print(f"Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
