from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
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
        
        self.var_sup_invoice=StringVar()
        self.var_name = StringVar()
        self.var_contact=StringVar()

        # #SearchBox
        # SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#f1faee")
        # SearchFrame.place(relx=0.2,rely=0.030,width=600,height=70)

        #OPtions
        lbl_search=Label(self.root,text="Searh by Invoice No.",font=("goudy old style",10,"bold"))
        lbl_search.place(x=650,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg = "#ffffe0").place(x=800,y=80,width=125)
        btn_search = Button(self.root, text="Search",command=self.search, font=("goudy old style", 12, "bold"), bg="#83c5be", fg="#fefae0", cursor="hand2").place(x=950, y=79, width=100, height=25)


        #Title
        title = Label(self.root, text="Supplier Details",font=("goudy old style",20), bg="#83c5be", fg="#fefae0", cursor="hand2")
        title.place(x=50, y=10, width=1000, height=40)
        

        #Content

        #Row 1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=80)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=80,width=180)

        #Row 2
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=120)
        txt_Name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=120,width=180)
    

        #Row 3
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=160,width=180)

        #Row 4
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="#ffffff").place(x=50, y=200)

        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200,width=425,height=150)

        #Salary Buttons
        btn_save = Button(self.root, text="Save",command=self.add, font=("goudy old style", 12, "bold"), bg="#2196f3", fg="#fefae0", cursor="hand2").place(x=180, y=375, width=100, height=35)
        btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 12, "bold"), bg="#4caf50", fg="#fefae0", cursor="hand2").place(x=290, y=375, width=100, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete,font=("goudy old style", 12, "bold"), bg="#f44336", fg="#fefae0", cursor="hand2").place(x=400, y=375, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear,font=("goudy old style", 12, "bold"), bg="#607d8b", fg="#fefae0", cursor="hand2").place(x=510, y=375, width=100, height=35)

        #Supplier Details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=650,y=120,width=400,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="Invoice No.")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")

        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=100)
        self.SupplierTable.column("name",width=125)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":

                    messagebox.showerror("Error","Invoice is required",parent=self.root)
            else:
                cur.execute("Select * from supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. already assigned",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                            self.var_sup_invoice.get(),
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)


    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content= (self.SupplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":

                messagebox.showerror("Error","Invoice No. is required",parent=self.root)
            else:
                cur.execute("Select * from supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? WHERE  invoice = ?",(

                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0', END),                        
                            self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":

                messagebox.showerror("Error","Invoice No. is required",parent=self.root)
            else:
                cur.execute("Select * from supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","The action cannot be reversed\ndo you wish to continue ?",parent=self.root)
                    if op==TRUE:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Supplier Deleted Successfully",parent=self.root)

                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set(""),
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice No. required", parent=self.root)
            else:
                cur.execute("Select * from supplier WHERE invoice=? ",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if rows!=NONE:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())                    
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()