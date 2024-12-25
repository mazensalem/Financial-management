def tax_update(tax):

    with open("balance.txt", "r") as file:
        current_balance = file.read().strip()
        if current_balance:
            current_balance = float(current_balance)
        else:
            current_balance = 0.0

    
    tax_amount = current_balance * (tax / 100)
    
    
    with open("balance.txt", "w") as file:
        file.write("Balance: ",current_balance)
        file.write("Tax: ", tax_amount)


