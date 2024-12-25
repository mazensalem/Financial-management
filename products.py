from copy import deepcopy
def get_balance():
    file = open("balance.txt", "r")
    data = file.readline().split(",")
    ibalance = int(data[0])
    balance = int(data[1])
    file.close()
    return [ibalance, balance]


def get_products():
    file = open("products.csv", "r")
    data = file.readlines()
    file.close()
    data = [i.strip().split(",") for i in data]
    return data

def get_price(id):
    file = open("products.csv", "r")
    data = file.readlines()
    file.close()
    data = [i.strip().split(",") for i in data]
    for row in data:
        if row[0] == str(id):
            return {"price_buying":row[3], "price_selling":row[4]}
    raise Exception("Didn't found the id for the function get_price")


def get_name(id):
    file = open("products.csv", "r")
    data = file.readlines()
    file.close()
    data = [i.strip().split(",") for i in data]
    for row in data:
        if row[0] == str(id):
            return row[1]
    raise Exception("Didn't found the id for the function get_name")


def add_products(product_id, quantity, balance=True):
    products = get_products()
    fproduct = None
    for product in products:
        if product[0] == product_id:
            fproduct = deepcopy(product)
            product[2] = str(int(quantity) + int(product[2]))

    if balance:
        if get_balance()[1] + get_balance()[0] -int(fproduct[3])*int(quantity) < 0:
            return False
        btext = str(get_balance()[0]) + "," + str(get_balance()[1]-int(fproduct[3])*int(quantity))
        balafile = open("balance.txt", "w")
        balafile.write(btext)
        balafile.close()
    alldata = "\n".join([",".join(row) for row in products])
    prodfile = open("products.csv", "w")
    prodfile.write(alldata)
    prodfile.close()
    return True


def remove_products(product_id, quantity, balance=True):
    products = get_products()
    fproduct = None
    for product in products:
        if product[0] == product_id:
            fproduct = deepcopy(product)
            product[2] = str(int(product[2]) - int(quantity))
    

    if int(fproduct[2]) - int(quantity) < 0:
        return False
    
    if balance:
        btext = str(get_balance()[0]) + "," + str(get_balance()[1]+int(fproduct[4])*int(quantity))
        balafile = open("balance.txt", "w")
        balafile.write(btext)
        balafile.close()
    alldata = "\n".join([",".join(row) for row in products])
    prodfile = open("products.csv", "w")
    prodfile.write(alldata)
    prodfile.close()
    return True

