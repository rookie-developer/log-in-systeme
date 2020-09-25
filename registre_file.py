from tkinter import *
import tkinter as tk
import os
from PIL import Image,ImageTk

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def login_sucess():
  global screen3
  screen3 = Toplevel(root)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(root)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(root)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    entry1.delete(0,END)
    entry2.delete(0,END)

    suclabel = tk.Label(screen,text="regestration succesfull",fg="green")
    suclabel.pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  user.delete(0, END)
  Password.delete(0, END)

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

def Register():

    global screen

    screen = Toplevel(root)
    screen.title("registration")
    screen.geometry("400x240")

    global username
    global password
    global entry1
    global entry2

    username = StringVar()
    password = StringVar()

    label1 = tk.Label(screen,text="username :")
    label1.place(relx="0.2",rely="0.25")

    entry1 = tk.Entry(screen,textvariable = username)
    entry1.place(relx="0.4",rely="0.25")

    label2 = tk.Label(screen,text="password :")
    label2.place(relx="0.2",rely="0.35")

    entry2 = tk.Entry(screen,textvariable = password)
    entry2.place(relx="0.4",rely="0.35")

    button = tk.Button(screen, text = "register",fg="#1a53ff",bg="black",command = register_user)
    button.place(relwidth="0.2",relheight="0.2",relx="0.45",rely="0.5")

global root

root = tk.Tk()

background_image = ImageTk.PhotoImage(Image.open('cyber.png'))
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth='1',relheight='1',x=0,y=0)

global user_verify
global Password_verify
global user
global Password

username_verify = StringVar()
password_verify = StringVar()


root.geometry("600x400")
root.title("register file")

User = tk.Label(root,text="username :")
User.place(relx="0.28",rely="0.2")

user = tk.Entry(root, textvariable = username_verify)
user.place(relwidth="0.2",relx="0.4",rely="0.2")

password = tk.Label(root,text="password :")
password.place(relx="0.28",rely="0.3")

Password = tk.Entry(root, textvariable = password_verify)
Password.place(relwidth="0.2",relx="0.4",rely="0.3")

login = tk.Button(root,text="Login",fg="#1a53ff",bg="black" ,command = login_verify)
login.place(relwidth="0.1",relheight="0.1",relx="0.45",rely="0.4")

labelx = tk.Label(root,text="if you don't have an account \ncreate one",bg="#DCD3C5")
labelx.place(relx="0.36",rely="0.52")

register = tk.Button(root,text="register",fg="#1a53ff",bg="black", command = Register)
register.place(relwidth="0.2",relheight="0.1",relx="0.4",rely="0.62")

root.mainloop()