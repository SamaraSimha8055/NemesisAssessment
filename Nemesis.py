from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Nemesis Login Form")

width = 1280
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
EMAIL = StringVar()
PHONE = StringVar()
ADDRESS = StringVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username "
                   "TEXT, password TEXT, firstname TEXT, lastname TEXT, email EMAIL, phone TEXT, address TEXT)")


def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()


def ToggleToLoginForm(event=None):
    UpdateFrame.destroy()
    LoginForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def ToggleToUpdate(event=None):
    ProfileFrame.destroy()
    UpdateForm()


def ToggleToUpdateForm(event=None):
    UpdateFrame.destroy()
    ProfileForm()


def ToggleToProfile(event=None):
    UpdateFrame.destroy()
    ProfileForm()


def ToggleToProfileForm(event=None):
    LoginFrame.destroy()
    ProfileForm()


def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=10)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_email = Label(RegisterFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)
    lbl_phone = Label(RegisterFrame, text="Phone no:", font=('arial', 18), bd=18)
    lbl_phone.grid(row=6)
    lbl_address = Label(RegisterFrame, text="Address:", font=('arial', 18), bd=18)
    lbl_address.grid(row=7)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=8, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    email = Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)
    phone = Entry(RegisterFrame, font=('arial', 20), textvariable=PHONE, width=15)
    phone.grid(row=6, column=1)
    address = Entry(RegisterFrame, font=('arial', 20), textvariable=ADDRESS, width=15)
    address.grid(row=7, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=9, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)


