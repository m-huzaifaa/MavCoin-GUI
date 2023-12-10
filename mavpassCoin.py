import tkinter as tk
from tkinter import messagebox
import json

# Load existing data from the file
try:
    with open("student_accounts.json", "r") as file:
        student_accounts = json.load(file)
except FileNotFoundError:
    student_accounts = {}

def save_data():
    # Save the data to the file
    with open("student_accounts.json", "w") as file:
        json.dump(student_accounts, file)

def add_coin():
    student_id = entry_id.get()
    if student_id:
        if student_id in student_accounts:
            student_accounts[student_id] += 1
        else:
            student_accounts[student_id] = 1
        save_data()
        messagebox.showinfo("Success", "Coin added to the account.")
    else:
        messagebox.showerror("Error", "Please enter a student ID.")

def redeem_coins():
    student_id = entry_id.get()
    if student_id:
        if student_id in student_accounts and student_accounts[student_id] >= 2:
            student_accounts[student_id] -= 2
            save_data()
            messagebox.showinfo("Success", "Coins redeemed.")
        else:
            messagebox.showerror("Error", "Not enough coins to redeem.")
    else:
        messagebox.showerror("Error", "Please enter a student ID.")

def lucky_draw():
    import random
    student_id = entry_id.get()
    if student_id:
        if student_id in student_accounts:
            # Simulate a lucky draw
            if random.randint(0, 1) == 0:
                student_accounts[student_id] += 2
                save_data()
                messagebox.showinfo("Lucky Draw", "You won! You earned two more coins.")
            else:
                student_accounts[student_id] -= 2
                save_data()
                messagebox.showinfo("Lucky Draw", "You lost. 2 coins deducted.")
        else:
            messagebox.showerror("Error", "Student not found.")
    else:
        messagebox.showerror("Error", "Please enter a student ID.")

def check_balance():
    student_id = entry_id.get()
    if student_id:
        if student_id in student_accounts:
            balance_label.config(text=f"Account balance: {student_accounts[student_id]}")
        else:
            messagebox.showerror("Error", "Student not found.")
            balance_label.config(text="Account balance: N/A")
    else:
        messagebox.showerror("Error", "Please enter a student ID.")
        balance_label.config(text="Account balance: N/A")

# Creating the main window
root = tk.Tk()
root.title("MavPASS Coin Management")

# Creating and configuring GUI components
root.geometry("400x250")  # Setting the window size

label_id = tk.Label(root, text="Enter Student ID:")
entry_id = tk.Entry(root)
add_button = tk.Button(root, text="Add 1 Coin", command=add_coin, width=20)
redeem_button = tk.Button(root, text="Redeem Coins (2 coins = 1 pt)", command=redeem_coins, width=20)
lucky_draw_button = tk.Button(root, text="Lucky Draw (2 coins)", command=lucky_draw, width=20)
balance_button = tk.Button(root, text="Check Balance", command=check_balance, width=20)
balance_label = tk.Label(root, text="Account balance: N/A", font=("Helvetica", 12))

# Placing GUI components in the window
label_id.pack(pady=10)
entry_id.pack()
add_button.pack(pady=5)
redeem_button.pack(pady=5)
lucky_draw_button.pack(pady=5)
balance_button.pack(pady=5)
balance_label.pack(pady=10)

# Starting the Tkinter main loop
root.mainloop()
