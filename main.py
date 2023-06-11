#import modules
 
from tkinter import *
import os
from PIL import Image, ImageTk
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    # register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("576x384")

    
    #  # Load the background image
    image = Image.open(r'C:\Users\vigo4\Desktop\Projects\My Python quickies\Tkinter\tkinter-GUI-login\pexels-jessica-lewis-creative-583847.jpg')  # Replace "background_image.jpg" with your image path
    image = image.resize((576, 384), Image.ANTIALIAS)  # Adjust the size of the image to fit the window
    background_image = ImageTk.PhotoImage(image)

    background_label = Label(register_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Sign Up with us!", width="300", height="2", font=("Calibri", 13), ).pack()

    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.geometry("576x384")
    login_screen.title("Login")


         # Load the background image
    image = Image.open(r'C:\Users\vigo4\Desktop\Projects\My Python quickies\Tkinter\tkinter-GUI-login\pexels-jessica-lewis-creative-583847.jpg') # Replace "background_image.jpg" with your image path
    image = image.resize((576, 384), Image.ANTIALIAS)  # Adjust the size of the image to fit the window
    background_image = ImageTk.PhotoImage(image)

    background_label = Label(login_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    Label(login_screen, text="Please Login", width="300", height="2", font=("Calibri", 13), ).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()




 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry



    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("576x384")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
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
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()
 
 
main_account_screen()
