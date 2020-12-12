from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import *
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
    cur.execute("SELECT password FROM users WHERE username=?",(username.get(),))
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
        bk_id=ttk.Entry(tab1)
        bk_id.grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(tab1,text="Book_Name").grid(row=1,column=0,padx=5,pady=5)
        bk_name=ttk.Entry(tab1)
        bk_name.grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(tab1,text="Author_Name").grid(row=2,column=0,padx=5,pady=5)
        bk_author=ttk.Entry(tab1)
        bk_author.grid(row=2,column=1,padx=5,pady=5)

        def addBook():
            conn = sqlite3.connect("books.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO books VALUES (:bk_id,:bk_name,:bk_author)",
            {
                'bk_id': bk_id.get(),
                'bk_name': bk_name.get(),
                'bk_author':bk_author.get()
            })
            conn.commit()
            conn.close()


        def deleteBook():
            conn = sqlite3.connect("books.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE b_id=?",(bk_id.get(),))
            bk_value=cur.fetchone()
            conn.commit()
            conn.close()
            
        
        addbkbtn = ttk.Button(tab1,text="Add Book",command=addBook)
        addbkbtn.grid(row=3,column=0,padx=5,pady=5)
        delbkbtn = ttk.Button(tab1,text="Delete Book",command=deleteBook)
        delbkbtn.grid(row=3,column=1,padx=5,pady=5)

        ttk.Label(tab2,text="Student_ID").grid(row=0,column=0,padx=5,pady=5)
        s_id=ttk.Entry(tab2)
        s_id.grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Student_Name").grid(row=1,column=0,padx=5,pady=5)
        s_name=ttk.Entry(tab2)
        s_name.grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Year").grid(row=2,column=0,padx=5,pady=5)
        s_year=ttk.Entry(tab2)
        s_year.grid(row=2,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Department").grid(row=3,column=0,padx=5,pady=5)
        s_dept=ttk.Entry(tab2)
        s_dept.grid(row=3,column=1,padx=5,pady=5)

        def stdetail():
            conn = sqlite3.connect("students.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM students WHERE s_id=?",(s_id.get(),))
            st_value=cur.fetchone()
            s_name.insert(0,st_value[1])
            s_year.insert(0,st_value[2])
            s_dept.insert(0,st_value[3])
            conn.commit()
            conn.close()
     
        stbtn = ttk.Button(tab2,text="Student Details",command=stdetail)
        stbtn.grid(row=1,column=2,padx=5,pady=5)
        
        ttk.Label(tab2,text="Book_ID").grid(row=4,column=0,padx=5,pady=5)
        b_id=ttk.Entry(tab2)
        b_id.grid(row=4,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Book_Name").grid(row=5,column=0,padx=5,pady=5)
        b_name=ttk.Entry(tab2)
        b_name.grid(row=5,column=1,padx=5,pady=5)
        ttk.Label(tab2,text="Author_Name").grid(row=6,column=0,padx=5,pady=5)
        b_author=ttk.Entry(tab2)
        b_author.grid(row=6,column=1,padx=5,pady=5)

        def bkdetail():
            conn = sqlite3.connect("books.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE b_id=?",(b_id.get(),))
            bk_value=cur.fetchone()
            b_name.insert(0,bk_value[1])
            b_author.insert(0,bk_value[2])
            conn.commit()
            conn.close()

        cal=Calendar(tab2,selectmode="day",year=2020,month=12)
        cal.grid(row=3,column=7,padx=5,pady=5)

        def brwdat():
            brwdt.insert(0,cal.get_date())

        def rtndat():
            rtndt.insert(0,cal.get_date())


        def borrow():
            conn = sqlite3.connect("students_book_info.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO student_book_info VALUES (:b_id,:s_id,:brwdt,:rtndt)",
            {
                'b_id': b_id.get(),
                's_id': s_id.get(),
                'brwdt':brwdt.get(),
                'rtndt':rtndt.get()
            })
            conn.commit()
            conn.close()

        def return_bk():
            conn = sqlite3.connect("students_book_info.db")
            cur = conn.cursor()
            bk_id=b_id.get()
            st_id=s_id.get()
            rtdt=rtndt.get()
            
            cur.execute("UPDATE student_book_info SET return_date =? WHERE b_id =? AND s_id=?",(rtdt,bk_id,st_id))
            conn.commit()
            conn.close()
        
        bkbtn = ttk.Button(tab2,text="Book Details",command=bkdetail)
        bkbtn.grid(row=5,column=2,padx=5,pady=5)
        ttk.Label(tab2,text="Borrow_Date").grid(row=7,column=0,padx=5,pady=5)
        brwdt=ttk.Entry(tab2)
        brwdt.grid(row=7,column=1,padx=5,pady=5)
        brwcal=ttk.Button(tab2,text="🕒",command=brwdat)
        brwcal.grid(row=7,column=2)
        ttk.Label(tab2,text="Return_Date").grid(row=8,column=0,padx=5,pady=5)
        rtndt=ttk.Entry(tab2)
        rtndt.grid(row=8,column=1,padx=5,pady=5)
        rtncal=ttk.Button(tab2,text="🕒",command=rtndat)
        rtncal.grid(row=8,column=2)

        brwbtn = ttk.Button(tab2,text="Borrow Book",command=borrow)
        brwbtn.grid(row=9,column=1,padx=5,pady=5)
        rtnbtn = ttk.Button(tab2,text="Return Book",command=return_bk)
        rtnbtn.grid(row=9,column=2,padx=5,pady=5)

        
        
        
    else:
        failure=Label(login_frame,text="Login failed",fg="red")
        failure.pack()


loginbtn = Button(login_frame,text="Login",command=login)
loginbtn.pack()

cancelbtn = Button(login_frame,text="Cancel",command=root.destroy)
cancelbtn.pack()

root.mainloop()
