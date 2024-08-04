from tkinter import *
from PIL import Image, ImageTk




class addbookclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Book")
        self.root.geometry("800x450+330+180")
        self.root.config(bg="#80AF81")
        self.root.resizable(False, False)

        title=Label(self.root,text="ADD BOOK",font=("times new roman",25,"bold"),bg="black",fg="white",pady=10,padx=10)
        title.place(x=0,y=0,relwidth=1)

        lbl1=Label(self.root,text="Book Code",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl1.place(x=50,y=100)
        lbl2=Label(self.root,text="Book Name",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl2.place(x=50,y=150)
        lbl3=Label(self.root,text="Author Name",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl3.place(x=50,y=200)
        lbl4=Label(self.root,text="Catagory",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl4.place(x=50,y=250)
        lbl5=Label(self.root,text="Rack",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl5.place(x=50,y=300)
        lbl6=Label(self.root,text="Date",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl6.place(x=50,y=350)

        entry_code=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        entry_code.place(x=250,y=100,width=100,height=35)
        Frame(self.root,bg="black")

        entry_name=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        entry_name.place(x=250,y=150,width=300,height=35)

        entry_author=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        entry_author.place(x=250,y=200,width=300,height=35)

        entry_catagory=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        entry_catagory.place(x=250,y=250,width=300,height=35)

        enttry_rack=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        enttry_rack.place(x=250,y=300,width=55,height=35)

        entry_date=Entry(self.root,font=("times new roman",18,"bold"),bg="white")
        entry_date.place(x=250,y=350,width=130,height=35)


if __name__=="__main__":
    root=Tk()
    obj=addbookclass(root)
    root.mainloop()    