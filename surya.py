# import mysql.connector
# from mysql.connector import Error
# from datetime import date
# from tkinter import *

# # Connect to the database
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='mydatabase',
#                                          user='myusername',
#                                          password='mypassword')

#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)

# # Create the table if it doesn't exist
# cursor.execute('''CREATE TABLE IF NOT EXISTS daily_survey
#              (id INT AUTO_INCREMENT PRIMARY KEY,
#               date DATE,
#               amount FLOAT,
#               recipient VARCHAR(255))''')

# # Define a function to insert the data
# def insert_data(date, amount, recipient):
#     try:
#         # Insert the data into the database
#         cursor.execute("INSERT INTO daily_survey (date, amount, recipient) VALUES (%s, %s, %s)", (date, amount, recipient))
#         connection.commit()
#         print(cursor.rowcount, "Record inserted successfully into daily_survey table")

#     except mysql.connector.Error as error:
#         print("Failed to insert record into daily_survey table {}".format(error))

# # Define a function to get the data from the UI and insert it into the database
# def submit_data():
#     date_str = date_entry.get()
#     amount = float(amount_entry.get())
#     recipient = recipient_entry.get()
#     date_obj = date.fromisoformat(date_str)
#     insert_data(date_obj, amount, recipient)

#     # Clear the UI
#     date_entry.delete(0, END)
#     amount_entry.delete(0, END)
#     recipient_entry.delete(0, END)

# # Set up the UI
# root = Tk()
# root.title("Daily Survey")

# date_label = Label(root, text="Date (YYYY-MM-DD):")
# date_label.pack()
# date_entry = Entry(root)
# date_entry.pack()

# amount_label = Label(root, text="Amount:")
# amount_label.pack()
# amount_entry = Entry(root)
# amount_entry.pack()

# recipient_label = Label(root, text="Recipient:")
# recipient_label.pack()
# recipient_entry = Entry(root)
# recipient_entry.pack()

# submit_button = Button(root, text="Submit", command=submit_data)
# submit_button.pack()

# root.mainloop()
import seaborn as sns