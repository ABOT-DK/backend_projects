
# Product Inventory with Custom Exception Handling

This Python project demonstrates how to use a custom exception class to handle out-of-stock items in a simple product inventory system.

## Features

- `ProductInventory` represented by a dictionary
- Custom exception: `OutOfStockError`
- Function to simulate purchasing an item
- Exception handling using `try-except-finally`

## How It Works

- If an item is out of stock, the program raises a `OutOfStockError`.
- If an item exists and is in stock, it decrements the inventory.
- If the item doesn't exist, it notifies the user.
- A `finally` block confirms that the request has been processed.

## Example Output

```
Sorry, the item 'orange' is out of stock.
Finished processing request for 'orange'.

One apple purchased. Remaining: 9
Finished processing request for 'apple'.

The item 'pineapple' does not exist in inventory.
Finished processing request for 'pineapple'.
```

## Run the Program

```bash
python inventory.py
```

## License

MIT License
