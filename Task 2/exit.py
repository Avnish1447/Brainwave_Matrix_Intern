from tkinter import messagebox

class exitClass:
    def __init__(self, root):
        self.root = root
        self.confirm_exit()
    
    def confirm_exit(self):
        
        answer = messagebox.askyesno("Exit", "Do you really want to exit?")
        if answer:
            self.root.destroy()
