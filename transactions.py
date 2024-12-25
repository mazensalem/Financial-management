import tkinter as tk
import tkinter.messagebox
from time import gmtime, strftime
from products import get_products, get_price, get_name, add_products, remove_products, get_balance
from copy import deepcopy

def is_float(i):
    try:
        float(i)
        return True
    except:
        return False

def get_transactions():
    file = open("transactions.csv", "r")
    data = file.readlines()
    file.close()
    data = [i.strip().split(",") for i in data]
    return data

def update_transaction(data, window):
    alldata = get_transactions()
    data = [str(data["transaction_id"]), str(data["date"]), str(data["type"]), str(data["total_price"]), str(data["amount"]), str(data["product_id"]), str(data["tax"]), str(data["discount"])]
    if data[0] == '-1':
        maxid = 0
        for row in alldata:
            if row[0].isdigit() and int(row[0]) >= maxid:
                maxid = int(row[0])+1
        data[0] = str(maxid)
        alldata.append(data)
        if data[2] == "selling":
            if not remove_products(data[5], data[4]):
                tkinter.messagebox.showerror("Error", "Make sure you have enought amount of that product", parent=window)
                return "error"
        else:
            if not add_products(data[5], data[4]):
                tkinter.messagebox.showerror("Error", "Make sure you have enought balance", parent=window)
                return "error"
    else:
        for i in range(len(alldata)):
            if alldata[i][0] == data[0]:
                remove_products(alldata[i][5], alldata[i][4], False)
                add_products(alldata[i][5], data[4], False)
                alldata[i] = data

    alldata = "\n".join([",".join(row) for row in alldata])
    file = open("transactions.csv", "w")
    file.write(alldata)
    file.close()

def delete_transaction(id, transactions_window):
    global data
    res = tkinter.messagebox.askquestion("Warning", "are you sure you want to delete", parent=transactions_window, default="no")
    data = get_transactions()
    if res == "yes":
        for i in range(len(data)):
            if data[i][0] == id:
                if data[i][2] == "buying":
                    if remove_products(data[i][5], data[i][4], False):
                        del data[i]
                    else:
                        tkinter.messagebox.showerror("Error", "This would make the amount negative", parent=transactions_window)
                else:
                    add_products(data[i][5], data[i][4], False)
                    del data[i]
                break
    
    file = open("transactions.csv", "w")
    data = ("\n".join([",".join(row) for row in data])).lstrip("\n")
    file.write(data)
    file.close()

    data = get_transactions()

    view_transaction()