def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "" or EMAIL.get == "" or PHONE.get == "" or ADDRESS.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `email` = ?", (EMAIL.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Email is already taken", fg="red")
        else:
            cursor.execute(
                "INSERT INTO `member` (username, password, firstname, lastname, email, phone, address) VALUES(?, ?, ?, ?, ?, ?, ?)",
                (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get()),
                 str(EMAIL.get()), str(PHONE.get()), str(ADDRESS.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            EMAIL.set("")
            PHONE.set("")
            ADDRESS.set("")
            lbl_result2.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_email = Label(LoginFrame, text="Email:", font=('arial', 25), bd=18)
    lbl_email.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    email = Entry(LoginFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)


def Login():
    Database()
    if EMAIL.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `email` = ? and `password` = ?", (EMAIL.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            root.after(1000, reduce_time_out)
            ToggleToProfileForm()
            menubar.entryconfig("Edit", state="normal")
            menubar.entryconfig("Log out", state="normal")



        else:
            lbl_result1.config(text="Invalid Email or password", fg="red")


LoginForm()


def ProfileForm():
    Database()
    global ProfileFrame, lbl_result5
    ProfileFrame = Frame(root)
    ProfileFrame.pack(side=TOP, pady=80)
    lbl_username = Label(ProfileFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(ProfileFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(ProfileFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(ProfileFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_email = Label(ProfileFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)
    lbl_phone = Label(ProfileFrame, text="Phone no:", font=('arial', 18), bd=18)
    lbl_phone.grid(row=6)
    lbl_address = Label(ProfileFrame, text="Address:", font=('arial', 18), bd=18)
    lbl_address.grid(row=7)
    username = Entry(ProfileFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(ProfileFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    password.grid(row=2, column=1)
    firstname = Entry(ProfileFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(ProfileFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    email = Entry(ProfileFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)
    phone = Entry(ProfileFrame, font=('arial', 20), textvariable=PHONE, width=15)
    phone.grid(row=6, column=1)
    address = Entry(ProfileFrame, font=('arial', 20), textvariable=ADDRESS, width=15)
    address.grid(row=7, column=1)

    conn.commit()
    cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
    USERNAME.set(username)
    PASSWORD.set(password)
    FIRSTNAME.set(firstname)
    LASTNAME.set(lastname)
    EMAIL.set(email)
    PHONE.set(phone)
    ADDRESS.set(address)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

    root.bind_all("<Any-KeyPress>", reset_timer)
    root.bind_all("<Any-ButtonPress>", reset_timer)
    root.after(120000, Logoutpack)


def UpdateForm():
    global UpdateFrame, lbl_result6
    UpdateFrame = Frame(root)
    UpdateFrame.pack(side=TOP, pady=80)
    lbl_username = Label(UpdateFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(UpdateFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(UpdateFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(UpdateFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_email = Label(UpdateFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)
    lbl_phone = Label(UpdateFrame, text="Phone no:", font=('arial', 18), bd=18)
    lbl_phone.grid(row=6)
    lbl_address = Label(UpdateFrame, text="Address:", font=('arial', 18), bd=18)
    lbl_address.grid(row=7)
    lbl_result4 = Label(UpdateFrame, text="", font=('arial', 18))
    lbl_result4.grid(row=7, columnspan=2)
    username = Entry(UpdateFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(UpdateFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    password.grid(row=2, column=1)
    firstname = Entry(UpdateFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(UpdateFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    email = Entry(UpdateFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)
    phone = Entry(UpdateFrame, font=('arial', 20), textvariable=PHONE, width=15)
    phone.grid(row=6, column=1)
    address = Entry(UpdateFrame, font=('arial', 20), textvariable=ADDRESS, width=15)
    address.grid(row=7, column=1)
    btn_update = Button(UpdateFrame, text="Update", font=('arial', 18), width=35, command=Update)
    btn_update.grid(row=9, columnspan=2, pady=20)
    menubar.entryconfig("Log out", state="disabled")


def Update():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "" or EMAIL.get == "" or PHONE.get == "" or ADDRESS.get == "":
        lbl_result5.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `email` = ?", (EMAIL.get(),))

        cursor.execute("INSERT INTO `member` (username, password, firstname, lastname, email, phone, address) VALUES("
                       "?, ?, ?, ?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get()),str(EMAIL.get()), str(PHONE.get()), str(ADDRESS.get())))
        conn.commit()
        USERNAME.set("")
        PASSWORD.set("")
        FIRSTNAME.set("")
        LASTNAME.set("")
        EMAIL.set("")
        PHONE.set("")
        ADDRESS.set("")
    cursor.close()
    conn.close()
    menubar.entryconfig("Log out", state="normal")
    ToggleToProfile()


def Logout():
    result = tkMessageBox.askquestion('System', 'Log out !', icon="warning")
    if result == 'yes':
        ProfileFrame.destroy()
        LoginForm()

        menubar.entryconfig("Edit", state="disabled")
        menubar.entryconfig("Log out", state="disabled")


def Logoutpack():
    ProfileFrame.destroy()
    LoginForm()

    menubar.entryconfig("Edit", state="disabled")
    menubar.entryconfig("Log out", state="disabled")


def AutoLogOut():
    UpdateFrame.destroy()
    LoginForm()
    menubar.entryconfig("Edit", state="disabled")
    menubar.entryconfig("Log out", state="disabled")


time_out = 120000


def reset_timer(event=None):
    global time_out
    if event is not None:
        time_out = 120000
    else:
        pass


def reduce_time_out():
    root.bind_all("<Any-KeyPress>", reset_timer)
    root.bind_all("<Any-ButtonPress>", reset_timer)
    global time_out
    time_out = time_out - 1000
    root.after(1000, reduce_time_out)
    if time_out == 0:
        AutoLogOut()


"""def ShowRecordForm():
    global ShowRecordFrame, lbl_result4
    ShowRecordFrame = Frame(root)
    ShowRecordFrame.pack(side=TOP, pady=80)
    lbl_username = Label(ShowRecordFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(ShowRecordFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(ShowRecordFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(ShowRecordFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_email = Label(ShowRecordFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)
    lbl_result4 = Label(ShowRecordFrame, text="", font=('arial', 18))
    lbl_result4.grid(row=7, columnspan=2)
    username = Entry(ShowRecordFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row = 1, column = 1)
    password = Entry(ShowRecordFrame, font=('arial', 20), textvariable=PASSWORD, width=15)
    password.grid(row=2, column=1)
    firstname = Entry(ShowRecordFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(ShowRecordFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    email = Entry(ShowRecordFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)
    btn_update = Button(ShowRecordFrame, text="Update", font=('arial', 18), width=35, command=ToggleToProfile)
    btn_update.grid(row=7, columnspan=2, pady=20)"""
"""def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()"""

menubar = Menu(root)

menubar.add_cascade(label="Edit", command=ToggleToUpdate, state="disabled")
menubar.add_cascade(label="Log out", command=Logout, state="disabled")
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
