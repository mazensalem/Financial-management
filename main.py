import tkinter as tk
root = tk.Tk()
lable = tk.Label(root, text="This is our project")
lable.pack(padx=90, pady=90)

menu = tk.Menu(root)


def get_transactions():
    file = open("transactions.csv", "r")
    data = file.readlines()
    file.close()
    data = [i.strip().split(",") for i in data]
    return data


def edit_transaction(id):
    print("edit", id)

def delete_transaction(id):
    print("delete", id)

def view_transaction():
    data = get_transactions()
    transactions_window = tk.Toplevel()
    height = len(data)
    width = len(data[0])
    for i in range(height):
        for j in range(width):
            b = tk.Label(transactions_window, text=data[i][j], anchor="nw", width=10, padx=10, pady= 2, bd=.5, relief="solid" )
            b.grid(row=i, column=j)
        if i != 0:
            editbutton = tk.Button(transactions_window, text="edit", command=lambda i=i: edit_transaction(i))
            editbutton.grid(row=i, column=j+1)
            deletbutton = tk.Button(transactions_window, text="delete", command=lambda i=i: delete_transaction(i))
            deletbutton.grid(row=i, column=j+2)



transactions = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="transaction", menu=transactions)
transactions.add_command(label="view transaction", command=view_transaction)


root.config(menu=menu)
root.mainloop()