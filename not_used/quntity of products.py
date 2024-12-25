import csv
import os

def Quantity_Of_Product(ID_of_product, count):

    file= open('stocks.csv','r')
    reader = csv.reader(file)
    rows = list(reader)
    file.close()
    if len(rows) == 0:
        print("The file 'stocks.csv' is empty. No products to update.")
        return

    for row in rows:
        if len(row) != 0:
            if row[0] == str(ID_of_product):  
                row.append(str(count))  
                break
    else:
        print(f"Product ID {ID_of_product} not found.")
        return

    file= open('stocks.csv','w')
    writer = csv.writer(file)
    writer.writerows(rows)  
    file.close()
    print(f"Product ID {ID_of_product} updated with quantity {count}.")

Quantity_Of_Product(1, 3)