from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

root = Tk()
root.title("GUI Creator")
root.geometry("600x600")

elements = ["Label","Button","Dropdown"]

dropdown = ttk.Combobox(root, state = "readonly", values = elements)
dropdown.pack()


class C_Elements():
    def __init__(self):
        print("This is Creating Elements")
        
    def C_label(self):
        label = Label(root, text = "A new Label had been created using class", fg = "gold", )
        label.pack()
        
    def C_button(self):
        btn = Button(root, text = "Click Me", command = self.msg)
        btn.pack(padx = 20, pady = 10)
        
    def C_D(self):
        val = [1,2,3,4,5,6,7,8,9,10]
        dd = ttk.Combobox(root, state = "readonly", values = val)
        dd.pack()
        
    def choose(self):
        global dropdown
        value = dropdown.get()
        
        if(value == "Label"):
            self.C_label()
        elif(value == "Button"):
            self.C_button()
        else:
            self.C_D()
    def msg(self):
        messagebox.showinfo("Created","A Button has been created using Classes")
        
c_obj = C_Elements()
btn2 = Button(root, text = "Create Element", command = c_obj.choose)
btn2.pack()

root.mainloop()
            
    
 