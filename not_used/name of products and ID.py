import csv
import os

def Name_of_product():
    Name_of_product = input("Please enter the name of the product: ")
    
    
    new_id = 1  
    
    if os.path.exists('stocks.csv'):
        file=open('stocks.csv', "r")
        reader = csv.reader(file)
        stocks = list(reader)  
          
        for row in stocks:
            if Name_of_product == row[1]: 
                print("Product already is found in the system!")
                return int(row[0])  
        if len(stocks) > 1: 
            last_id = int(stocks[-1])  
            new_id = last_id + 1  
        else:
            new_id = 1
        file.close()
    
        file=open('stocks.csv', "w")
        writer = csv.writer(file)
        print(" ")
        if os.stat('stocks.csv').st_size == 0:
            writer.writerow(["ID", "Name", "quantity"])  

        writer.writerow([new_id, Name_of_product])
        file.close()

    print(f"Product '{Name_of_product}' has been successfully added to then stocks file with ID {new_id}")
    return new_id

Name_of_product()