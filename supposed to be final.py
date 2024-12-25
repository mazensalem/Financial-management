data = {
    "Pr01": {"cost_price": 50, "selling_price": 40, "unsold_quantity": 10},
    "Pr02": {"cost_price": 30, "selling_price": 20, "unsold_quantity": 5},
    "Pr03": {"cost_price": 100, "selling_price": 90, "unsold_quantity": 2}
}

print(data)
sho= int(input(' If you want to show the loss, type 1 \n If you want to show the profit, type 2 \n If you want to show the revenue, type 3 \n If you want to show the taxes, type 4'))
def loss_calc (product_id):
   
    product_data = {
        "Pr01": {"cost_price": 50, "selling_price": 40, "unsold_quantity": 10},
        "Pr02": {"cost_price": 30, "selling_price": 20, "unsold_quantity": 5},
        "Pr03": {"cost_price": 100, "selling_price": 90, "unsold_quantity": 2}} # I wrote any product ID and any price
      
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    else:

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
def profit_calc(product_id):
    

    product_data = {
        "Pr01": {"cost_price": 50, "selling_price": 40, "sold_quantity": 50},
        "Pr02": {"cost_price": 30, "selling_price": 20, "sold_quantity": 30},
        "Pr03": {"cost_price": 100, "selling_price": 90, "sold_quantity": 20}
    }
    
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    
    else:
        product_info = product_data[product_id]
        cost_price = product_info["cost_price"]
        selling_price = product_info["selling_price"]
        sold_quantity = product_info["sold_quantity"]
    
    
        money_made = selling_price * sold_quantity
        money_spent = cost_price * sold_quantity
        profit = money_made - money_spent
        profit=str(profit)
    
    
        file = open('balance.txt','w') 
        file.write(profit) 
        file.close()

        return print(profit)
def revenue_calc (product_id):
  
    product_data = {
        "Pr01": {"selling_price": 40, "sold_quantity": 50},
        "Pr02": {"selling_price": 20, "sold_quantity": 30},
        "Pr03": {"selling_price": 90, "sold_quantity": 20},
    }
    
    
    if product_id not in product_data:
        print("Product not found.")
        return 0.0
    else:
        product_info = product_data[product_id]
        selling_price = product_info["selling_price"]
        sold_quantity = product_info["sold_quantity"]
    
        revenue = selling_price * sold_quantity
    
   
  
        with open("balance.txt", "a") as file:
            file.write( str(revenue))

    
        return revenue
def tax_update(tax):

    with open("balance.txt", "r") as file:
        current_balance = file.read().strip()
        if current_balance:
            current_balance = float(current_balance)
        else:
            current_balance = 0.0

    
    tax_amount = current_balance * (tax / 100)
    
    
    with open("balance.txt", "w") as file:
        file.write(str(current_balance))
        file.write(str(tax_amount))

if sho == 1:
    prid= input("enter the produc id")
    print= (loss_calc(prid))
elif sho == 2:
    pr0id= input("enter the produc id")
    print= (profit_calc(pr0id))
elif sho == 3:
    pr1id= input("enter the produc id")
    print= (revenue_calc (pr1id))
elif sho == 4:
    pr2id= input("enter the tax value")
    print= (tax_update(pr2id))