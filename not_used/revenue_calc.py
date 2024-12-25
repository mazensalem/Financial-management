def revenue_calc (product_id):
  
    product_data = {
        "Pr01": {"selling_price": 40, "sold_quantity": 50},
        "Pr02": {"selling_price": 20, "sold_quantity": 30},
        "Pr03": {"selling_price": 90, "sold_quantity": 20},
    }
    
    
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    
    product_info = product_data[product_id]
    selling_price = product_info["selling_price"]
    sold_quantity = product_info["sold_quantity"]
    
    revenue = selling_price * sold_quantity
    
   
  
    with open("balance.txt", "a") as file:
        file.write("Product ID: ", product_id, "Revenue: ", revenue)

    
    return revenue

