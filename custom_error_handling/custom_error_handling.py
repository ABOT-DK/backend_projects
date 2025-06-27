class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."


# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}


# Function to simulate purchasing an item
def purchase_item(item_name):
    try:
        if item_name not in product_inventory:
            print(f"The item '{item_name}' does not exist in inventory.")
        elif product_inventory[item_name] == 0:
            raise OutOfStockError(item_name)
        else:
            product_inventory[item_name] -= 1
            print(f"One {item_name} purchased. Remaining: {product_inventory[item_name]}")
    except OutOfStockError as e:
        print(e)
    finally:
        print(f"Finished processing request for '{item_name}'.\n")


# Test cases
purchase_item("orange")
purchase_item("apple")
purchase_item("pineapple")
