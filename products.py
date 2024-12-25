from copy import deepcopy
import tkinter as tk
import tkinter.messagebox


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


def update_products(datac, root):
    alldata = get_products()
    data = [str(datac["product_id"]), datac["name"], str(datac["quantity"]), str(datac["price_buying"]), str(datac["price_selling"])]
    if data[0] == '-1':
        maxid = 0
        for row in alldata:
            if row[0].isdigit() and int(row[0]) >= maxid:
                maxid = int(row[0])+1
        data[0] = str(maxid)
        alldata.append(data)
    else:
        for i in range(len(alldata)):
            if alldata[i][0] == data[0]:
                alldata[i] = data

    alldata = "\n".join([",".join(row) for row in alldata])
    file = open("products.csv", "w")
    file.write(alldata)
    file.close()


def create_edit_windowp(transactions_window, idata={"product_id":-1, "name":"", "quantity": 0, "price_buying": 0, "price_selling": 0}):
    profitvar = tk.StringVar(value=str(int(idata["price_selling"]) - int(idata["price_buying"])))
    namevar = tk.StringVar(value=idata["name"])
    bpricevar = tk.StringVar(value=idata["price_buying"])
    spricevar = tk.StringVar(value=idata["price_selling"])
    datac = deepcopy(idata)

    create_window = tk.Toplevel()



    def calcprofit(*args):
        profitvar.set(str(int(spricevar.get() or 0) - int(bpricevar.get() or 0)))

    def setdata(root):
        datac["name"] = namevar.get()
        try:
            if int(bpricevar.get()) <= 0:
                tkinter.messagebox.showerror("Error", "Make sure that you enter a non-zero number for the buying price", parent=create_window)
                return
            
            datac["price_buying"] = int(bpricevar.get())
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you entered only whole numbers for the buying price", parent=create_window)
            return
        
        try:
            if int(spricevar.get()) <= 0:
                tkinter.messagebox.showerror("Error", "Make sure that you enter a non-zero number for the selling price", parent=create_window)
                return
            
            datac["price_selling"] = int(spricevar.get())
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you entered only whole numbers for the selling price", parent=create_window)
            return
        
        
        
        
        update_products(datac, root)
        root.destroy()
        global data
        data = get_products()
        if transactions_window:
            transactions_window.destroy()
            view_products()


   
    lable4 = tk.Label(create_window, text="Enter the name")
    Enteryname = tk.Entry(create_window, textvariable=namevar)
    lable4.grid(row=2, column=0)
    Enteryname.grid(row=2, column=1)

    lable5 = tk.Label(create_window, text="Enter the buying price")
    Enterytax = tk.Entry(create_window, textvariable=bpricevar)
    bpricevar.trace_add('write', calcprofit)
    lable5.grid(row=3, column=0)
    Enterytax.grid(row=3, column=1)


    lable6 = tk.Label(create_window, text="Enter the selling price")
    Enteryprices = tk.Entry(create_window, textvariable=spricevar)
    spricevar.trace_add('write', calcprofit)
    lable6.grid(row=4, column=0)
    Enteryprices.grid(row=4, column=1)

    lablesumtext = tk.Label(create_window, text="The profit per unit is: ", anchor="center")
    lablesumvalue = tk.Label(create_window, textvariable=profitvar, anchor="w")
    lablesumvalue.grid(row=5, column=1)
    lablesumtext.grid(row=5, column=0)


    Submit = tk.Button(create_window, text="Save", command=lambda: setdata(create_window))
    Submit.grid(row=6, column=0, columnspan=2)


def delete_product(id, transactions_window):
    global data
    res = tkinter.messagebox.askquestion("Warning", "are you sure you want to delete", parent=transactions_window, default="no")
    data = get_products()
    if res == "yes":
        for i in range(len(data)):
            if data[i][0] == id:
                del data[i]
                break
    
    file = open("products.csv", "w")
    data = ("\n".join([",".join(row) for row in data])).lstrip("\n")
    file.write(data)
    file.close()

    data = get_products()

    view_products()



def view_products():
    global data
    data = get_products()

    transactions_window = tk.Toplevel()
    height = len(data)
    width = len(data[0])
    
    createbutton = tk.Button(transactions_window, text="create", command=lambda:create_edit_windowp(transactions_window))
    createbutton.grid(row=0, column=0)

    starti = 1;
    for i in range(height):
        for j in range(width):
            b = tk.Label(transactions_window, text=data[i][j], anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )
            if j == 5 and i != 0:
                b = tk.Label(transactions_window, text=data[i][j] + " " + get_name(data[i][j]), anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )
            if (j == 6 or j == 7) and i != 0:
                b = tk.Label(transactions_window, text=str(float(data[i][j])*100) + " %", anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )

            b.grid(row=i+starti, column=j)
        if i != 0:
            editbutton = tk.Button(transactions_window, text="edit", command=lambda i=i: (create_edit_windowp(transactions_window, {"product_id":data[i][0], "name":data[i][1], "quantity": data[i][2], "price_buying": data[i][3], "price_selling": data[i][4]})))
            editbutton.grid(row=i+starti, column=j+1)
            deletbutton = tk.Button(transactions_window, text="delete", command=lambda i=i: (delete_product(data[i][0], transactions_window), transactions_window.destroy()))
            deletbutton.grid(row=i+starti, column=j+2)
