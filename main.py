import tkinter as tk
from transactions import view_transaction

root = tk.Tk()
lable = tk.Label(root, text="This is our project")
lable.pack(padx=90, pady=90)

menu = tk.Menu(root)


transactions = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="transaction", menu=transactions)
transactions.add_command(label="view transaction", command=view_transaction)


root.config(menu=menu)
root.mainloop()
