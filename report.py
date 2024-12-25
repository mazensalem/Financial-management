import tkinter as tk
from transactions import is_float, get_balance, get_transactions
from pdfhandler import savepdf
import tkinter.messagebox
from tkcalendar import DateEntry


def date1_greater(data1, data2):
    if int(data1[0]) > int(data2[0]):
        return True
    if int(data1[0]) < int(data2[0]):
        return False
    
    if int(data1[1]) > int(data2[1]):
        return True
    if int(data1[1]) < int(data2[1]):
        return False
    
    if int(data1[2]) > int(data2[2]):
        return True
    if int(data1[2]) < int(data2[2]):
        return False
    
    return "equal"

def generate_report_view(start, end, select_date_window):
    select_date_window.destroy()
    report_window = tk.Toplevel()
    if not date1_greater(str(end).split("-"), str(start).split("-")):
        tkinter.messagebox.showerror("Error", "The start must be before the end")
        ask_date_view()
        return
    data = get_transactions()
    total_spend = 0
    total_gained = 0
    count_transaction = 0
    for row in data:
        if len(row[1].split("/")) > 1:
            count_transaction += 1
            date = row[1].split("/")
            date.reverse()
            if row[2] == "buying":
                total_spend += float(row[3])
            else:
                total_gained += float(row[3])
    
    Ldate = tk.Label(report_window, text=f"From {str(start)} to {str(end)} you did {count_transaction} transactions")
    Lprofit = tk.Label(report_window, text=f"the total profit you achieved was {total_gained - total_spend}")
    Lgained = tk.Label(report_window, text=f"the total revenue you achieved was {total_gained}")
    Lspend = tk.Label(report_window, text=f"the total spending you achieved was {total_spend}")
    # Bexp = tk.Button(report_window, text="export to pdf", command=lambda : savepdf(str(start), str(end), total_gained, total_spend, count_transaction))
    Ldate.grid(row=0)
    Lprofit.grid(row=1)
    Lgained.grid(row=2)
    Lspend.grid(row=3)
    # Bexp.grid(row=4)

    
    report_window.mainloop()
    

def ask_date_view():
    select_date_window = tk.Toplevel()

    L1 = tk.Label(select_date_window, text="Enter the start date")
    L2 = tk.Label(select_date_window, text="Enter the end date")
    D1 = DateEntry(select_date_window)
    D2 = DateEntry(select_date_window)

    B = tk.Button(select_date_window, text="Generate", command=lambda : generate_report_view(D1.get_date(), D2.get_date(), select_date_window))

    L1.grid(row=0, column=0)
    L2.grid(row=1, column=0)
    D1.grid(row=0, column=1)
    D2.grid(row=1, column=1)
    B.grid(row=2, column=1)


    select_date_window.mainloop()



def set_initial_balance():
    window = tk.Toplevel()
    balance = tk.StringVar()

    def set_balance_file():
        if is_float(balance.get()):
            data = get_balance()
            file = open("balance.txt", "w")
            file.write(balance.get() + "," + str(data[1]))
            file.close()
            tkinter.messagebox.showinfo("Info", f"you have set the initial balance to {balance.get()}", parent=window)
            window.destroy()
        else:
            tkinter.messagebox.showerror("Error", "you have to enter a number", parent=window)
            

    L = tk.Label(window, text="Enter the initial balance: ")
    E = tk.Entry(window, textvariable=balance)
    B = tk.Button(window, text="Set", command=set_balance_file)
    L.grid(row=0, column=0)
    E.grid(row=0, column=2)
    B.grid(row=1, column=2)
    window.mainloop()