from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.iconbitmap("C:/Users/dell/Pictures/Saved Pictures/library_manage.ico")
root.title("Login")
root.geometry("250x250")

my_img=ImageTk.PhotoImage(Image.open("C:/Users/dell/Pictures/Saved Pictures/library_manage.jpg"))

login_frame=Frame(root)
login_frame.pack()

my_label=Label(login_frame,image=my_img)
my_label.pack()

usernamelbl=Label(login_frame,text="username")
usernamelbl.pack()

username=Entry(login_frame)
username.pack()

passwordlbl=Label(login_frame,text="password")
passwordlbl.pack()

password=Entry(login_frame,show="*")
password.pack()

def login():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username='Monica'")
    pass_value=cur.fetchone()
    conn.commit()
    conn.close()
    if  password.get() == pass_value[0]:
        lib_manage=Toplevel()
        lib_manage.iconbitmap("C:/Users/dell/Pictures/Saved Pictures/library_manage.ico")
        lib_manage.title("Library Management System")

        
        tab_window=ttk.Notebook(lib_manage)
        root.withdraw()

        tab1=ttk.Frame(tab_window)
        tab2=ttk.Frame(tab_window)
        tab3=ttk.Frame(tab_window)

        tab_window.add(tab1,text='Add/Delete Book')
        tab_window.add(tab2,text='Borrow/Return Book')
        tab_window.pack(expand = 1, fill ="both")

        ttk.Label(tab1,text="Book_ID").grid(row=0,column=0,padx=5,pady=5)
        ttk.Entry(tab1).grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(tab1,text="Book_Name").grid(row=1,column=0,padx=5,pady=5)
        ttk.Entry(tab1).grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(tab1,text="Author_Name").grid(row=2,column=0,padx=5,pady=5)
        ttk.Entry(tab1).grid(row=2,column=1,padx=5,pady=5)
        addbkbtn = ttk.Button(tab1,text="Add Book")
        addbkbtn.grid(row=3,column=0,padx=5,pady=5)
        delbkbtn = ttk.Button(tab1,text="Delete Book")
        delbkbtn.grid(row=3,column=1,padx=5,pady=5)


        ttk.Label(tab2,text="Student_ID").grid(row=0,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Student_Name").grid(row=1,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Year").grid(row=2,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=2,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Department").grid(row=2,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=3,column=1,padx=5,pady=5)
        stbtn = ttk.Button(tab2,text="Student Details")
        stbtn.grid(row=1,column=2,padx=5,pady=5)
        
        ttk.Label(tab2,text="Book_ID").grid(row=4,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=4,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Book_Name").grid(row=5,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=5,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Author_Name").grid(row=6,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=6,column=1,padx=5,pady=5)
        bkbtn = ttk.Button(tab2,text="Book Details")
        bkbtn.grid(row=5,column=2,padx=5,pady=5)
        ttk.Label(tab2,text="Borrow_Date").grid(row=7,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=7,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Return_Date").grid(row=8,column=0,padx=5,pady=5)
        ttk.Entry(tab2).grid(row=8,column=1,padx=5,pady=5)


        brwbtn = ttk.Button(tab2,text="Borrow Book")
        brwbtn.grid(row=9,column=1,padx=5,pady=5)
        rtnbtn = ttk.Button(tab2,text="Return Book")
        rtnbtn.grid(row=9,column=2,padx=5,pady=5)

        
        
        
    else:
        failure=Label(login_frame,text="Login failed",fg="red")
        failure.pack()


loginbtn = Button(login_frame,text="Login",command=login)
loginbtn.pack()

cancelbtn = Button(login_frame,text="Cancel",command=root.destroy)
cancelbtn.pack()

root.mainloop()