def create_edit_window(transactions_window, idata={"transaction_id":-1, "total_price":0, "amount": 0, "tax": 0, "discount": 0, "type": "buying", "product_id": -1}):

    pricevar = tk.StringVar(value=idata["total_price"])
    amountvar = tk.StringVar(value=idata["amount"])
    taxvar = tk.StringVar(value=idata["tax"])
    discountvar = tk.StringVar(value=idata["discount"])
    typevar = tk.StringVar(value=(idata["type"]))
    productvar = tk.StringVar(value=("---------" if idata["product_id"] == -1 else idata["product_id"]))
    datac = deepcopy(idata)

    create_window = tk.Toplevel()



    def calcprice(*args):
        n = int(amountvar.get() if amountvar.get().isdigit() else 0)

        price = (get_price(int(productvar.get().split(" ")[0]))) if productvar.get() != "---------" else {"price_buying":0, "price_selling": 0}
        discount =1-((float(discountvar.get()) if is_float(discountvar.get()) and float(discountvar.get()) != 0 else 0)/100)
        tax = ((((float(taxvar.get()) if is_float(taxvar.get()) else 0)/100))+1)
        priceb = round(n * int(price["price_buying"]) * discount * tax, 5)
        prices = round(n * int(price["price_selling"]) * discount * tax, 5)

        pricevar.set(priceb if typevar.get() == "buying" else prices)


    def get_product_name():
        product_names = []
        data = get_products()
        for row in data:
            if row[0].isdigit():
                product_names.append(f"{row[0]} {row[1]}")

        return product_names
    
    def setdata(root):
        datac["date"] = strftime("%d/%m/%Y", gmtime())
        datac["type"] = typevar.get()
        datac["total_price"] = float(pricevar.get())
        try:
            if int(amountvar.get()) == 0:
                tkinter.messagebox.showerror("Error", "Make sure that you enter a non-zero number for the amount", parent=create_window)
                return
            
            datac["amount"] = int(amountvar.get())
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you entered only whole numbers for the amount", parent=create_window)
            return
        
        try:
            datac["product_id"] = int(productvar.get().split(" ")[0])
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you choose an option for the product", parent=create_window)
            return
        
        try:
            datac["tax"] = float(taxvar.get())/100
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you entered only dicimal numbers for the tax", parent=create_window)
            return
        
        try:
            datac["discount"] = float(discountvar.get())/100
        except:
            tkinter.messagebox.showerror("Error", "Make sure that you entered only dicimal numbers for the discount", parent=create_window)
            return
        
        if update_transaction(datac, root) != "error":
            root.destroy()
            global data
            data = get_transactions()
            if transactions_window:
                transactions_window.destroy()
                view_transaction()


    
    lable1 = tk.Label(create_window, text="Enter the type")
    Enterytype = tk.OptionMenu(create_window, typevar, "buying", "selling")
    typevar.trace_add('write', calcprice)
    lable1.grid(row=0, column=0)
    Enterytype.grid(row=0, column=1)



    lable2 = tk.Label(create_window, text="Enter the product")
    Enterytype = tk.OptionMenu(create_window, productvar, *get_product_name())
    productvar.trace_add('write', calcprice)
    lable2.grid(row=1, column=0)
    Enterytype.grid(row=1, column=1)


    
    lable4 = tk.Label(create_window, text="Enter the quantity")
    Enteryamount = tk.Entry(create_window, textvariable=amountvar)
    amountvar.trace_add('write', calcprice)
    lable4.grid(row=2, column=0)
    Enteryamount.grid(row=2, column=1)

    lable5 = tk.Label(create_window, text="Enter the tax")
    Enterytax = tk.Entry(create_window, textvariable=taxvar)
    taxvar.trace_add('write', calcprice)
    lable5.grid(row=3, column=0)
    Enterytax.grid(row=3, column=1)

    lable6 = tk.Label(create_window, text="Enter the discount")
    Enterydiscount = tk.Entry(create_window, textvariable=discountvar)
    discountvar.trace_add('write', calcprice)
    lable6.grid(row=4, column=0)
    Enterydiscount.grid(row=4, column=1)

    lablesumtext = tk.Label(create_window, text="Your total is: ", anchor="center")
    lablesumvalue = tk.Label(create_window, textvariable=pricevar, anchor="w")
    lablesumvalue.grid(row=5, column=1)
    lablesumtext.grid(row=5, column=0)


    Submit = tk.Button(create_window, text="Save", command=lambda: setdata(create_window))
    Submit.grid(row=6, column=0, columnspan=2)


columnvardataf = "---------"
filtervardata = "---------"
valuevardata = ""
def filter(transactions_window):
    def filterdata():
        global data
        global columnvardataf
        global filtervardata
        global valuevardata
        columnvardataf = columnvar.get()
        filtervardata = filtervar.get()
        valuevardata = valuevar.get()

        columnmap = {"transaction_id": 0, "date": 1, "type": 2, "total_price": 3, "amount": 4, "product_id": 5, "tax": 6, "dicount": 7}
        check = lambda el : el < float(valuevar.get()) if filtervar.get() == "less than" else (el > float(valuevar.get()) if filtervar.get() == "bigger than" else el == float(valuevar.get()))
        i = 0
        while i < len(data):
            if i != 0:
                if not check(float(data[i][columnmap[columnvar.get()]])):
                    del data[i]
                    i-=1
            i+=1
        transactions_window.destroy()
        view_transaction()
    
    def reset():
        global data
        global columnvardataf
        global filtervardata
        global valuevardata
        columnvardataf = "---------"
        filtervardata = "---------"
        valuevardata = ""
        data = get_transactions()
        transactions_window.destroy()
        view_transaction()




    columnvar = tk.StringVar(value=columnvardataf)
    filtervar = tk.StringVar(value=filtervardata)
    valuevar = tk.StringVar(value=valuevardata)

    filterfram = tk.Frame(transactions_window)
    filterfram.grid(row=1, column=1, columnspan=4)

    columnfilter = tk.OptionMenu(filterfram,columnvar, "transaction_id", "total_price", "amount")
    columnfilter.grid(row=0, column=1)
    filterchose = tk.OptionMenu(filterfram,filtervar,  "less than", "equal", "bigger than")
    filterchose.grid(row=0, column=2)
    filtervalue = tk.Entry(filterfram, textvariable=valuevar)
    filtervalue.grid(row=0, column=3)
    filterbutton = tk.Button(filterfram, text="Filter", command=filterdata)
    filterbutton.grid(row=0, column=4)


    resetbutton = tk.Button(filterfram, text="Reset", command=reset)
    resetbutton.grid(row=0, column=7)

