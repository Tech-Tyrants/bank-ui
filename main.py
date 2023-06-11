#import modules
 
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import messagebox

 


def dashboard():
    global dashboard_screen
    dashboard_screen = Tk()
    dashboard_screen.title("Bank App Dashboard")
    dashboard_screen.geometry("576x384")


    # Create the labels
    balance_label = Label(dashboard_screen, text="Current Balance:", font=("Arial", 14)).pack()

    current_balance_label = Label(dashboard_screen, text="", font=("Arial", 18, "bold"))
    current_balance_label.pack()
    current_balance_label['text'] = "0"


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
        withdraw_button = Button(withdraw_window, text="Withdraw", font=("Arial", 12), command=lambda: process_withdrawal_savings(amount_entry.get(), withdraw_window))
        withdraw_button.pack(pady=10)

    def process_withdrawal_savings(amount, window):
        try:
            withdrawal_amount = float(amount)
            if float(current_balance_label.cget("text")) == 0 or withdrawal_amount > float(current_balance_label.cget("text")):
                # self.current_balance_label['text'] = "Insufficient funds"
                messagebox.showerror("Error", "Insufficient funds")
            elif withdrawal_amount > 5000:
                messagebox.showinfo("Limit Exceeded", "You have exceeded the limit of 5000 per day")
            else:
                current_balance_label['text'] = float(current_balance_label.cget("text")) - withdrawal_amount
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

    def process_withdrawal(amount, window):
        try:
            withdrawal_amount = float(amount)
            if float(current_balance_label.cget("text")) == 0 or withdrawal_amount > float(current_balance_label.cget("text")):
                # self.current_balance_label['text'] = "Insufficient funds"
                messagebox.showerror("Error", "Insufficient funds")
            else:
                current_balance_label['text'] = float(current_balance_label.cget("text")) - withdrawal_amount
                window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

    def process_deposit(amount, window):
        try:
            deposit_amount = float(amount)
            current_balance_label['text'] = float(current_balance_label.cget('text')) + deposit_amount
            window.destroy()
        except:
            messagebox.showerror("Error", "Invalid Deposit amount")
            window.destroy()


    # dashboard_screen.messagebox.showinfo("Welcome to Bank app", "Deposit at least 1000 to get started with your account")
# Create the withdraw button
    withdraw_button = Button(dashboard_screen, text="Withdraw", font=("Arial", 12), command=confirm_account_type)
    withdraw_button.pack(pady=10)
    #Deposit button
    deposit_button = Button(dashboard_screen, text="Deposit", font=("Arial", 12), command=deposit_funds)
    deposit_button.pack()
    
    

 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("576x384")
    main_screen.title("Account Login")
    # Load the background image
    image = Image.open(r'C:\Users\vigo4\Desktop\Projects\My Python quickies\Tkinter\tkinter-GUI-login\pexels-jessica-lewis-creative-583847.jpg')  # Replace "background_image.jpg" with your image path
    image = image.resize((576, 384), Image.ANTIALIAS)  # Adjust the size of the image to fit the window
    background_image = ImageTk.PhotoImage(image)

    background_label = Label(main_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(text="Welcome to your Bank App", width="300", height="2", font=("Calibri", 13), ).pack()
    
    Label(text="").pack()
    Label(text="", bg="black").pack()
    Label(text="", bg="black").pack()
    Label(text="", bg="black").pack()
    Label(text="", bg="black").pack()
    # Button(text="Login", height="2", width="30", command = login).pack()
    # Label(text="").pack()
    Button(text="Get Started", height="2", width="30", command=dashboard).pack()
    main_screen.mainloop()
 
 
main_account_screen()
