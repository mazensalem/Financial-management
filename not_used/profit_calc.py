def profit_calc(product_id):
   

    product_data = {
        "Pr01": {"cost_price": 50, "selling_price": 40, "sold_quantity": 50},
        "Pr02": {"cost_price": 30, "selling_price": 20, "sold_quantity": 30},
        "Pr03": {"cost_price": 100, "selling_price": 90, "sold_quantity": 20},
    }
    
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    
    
    product_info = product_data[product_id]
    cost_price = product_info["cost_price"]
    selling_price = product_info["selling_price"]
    sold_quantity = product_info["sold_quantity"]
    
    
    money_made = selling_price * sold_quantity
    money_spent = cost_price * sold_quantity
    profit = money_made - money_spent
    
    
    
    with open("balance.txt", "a") as file:
        file.write("Product ID: ", product_id, "Profit: ",profit)

    return profit


