import datetime
def date_set():

    current_time = datetime.datetime.now()
    transaction_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("balance.txt", "a") as file:
        file.write("Transaction Date: ", transaction_date)