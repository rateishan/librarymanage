from tkinter import *
from PIL import Image, ImageTk
import pymysql
import datetime
from tkinter import messagebox
from tkinter import ttk,messagebox




class addbookclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Book")
        self.root.geometry("800x500+330+183")
        self.root.config(bg="#80AF81")
        self.root.resizable(False, False)

        title=Label(self.root,text="ADD BOOK",font=("times new roman",25,"bold"),bg="black",fg="white",pady=10,padx=10)
        title.place(x=0,y=0,relwidth=1)

        #variables----------------------
        self.var_code=StringVar()
        self.var_bookname=StringVar()
        self.var_author=StringVar()
        self.var_catagory=StringVar()
        self.var_rack=StringVar()
        self.var_date=StringVar()

        self.var_date.set(datetime.datetime.now().date())


        #labal---------------------------
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

        entry_code=Entry(self.root,textvariable=self.var_code,font=("times new roman",18,"bold"),bg="white")
        entry_code.place(x=250,y=100,width=100,height=35)
        Frame(self.root,bg="black")

        entry_name=Entry(self.root,textvariable=self.var_bookname,font=("times new roman",18,"bold"),bg="white")
        entry_name.place(x=250,y=150,width=300,height=35)

        entry_author=Entry(self.root,textvariable=self.var_author,font=("times new roman",18,"bold"),bg="white")
        entry_author.place(x=250,y=200,width=300,height=35)

        entry_catagory=Entry(self.root,textvariable=self.var_catagory,font=("times new roman",18,"bold"),bg="white")
        entry_catagory.place(x=250,y=250,width=300,height=35)

        enttry_rack=Entry(self.root,textvariable=self.var_rack,font=("times new roman",18,"bold"),bg="white")
        enttry_rack.place(x=250,y=300,width=55,height=35)

        entry_date=Entry(self.root,textvariable=self.var_date,font=("times new roman",18,"bold"),bg="white")
        entry_date.place(x=250,y=350,width=130,height=35)

        #button---------------------------
        btn_save=Button(self.root,text="Save",command=self.save,font=("times",20,"bold"),bg="black",fg="white")
        btn_save.place(x=100,y=420,width=100,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times",20,"bold"),bg="black",fg="white")
        btn_update.place(x=250,y=420,width=100,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times",20,"bold"),bg="black",fg="white")
        btn_delete.place(x=400,y=420,width=100,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times",20,"bold"),bg="black",fg="white")
        btn_clear.place(x=550,y=420,width=100,height=40)

        #treeviwe-------------------------
        treeviweframe=Frame(self.root,bd=4,relief=RIDGE)
        treeviweframe.place(x=570,y=70,width=200,height=340)

        scrolly=Scrollbar(treeviweframe,orient=VERTICAL)
        scrollx=Scrollbar(treeviweframe,orient=HORIZONTAL)
        
        self.treeviwetable=ttk.Treeview(treeviweframe,columns=("code","name",),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviwetable.xview)
        scrolly.config(command=self.treeviwetable.yview)

        self.treeviwetable.heading("code",text="Code")
        self.treeviwetable.heading("name",text="Book Name")

        self.treeviwetable["show"]="headings"
        self.treeviwetable.column("code",width=50)
        self.treeviwetable.column("name",width=150)
  

        self.treeviwetable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviwetable.yview)
        self.treeviwetable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("select * from addbooks")
        result=cur.fetchall()

        self.treeviwetable.delete(*self.treeviwetable.get_children())
        for row in result:
            self.treeviwetable.insert("",END,values=row)
    
    def getdata(self,ev):
        viweinfo=self.treeviwetable.focus()
        learnerdata=(self.treeviwetable.item(viweinfo))
        row=learnerdata['values']

        self.var_code.set(row[0])
        self.var_bookname.set(row[1])
        self.var_author.set(row[2])
        self.var_catagory.set(row[3])
        self.var_rack.set(row[4])
        self.var_date.set(row[5])    

    def save(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        try:
            if self.var_code.get()=="":
                messagebox.showerror("Error","all field required",parent=self.root)
            else:
                cur.execute("insert into addbooks (code,name,author,catagory,rack,date) values(%s,%s,%s,%s,%s,%s)",
                (
                    self.var_code.get(),
                    self.var_bookname.get(),
                    self.var_author.get(),
                    self.var_catagory.get(),
                    self.var_rack.get(),
                    self.var_date.get()

                    
                ) ) 
                sqlcon.commit()
                messagebox.showinfo("Success","Data saved successfully",parent=self.root)
                self.displaydata()
                sqlcon.close()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)


        
    def update(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("update addbooks set name=%s,author=%s,catagory=%s,rack=%s,date=%s where code=%s",
                    
                  (
                      self.var_bookname.get(),
                      self.var_author.get(),
                      self.var_catagory.get(),
                      self.var_rack.get(),
                      self.var_date.get(),
                      self.var_code.get(),

                  ) ) 
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success","Data updated successfully",parent=self.root)
        sqlcon.close()
        self.clear()
                    
    def delete(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("delete from addbooks where code=%s",self.var_code.get())
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success","Data deleted successfully",parent=self.root)
        sqlcon.close()
        self.clear()
                    
    def clear(self):
        self.var_code.set(""),
        self.var_bookname.set(""),
        self.var_author.set(""),
        self.var_catagory.set(""),
        self.var_rack.set(""),
        self.var_date.set("")
            
        


if __name__=="__main__":
    root=Tk()
    obj=addbookclass(root)
    root.mainloop()    