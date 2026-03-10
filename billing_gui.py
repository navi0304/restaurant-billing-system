import tkinter as tk

items = [
    ("Samosa",10),
    ("Aloo Tikki",15),
    ("Bun Samosa",35),
    ("Oreo Milkshake",80),
    ("Fresh Lime Soda",15),
    ("Veg Burger",50),
    ("French Fries",40),
    ("Cold Coffee",60),
    ("Chocolate Milkshake",70),
    ("Pizza Slice",80)
]

entries = []

def calculate_bill():

    bill_text.delete("1.0", tk.END)

    bill_text.insert(tk.END,"------ RESTAURANT BILL ------\n\n")
    bill_text.insert(tk.END,"Item\t\tQty\tPrice\n")
    bill_text.insert(tk.END,"--------------------------------\n")

    total = 0

    for i in range(len(items)):

        qty = entries[i].get()

        if qty != "":
            qty = int(qty)

            name = items[i][0]
            price = items[i][1]

            item_total = qty * price
            total += item_total

            bill_text.insert(
                tk.END,
                f"{name}\t\t{qty}\tRs.{item_total}\n"
            )

    bill_text.insert(tk.END,"--------------------------------\n")
    bill_text.insert(tk.END,f"TOTAL BILL\t\tRs.{total}")


def reset_fields():

    for entry in entries:
        entry.delete(0, tk.END)

    bill_text.delete("1.0", tk.END)


window = tk.Tk()
window.title("Restaurant Billing System")
window.geometry("450x500")

title = tk.Label(window,text="Restaurant Billing System",font=("Arial",18))
title.pack(pady=10)

menu_frame = tk.Frame(window)
menu_frame.pack()

for i in range(len(items)):

    name = items[i][0]
    price = items[i][1]

    label = tk.Label(menu_frame,text=f"{name} (Rs.{price})",width=25,anchor="w")
    label.grid(row=i,column=0,padx=10,pady=5)

    entry = tk.Entry(menu_frame,width=5)
    entry.grid(row=i,column=1)

    entries.append(entry)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

calc_btn = tk.Button(button_frame,text="Calculate Bill",command=calculate_bill)
calc_btn.grid(row=0,column=0,padx=10)

reset_btn = tk.Button(button_frame,text="Reset",command=reset_fields)
reset_btn.grid(row=0,column=1,padx=10)


bill_text = tk.Text(window,height=10,width=40)
bill_text.pack(pady=10)

window.mainloop()