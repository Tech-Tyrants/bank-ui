# from main import main_screen
from tkinter import *
from tkinter import messagebox



def confirm_account_type():
    global confirm_window
    confirm_window = Tk()
    confirm_window.title("Confirm Account Type")
    confirm_window.geometry("576x384")
    clicked = StringVar()
    account_type_label = Label(confirm_window, text="Confirm Your Accout Type Below")
    account_type_label.pack()
    main_menu = OptionMenu(confirm_window, clicked, "Currents", "Savings")
    main_menu.pack()
    def get_option():
        selected_option = clicked.get()
        print("Selected option is: ", selected_option)
        if selected_option == "Savings":
            withdraw_savings()
        else:
            withdraw_funds()
    confirm_button = Button(confirm_window, text="Continue", command=get_option)
    confirm_button.pack(pady=5)

def withdraw_savings():
    withdraw_window = Tk()
    withdraw_window.title("Withdraw Funds")
    withdraw_window.geometry("576x384")
    amount_label = Label(withdraw_window, text="Withdrawal amount: ", font=("Arial", 12))
    amount_label.pack()
    amount_entry = Entry(withdraw_window, font=("Arial", 12))
    amount_entry.pack()
    withdraw_button = Button(withdraw_window, text="Withdraw", font=("Arial", 12), command=lambda: self.process_withdrawal_savings(amount_entry.get(), withdraw_window))
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

def deposit_funds():
    deposit_window =Tk()
    deposit_window.title("Deposit Funds")
    deposit_window.geometry("576x384")
    amount_label =Label(deposit_window, text="Deposit Amount:", font=("Arial", 12))
    amount_label.pack()

    amount_entry =Entry(deposit_window, font=("Arial", 12))
    amount_entry.pack()

    deposit_button =Button(deposit_window, text="Deposit", font=("Arial", 12), command=lambda: process_deposit(amount_entry.get(), deposit_window))
    deposit_button.pack(pady=10)

def withdraw_funds():
    # Create a new window for the withdrawal form
    withdraw_window =Tk()
    withdraw_window.title("Withdraw Funds")
    withdraw_window.geometry("576x384")

    # Create the label and entry for the withdrawal amount
    amount_label =Label(withdraw_window, text="Withdraw Amount:", font=("Arial", 12))
    amount_label.pack()

    amount_entry =Entry(withdraw_window, font=("Arial", 12))
    amount_entry.pack()

    # Create the withdraw button in the withdrawal window
    withdraw_button =Button(withdraw_window, text="Withdraw", font=("Arial", 12), command=lambda: process_withdrawal(amount_entry.get(), withdraw_window))
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

def process_deposit(amount, window):
    try:
        deposit_amount = float(amount)
        current_balance_label['text'] = float(self.current_balance_label.cget('text')) + deposit_amount
        window.destroy()
    except:
        messagebox.showerror("Error", "Invalid Deposit amount")
        window.destroy()