columnvardatas = "---------"
sortvardata = "---------"
sorted = False
def sort(transactions_window):
    global sorted
    def sortdata(*args):
        global data
        global sorted
        global columnvardatas
        global sortvardata
        sorted = True
        columnvardatas = columnvar.get()
        sortvardata = sortvar.get()
        columnmap = {"transaction_id": 0, "date": 1, "type": 2, "total_price": 3, "amount": 4, "product_id": 5, "tax": 6, "discount": 7}
        if sortvar.get() == "ASC":
            for i in range(len(data)-1):
                for j in range(i, len(data)-1):
                    if float(data[i+1][columnmap[columnvar.get()]]) > float(data[j+1][columnmap[columnvar.get()]]):
                        data[i+1], data[j+1] = data[j+1], data[i+1]
        else:
            for i in range(len(data)-1):
                for j in range(i, len(data)-1):
                    if float(data[i+1][columnmap[columnvar.get()]]) < float(data[j+1][columnmap[columnvar.get()]]):
                        data[i+1], data[j+1] = data[j+1], data[i+1]

        transactions_window.destroy()
        view_transaction()


    columnvar = tk.StringVar(value=columnvardatas)
    sortvar = tk.StringVar(value=sortvardata)


    sortfram = tk.Frame(transactions_window)
    sortfram.grid(row=1, column=6, columnspan=3)

    columnsort = tk.OptionMenu(sortfram,columnvar, "transaction_id", "total_price", "amount")
    columnsort.grid(row=0, column=1)
    sortchose = tk.OptionMenu(sortfram, sortvar, "ASC", "DEC")
    sortvar.trace_add("write", sortdata)
    sortchose.grid(row=0, column=2)




data = get_transactions()
def view_transaction():
    global data
    global sorted
    if not sorted:
        data = get_transactions()
    else:
        sorted = False

    transactions_window = tk.Toplevel()
    height = len(data)
    width = len(data[0])
    
    createbutton = tk.Button(transactions_window, text="create", command=lambda:create_edit_window(transactions_window))
    createbutton.grid(row=1, column=0)
    filter(transactions_window)
    sort(transactions_window)

    starti = 2;
    balance_label = tk.Label(transactions_window, text=f"balance:  {get_balance()[1] + get_balance()[1]}", justify="center")
    balance_label.grid(row=0, columnspan=8)
    for i in range(height):
        for j in range(width):
            b = tk.Label(transactions_window, text=data[i][j], anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )
            if j == 5 and i != 0:
                b = tk.Label(transactions_window, text=data[i][j] + " " + get_name(data[i][j]), anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )
            if (j == 6 or j == 7) and i != 0:
                b = tk.Label(transactions_window, text=str(float(data[i][j])*100) + " %", anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )

            b.grid(row=i+starti, column=j)
        if i != 0:
            editbutton = tk.Button(transactions_window, text="edit", command=lambda i=i: (create_edit_window(transactions_window, {"transaction_id": data[i][0], "date": data[i][1], "type": data[i][2], "total_price": data[i][3], "amount": data[i][4], "product_id": data[i][5] + " " + get_name(data[i][5]), "tax": data[i][6],"discount": data[i][7] })))
            editbutton.grid(row=i+starti, column=j+1)
            deletbutton = tk.Button(transactions_window, text="delete", command=lambda i=i: (delete_transaction(data[i][0], transactions_window), transactions_window.destroy()))
            deletbutton.grid(row=i+starti, column=j+2)
