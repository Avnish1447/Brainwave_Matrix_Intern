from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Inventory Management System | Avnish Agrawal")
        self.root.config(bg="#ffffff")
        '''fefae0'''
        self.root.focus_force()


        #All Variables
        self.var_searchBy = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email=StringVar()
        self.var_password = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        #SearchBox
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#f1faee")
        SearchFrame.place(relx=0.2,rely=0.030,width=600,height=70)

        #OPtions
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("Search By ","E-mail","Name","Contact"),state="readonly",justify=CENTER,font=("goudy old style",10,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg = "#ffffe0").place(x=200,y=10)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 12, "bold"), bg="#83c5be", fg="#fefae0", cursor="hand2").place(x=410, y=9, width=150, height=30)


        #Title
        title = Label(self.root, text="Employee Details",font=("goudy old style",15), bg="#83c5be", fg="#fefae0", cursor="hand2")
        # title.place(x=50, y=100, width=1000, height=30)
        title.place(relx=0.5, y=120, relwidth=0.95,anchor=CENTER)

        #Content

        #Row 1
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=150)
        lbl_contact = Label(self.root, text="Gender", font=("goudy old style", 15), bg="#ffffff").place(x=350, y=150)
        lbl_gender = Label(self.root, text="Contact", font=("goudy old style", 15), bg="#ffffff").place(x=650, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=150,width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select ", "Male", "Female"), state="readonly", justify=CENTER,font=("goudy old style", 10, "bold"))
        cmb_gender.place(x=450, y=150, width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=750, y=150,width=180)

        #Row 2
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=200)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15), bg="#ffffff").place(x=350, y=200)
        lbl_contact = Label(self.root, text="D.O.J", font=("goudy old style", 15), bg="#ffffff").place(x=650, y=200)

        txt_Name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=200,width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=450, y=200,width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow").place(x=750, y=200,width=180)


        #Row 3
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=250)
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 15), bg="#ffffff").place(x=350, y=250)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 15), bg="#ffffff").place(x=650, y=250)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=250,width=180)
        txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 15), bg="lightyellow").place(x=450, y=250,width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype,values=("Select ", "Administrator", "Local"), state="readonly", justify=CENTER,font=("goudy old style", 10, "bold"))
        cmb_utype.place(x=750, y=250, width=180)
        cmb_utype.current(0)

        #Row 4
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=300)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="#ffffff").place(x=500, y=300)
        # lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 15), bg="#ffffff").place(x=650, y=250)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=300,width=300,height=50)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow").place(x=600, y=300,width=180)
        
        #Salary Buttons
        btn_save = Button(self.root, text="Save",command=self.add, font=("goudy old style", 12, "bold"), bg="#2196f3", fg="#fefae0", cursor="hand2").place(x=500, y=350, width=100, height=30)
        btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 12, "bold"), bg="#4caf50", fg="#fefae0", cursor="hand2").place(x=610, y=350, width=100, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete,font=("goudy old style", 12, "bold"), bg="#f44336", fg="#fefae0", cursor="hand2").place(x=720, y=350, width=100, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear,font=("goudy old style", 12, "bold"), bg="#607d8b", fg="#fefae0", cursor="hand2").place(x=830, y=350, width=100, height=30)

        #Employee Details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=400,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","gender","email","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email", text="E-Mail")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("password", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=100)
        self.EmployeeTable.column("name",width=125)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":

                messagebox.showerror("Error", "Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid = ?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already assigned, Try other",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,gender,email,contact,dob,doj,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_password.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content= (self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_email.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_password.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10]),

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":

                messagebox.showerror("Error","Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid = ?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("update employee set name=?,gender=?,email=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? WHERE  eid = ?",(

                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_password.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":

                messagebox.showerror("Error","Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid = ?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","The action cannot be reversed\ndo you wish to continue ?",parent=self.root)
                    if op==TRUE:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Employee Deleted Successfully",parent=self.root)

                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_gender.set("Select"),
        self.var_email.set(""),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_password.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0',END)
        self.var_salary.set(""),
        self.var_searchtxt.set(""),
        self.var_searchBy.set("Search By"),
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchBy.get()=="Select":
                messagebox.showerror("Error","Select search category",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Select input required", parent=self.root)
            else:
                cur.execute("Select * from employee WHERE "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)



if __name__ == "__main__":
    root = Tk( )
    obj = employeeClass(root)
    root.mainloop()