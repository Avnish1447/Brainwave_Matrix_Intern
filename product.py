from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Inventory Management System | Avnish Agrawal")
        self.root.config(bg="#ffffff")
        '''fefae0'''
        self.root.focus_force()

        #Variables
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.var_searchBy = StringVar()
        self.var_searchtxt = StringVar()
        self.var_pid=StringVar()

        #Product Frame
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#f1faee")
        product_Frame.place(x=10,y=10,width=450,height=480)

        title = Label(product_Frame, text="Product Details",font=("goudy old style",20), bg="#83c5be", fg="#fefae0", cursor="hand2")
        title.pack(side=TOP,fill=X,pady=2)

        #Coloumn 1
        lbl_category = Label(product_Frame, text="Category",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_category.place(x=30,y=60)

        lbl_supplier = Label(product_Frame, text="Supplier",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_supplier.place(x=30,y=110)
        
        lbl_product_name = Label(product_Frame, text="Name",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_product_name.place(x=30,y=160)
        
        lbl_price = Label(product_Frame, text="Price",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_price.place(x=30,y=210)

        lbl_quantity = Label(product_Frame, text="Quantity",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_quantity.place(x=30,y=260)

        lbl_status = Label(product_Frame, text="Status",font=("goudy old style",20,"bold"), bg="#f1faee",fg="#83c5be", cursor="hand2")
        lbl_status.place(x=30,y=310)

        #Coloumn 2

        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("goudy old style",10,"bold"))
        cmb_cat.place(x=150,y=70,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("goudy old style",10,"bold"))
        cmb_sup.place(x=150,y=120,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",10,"bold"),bg="lightyellow")
        txt_name.place(x=150,y=170,width=200)

        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",10,"bold"),bg="lightyellow")
        txt_price.place(x=150,y=220,width=200)

        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",10,"bold"),bg="lightyellow")
        txt_qty.place(x=150,y=270,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("goudy old style",10,"bold"))
        cmb_status.place(x=150,y=320,width=200)
        cmb_status.current(0)

        #Salary Buttons
        btn_save = Button(product_Frame, text="Save",command=self.add, font=("goudy old style", 12, "bold"), bg="#2196f3", fg="#fefae0", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update",command=self.update, font=("goudy old style", 12, "bold"), bg="#4caf50", fg="#fefae0", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete,font=("goudy old style", 12, "bold"), bg="#f44336", fg="#fefae0", cursor="hand2").place(x=240, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear,font=("goudy old style", 12, "bold"), bg="#607d8b", fg="#fefae0", cursor="hand2").place(x=360, y=400, width=100, height=40)

    #Search Box
        #SearchFrame
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#f1faee")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #OPtions
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("Search By ","Name","Category","Supplier"),state="readonly",justify=CENTER,font=("goudy old style",10,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg = "#ffffe0").place(x=200,y=10)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 12, "bold"), bg="#83c5be", fg="#fefae0", cursor="hand2").place(x=410, y=9, width=150, height=30)

        #Product Details
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="Product ID")
        self.product_Table.heading("Category",text="Category")
        self.product_Table.heading("Supplier", text="Supplier")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Quantity")
        self.product_Table.heading("status", text="Status")
        
        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=100)
        self.product_Table.column("Category",width=125)
        self.product_Table.column("Supplier",width=100)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=100)
        self.product_Table.column("status", width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        


        #Functions  

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

              
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or  self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":

                messagebox.showerror("Error","All feilds are required",parent=self.root)
            else:
                cur.execute("Select * from product WHERE name = ?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already availaible",parent=self.root)
                else:
                    cur.execute("Insert into product( Category , Supplier , name , price , qty , status ) values(?,?,?,?,?,?)",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            ))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)


    def get_data(self,ev):
        f=self.product_Table.focus()
        content= (self.product_Table.item(f))
        row=content['values']        
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":

                messagebox.showerror("Error","Select product from list",parent=self.root)
            else:
                cur.execute("Select * from product WHERE pid = ?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    cur.execute("update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? WHERE  pid = ?",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":

                messagebox.showerror("Error","Product ID is required",parent=self.root)
            else:
                cur.execute("Select * from product WHERE pid = ?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","The action cannot be reversed\ndo you wish to continue ?",parent=self.root)
                    if op==TRUE:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Employee Deleted Successfully",parent=self.root)

                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)

    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set("Active"),
        self.var_status.set(""),
        self.var_pid.set(""),
        self.var_searchtxt.set(""),
        self.var_searchBy.set("Search By"),
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchBy.get()=="Select":
                messagebox.showerror("Error","Select search product",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Select input required", parent=self.root)
            else:
                cur.execute("Select * from product WHERE "+self.var_searchBy.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)





if __name__ == "__main__":
    root = Tk( )
    obj = productClass(root)
    root.mainloop()        