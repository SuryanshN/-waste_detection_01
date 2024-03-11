# # def rev(a,s,e):
# #     if(s>=e):
# #         return
# #     a[s],a[e]=a[e],a[s]
# #     return rev(a,s+1,e-1)

# def kth(a,k):
#     l=[]
#     l.append(a[k])
#     return l

# a=[1,5,6,7,8]
# s=0
# e=len(a)
# print(a)
# rev(a,s+1,e-1)
# print(a)
import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS daily_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              amount REAL,
              recipient TEXT)''')

class DailyDataUI:
    def __init__(self, master):
        self.master = master
        master.title("Daily Data")

        # Add UI elements
        self.date_label = tk.Label(master, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(master)
        self.date_entry.pack()

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.recipient_label = tk.Label(master, text="Recipient:")
        self.recipient_label.pack()
        self.recipient_entry = tk.Entry(master)
        self.recipient_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        # Get the data from the UI
        date = self.date_entry.get()
        amount = float(self.amount_entry.get())
        recipient = self.recipient_entry.get()

        # Insert the data into the database
        c.execute("INSERT INTO daily_data (date, amount, recipient) VALUES (?, ?, ?)", (date, amount, recipient))
        conn.commit()

        # Clear the UI
        self.date_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)

root = tk.Tk()
daily_data_ui = DailyDataUI(root)
root.mainloop()
