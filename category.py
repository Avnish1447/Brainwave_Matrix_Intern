from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Inventory Management System | Avnish Agrawal")
        self.root.config(bg="#ffffff")
        '''fefae0'''
        self.root.focus_force()
        

        #Variables
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #Title
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30,"bold"),bg="#507874",fg="#ffffff",bd=3,relief=RIDGE)
        lbl_title.pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30,"bold"),bg="#f1faee")
        lbl_name.place(x=50,y=100)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18,"bold"),bg="lightyellow")
        txt_name.place(x=50,y=170,width=300)
        
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",18,"bold"),bg="#386641",fg="#ffffff",cursor="hand2")
        btn_add.place(x=360,y=170,width=150,height=30)
        
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",18,"bold"),bg="#bc4749",fg="#ffffff",cursor="hand2")
        btn_delete.place(x=520,y=170,width=150,height=30)
        
        #Category Details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=400,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid",text="Category ID")
        self.category_table.heading("name",text="Name")
        
        self.category_table["show"]="headings"

        self.category_table.column("cid",width=100)
        self.category_table.column("name",width=125)
        self.category_table.pack(fill=BOTH,expand=1)
        self.show()
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #Images
        self.im1=Image.open("Images/images/cat.jpg")
        self.im1=self.im1.resize((500,250))
        self.im1=ImageTk.PhotoImage(self.im1)

        self_lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self_lbl_im1.place(x=50,y=220)

        self.im2=Image.open("Images/images/catEGORY.jpg")
        self.im2=self.im2.resize((500,250))
        self.im2=ImageTk.PhotoImage(self.im2)

        self_lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self_lbl_im2.place(x=580,y=220)

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":

                    messagebox.showerror("Error","Category is required",parent=self.root)
            else:
                cur.execute("Select * from category WHERE name = ?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category exists",parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)} ",parent=self.root)
        
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)

    def get_data(self,ev):
        f=self.category_table.focus()
        content= (self.category_table.item(f))
        row=content['values']
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get()=="":

                messagebox.showerror("Error","Select a category",parent=self.root)
            else:
                cur.execute("Select * from category WHERE cid = ?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid category",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","The action cannot be reversed\ndo you wish to continue ?",parent=self.root)
                    if op==TRUE:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Category Deleted Successfully",parent=self.root)
                        self.show()
                        # self.clear()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)} ", parent=self.root)

        



if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()