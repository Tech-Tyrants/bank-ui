import tkinter as tk
from tkinter import messagebox

class FinanceAppDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance App Dashboard")
        self.geometry("700x500")

        # Create the main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=40)

        # Create the labels
        balance_label = tk.Label(self.main_frame, text="Current Balance:", font=("Arial", 14))
        balance_label.pack()

        self.current_balance_label = tk.Label(self.main_frame, text="$1000", font=("Arial", 18, "bold"))
        self.current_balance_label.pack()

        # Create the withdraw button
        withdraw_button = tk.Button(self.main_frame, text="Withdraw", font=("Arial", 12), command=self.withdraw_funds)
        withdraw_button.pack(pady=10)
        #Deposit button
        deposit_button = tk.Button(self.main_frame, text="Deposit", font=("Arial", 12), command=self.deposit_funds)
        deposit_button.pack()

    def deposit_funds(self):
        deposit_window = tk.Toplevel(self)
        deposit_window.title("Deposit Funds")
        deposit_window.geometry("350x250")
        amount_label = tk.Label(deposit_window, text="Deposit Amount:",font=("Arial", 12))
        amount_label.pack()

        amount_entry = tk.Entry(deposit_window, font=("Arial", 12))
        amount_entry.pack()

    def withdraw_funds(self):
        # Create a new window for the withdrawal form
        withdraw_window = tk.Toplevel(self)
        withdraw_window.title("Withdraw Funds")
        withdraw_window.geometry("250x150")

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
            # Perform the withdrawal logic here

            self.current_balance_label.config(text=f"${self.current_balance}")  # Update the balance label
            window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

# Create an instance of the finance app dashboard
app = FinanceAppDashboard()

# Start the main event loop
app.mainloop()
