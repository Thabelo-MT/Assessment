import sqlite3
from tkinter import messagebox
#Create a message box and assign values for username and password

def login():
    db=sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    db.execute("Insert into login(username, password) VALUES('Tom', '12dee')")
    db.execute("Insert into login(username, password) VALUES('Kyle', 'K@yle')")
    db.execute("Insert into login(username, password) VALUES('cas', 'ca22')")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", (userinput.get(), passwordinput.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login success')
    else:
        messagebox.showinfo('info', 'login failed, please try again')
    cursor.connection.commit()
    db.close()
        
main_window=tkinter.Tk()
main_window.title('Login Form')
main_window.geometry('450x300')

info_label=tkinter.Label(main_window, text='Login Form')
info_label.grid(row=0, column=0)
#For username
info_user=tkinter.Label(main_window, text='Username')
info_user.grid(row=1, column=0)
userinput=tkinter.Entry()
userinput.grid(row=1, column=1)
#For password
info_password=tkinter.Label(main_window, text='Password')
info_password.grid(row=2, column=0)
passwordinput=tkinter.Entry()
passwordinput.grid(row=2, column=1)
#Add Login button
login_btn=tkinter.Button(main_windowtext='Login', command=login())
login_btn.grid(row=3, column=1)


main_window.mainloop()