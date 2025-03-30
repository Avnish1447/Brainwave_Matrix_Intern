from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from exit import exitClass
from login import loginClass
import sqlite3


class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Avnish Agrawal")
        self.root.config(bg="white")
        #Title
        self.icon_title=PhotoImage(file="Images/Untitled design (Custom).png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #LogOut Button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#010c48",fg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #clock
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Left Menu
        self.MenuLogo=Image.open("Images/images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#f1faee")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_MenuLogo= Label(LeftMenu,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

        self.icon_side = PhotoImage(file="Images/images/side.png")

        Label_Menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688", fg="white").pack(side=TOP,fill=X)

        btn_employee = Button(LeftMenu, text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplier = Button(LeftMenu, text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category = Button(LeftMenu, text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product = Button(LeftMenu, text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        # btn_Sales = Button(LeftMenu, text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit = Button(LeftMenu, text="Exit",command=self.exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 10, "bold"), bg="#bfc6bd",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        # Boxes
            #Employee
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd = 5,relief=RIDGE,bg="#ffb5a7",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

            #Supplier
        self.lbl_supplier=Label(self.root,text="Total supplier\n[ 0 ]",bd = 5,relief=RIDGE,bg="#fcd5ce",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
            #Category
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd = 5,relief=RIDGE,bg="#f8edeb",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
            #Product
        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd = 5,relief=RIDGE,bg="#f9dcc4",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
            #Sales
        # self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd = 5,relief=RIDGE,bg="#fec89a",fg="black",font=("goudy old style",20,"bold"))
        # self.lbl_sales.place(x=650,y=300,height=150,width=300)


        # Footer
        lbl_footer = Label(self.root,text="Inventory Management System | BrainWave Matrix Solutions \n Avnish Agrawal",font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM,fill=X)

        self.update_counts()

    def update_counts(self):
        """Fetches and updates employee, category, product, and supplier counts in dashboard boxes."""
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            # Fetch counts from database
            cur.execute("SELECT COUNT(*) FROM employee")
            employee_count = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM category")
            category_count = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM product")
            product_count = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM supplier")
            supplier_count = cur.fetchone()[0]

            self.lbl_employee.config(text=f"Total Employees\n{employee_count}")
            self.lbl_category.config(text=f"Total Categories\n{category_count}")
            self.lbl_product.config(text=f"Total Products\n{product_count}")
            self.lbl_supplier.config(text=f"Total Suppliers\n{supplier_count}")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:

            con.close()

        self.root.after(2000, self.update_counts)

        # Call function to update counts dynamically


    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)    

    def exit(self):
        exitClass(self.root)

    if __name__ == "__main__":
        root = Tk()
        login_window = loginClass(root)
        root.mainloop()




if __name__ == "__main__":
    root = Tk( )

    obj = IMS(root)
    root.mainloop()