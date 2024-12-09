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
