# Product Billing and Inventory Management System

This project implements a basic billing and inventory management system using Python. The system allows users to view available products, purchase items, and update the inventory accordingly. The program reads and writes product data from a JSON file and logs sales information into a text file for record-keeping.

## Features

- **Product Menu Display**: Displays the list of available products along with their price and available quantity.
- **User Input**: Collects user details such as name, email, phone number, product ID, and the desired quantity to purchase.
- **Billing**: Generates a bill for the purchased items based on user input, deducting the quantity from inventory.
- **Inventory Update**: Updates the product stock in the `product_Records.json` file.
- **Sales Logging**: Appends each sale record to a `sales.txt` file for future reference.
- **Partial Purchases**: If the requested quantity is not available, the user is given the option to buy the available stock.

## Files

- `product_Records.json`: Stores product data in the following format:
  ```json
  {
      "product_id_1": {
          "Product_Name": "Product A",
          "Price": 100,
          "Quantity": 50
      },
      "product_id_2": {
          "Product_Name": "Product B",
          "Price": 200,
          "Quantity": 30
      },
      ...
  }
# Customer Details Saving In This format :

<user_name>, <user_email>, <user_phone>, <product_id>, <product_name>, <quantity>, <total_price>, <timestamp>
