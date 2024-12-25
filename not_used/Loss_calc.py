def loss_calc (product_id):
   
    product_data = {
        "Pr01": {"cost_price": 50, "selling_price": 40, "unsold_quantity": 10},
        "Pr02": {"cost_price": 30, "selling_price": 20, "unsold_quantity": 5},
        "Pr03": {"cost_price": 100, "selling_price": 90, "unsold_quantity": 2}, # I wrote any product ID and any prices
    }
    
  
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    

    product_info = product_data[product_id]
    cost_price = product_info["cost_price"]
    selling_price = product_info["selling_price"]
    unsold_quantity = product_info["unsold_quantity"]
    
    if cost_price>selling_price:
        loss_per_unit = cost_price - selling_price
        lost_amount = loss_per_unit * unsold_quantity
    

    
        with open("balance.txt", "r") as file:
            current_balance = file.read().strip()
            if current_balance:
                current_balance = float(current_balance)
            else:
                current_balance = 0.0
   
    
        new_balance = current_balance + lost_amount
    

        with open("balance.txt", "w") as file:
            file.write(str(new_balance))
    
    return lost_amount


