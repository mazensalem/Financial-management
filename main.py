import tkinter as tk
from transactions import view_transaction, create_edit_window
from report import ask_date_view, set_initial_balance
from products import view_products, create_edit_windowp

root = tk.Tk()
lable = tk.Label(root, text="This is our project")
lable.pack(padx=90, pady=90)

menu = tk.Menu(root)

transactions = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="transaction", menu=transactions)
transactions.add_command(label="view transaction", command=view_transaction)
transactions.add_command(label="create transaction", command=lambda:create_edit_window(None))


products = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="products", menu=products)
products.add_command(label="view products", command=view_products)
products.add_command(label="create product", command=lambda:create_edit_windowp(None))


report = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="report", menu=report)
report.add_command(label="generate report", command=ask_date_view)
report.add_command(label="set initial balance", command=set_initial_balance)


root.config(menu=menu)
root.mainloop()
