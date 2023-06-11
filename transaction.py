import tkinter as tk
from tkinter import *
from tkinter import messagebox

class BankAppDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank App Dashboard")
        self.geometry("700x500")

        # Create the main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=40)

        # Create the labels
        balance_label = tk.Label(self.main_frame, text="Current Balance:", font=("Arial", 14))
        balance_label.pack()

        self.current_balance_label = tk.Label(self.main_frame, text="", font=("Arial", 18, "bold"))
        self.current_balance_label.pack()
        self.current_balance_label['text'] = "0"

        # self.get_started_label = tk.Label(self.main_frame, text="", font=("Arial", 12))
        # self.get_started_label.pack()
        # self.get_started_label = ""
        messagebox.showinfo("Welcome to Bank app", "Deposit at least 1000 to get started with your account")

        # Create the withdraw button
        withdraw_button = tk.Button(self.main_frame, text="Withdraw", font=("Arial", 12), command=self.confirm_account_type)
        withdraw_button.pack(pady=10)
        #Deposit button
        deposit_button = tk.Button(self.main_frame, text="Deposit", font=("Arial", 12), command=self.deposit_funds)
        deposit_button.pack()

    def confirm_account_type(self):
        confirm_window = tk.Toplevel(self)
        confirm_window.title("Confirm Account Type")
        confirm_window.geometry("350x250")
        clicked = StringVar()
        account_type_label = tk.Label(confirm_window, text="Confirm Your Accout Type Below")
        account_type_label.pack()
        main_menu = OptionMenu(confirm_window, clicked, "Currents", "Savings")
        main_menu.pack()
        def get_option():
            selected_option = clicked.get()
            # print("Selected option is: ", selected_option)
            if selected_option == "Savings":
                self.withdraw_savings()
            else:
                self.withdraw_funds()
        confirm_button = tk.Button(confirm_window, text="Continue", command=get_option)
        confirm_button.pack(pady=5)

    def withdraw_savings(self):
        withdraw_window = tk.Toplevel(self)
        withdraw_window.title("Withdraw Funds")
        withdraw_window.geometry("350x250")
        amount_label = tk.Label(withdraw_window, text="Withdrawal amount: ", font=("Arial", 12))
        amount_label.pack()
        amount_entry = tk.Entry(withdraw_window, font=("Arial", 12))
        amount_entry.pack()
        withdraw_button = tk.Button(withdraw_window, text="Withdraw", font=("Arial", 12), command=lambda: self.process_withdrawal_savings(amount_entry.get(), withdraw_window))
        withdraw_button.pack(pady=10)

    def process_withdrawal_savings(self, amount, window):
        try:
            withdrawal_amount = float(amount)
            if float(self.current_balance_label.cget("text")) == 0 or withdrawal_amount > float(self.current_balance_label.cget("text")):
                # self.current_balance_label['text'] = "Insufficient funds"
                messagebox.showerror("Error", "Insufficient funds")
            elif withdrawal_amount > 5000:
                messagebox.showinfo("Limit Exceeded", "You have exceeded the limit of 5000 per day")
            else:
                self.current_balance_label['text'] = float(self.current_balance_label.cget("text")) - withdrawal_amount
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

    def deposit_funds(self):
        deposit_window = tk.Toplevel(self)
        deposit_window.title("Deposit Funds")
        deposit_window.geometry("350x250")
        amount_label = tk.Label(deposit_window, text="Deposit Amount:", font=("Arial", 12))
        amount_label.pack()

        amount_entry = tk.Entry(deposit_window, font=("Arial", 12))
        amount_entry.pack()

        deposit_button = tk.Button(deposit_window, text="Deposit", font=("Arial", 12), command=lambda: self.process_deposit(amount_entry.get(), deposit_window))
        deposit_button.pack(pady=10)

    def withdraw_funds(self):
        # Create a new window for the withdrawal form
        withdraw_window = tk.Toplevel(self)
        withdraw_window.title("Withdraw Funds")
        withdraw_window.geometry("350x250")

        # Create the label and entry for the withdrawal amount
        amount_label = tk.Label(withdraw_window, text="Withdraw Amount:", font=("Arial", 12))
        amount_label.pack()

        amount_entry = tk.Entry(withdraw_window, font=("Arial", 12))
        amount_entry.pack()

        # Create the withdraw button in the withdrawal window
        withdraw_button = tk.Button(withdraw_window, text="Withdraw", font=("Arial", 12), command=lambda: self.process_withdrawal(amount_entry.get(), withdraw_window))
        withdraw_button.pack(pady=10)

    def process_withdrawal(self, amount, window):
        try:
            withdrawal_amount = float(amount)
            if float(self.current_balance_label.cget("text")) == 0 or withdrawal_amount > float(self.current_balance_label.cget("text")):
                # self.current_balance_label['text'] = "Insufficient funds"
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.current_balance_label['text'] = float(self.current_balance_label.cget("text")) - withdrawal_amount
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

    def process_deposit(self, amount, window):
        try:
            deposit_amount = float(amount)
            self.current_balance_label['text'] = float(self.current_balance_label.cget('text')) + deposit_amount
            window.destroy()
        except:
            messagebox.showerror("Error", "Invalid Deposit amount")
            window.destroy()

# Create an instance of the finance app dashboard
app = BankAppDashboard()

# Start the main event loop
app.mainloop()
