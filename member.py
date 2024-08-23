from tkinter import *
from PIL import Image, ImageTk
import pymysql
import datetime
from tkinter import messagebox
from tkinter import ttk,messagebox




class membersclass:
    def __init__(self, root):
        self.root = root
        self.root.title("library management system")
        self.root.geometry("800x500+330+183")
        self.root.config(bg="#80AF81")
        self.root.resizable(False, False)

        title=Label(self.root,text="MEMBERS",font=("times new roman",25,"bold"),bg="black",fg="white",pady=10,padx=10)
        title.place(x=0,y=0,relwidth=1)

        #variables----------------------
        self.var_nic=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_date=StringVar()

        self.var_date.set(datetime.datetime.now().date())


        #labal---------------------------
        lbl1=Label(self.root,text="NIC No",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl1.place(x=50,y=100)
        lbl2=Label(self.root,text="Name",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl2.place(x=50,y=150)
        lbl3=Label(self.root,text="Address",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl3.place(x=50,y=200)
        lbl4=Label(self.root,text="Contact No",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl4.place(x=50,y=250)
        lbl5=Label(self.root,text="Email",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl5.place(x=50,y=300)
        lbl6=Label(self.root,text="Date",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl6.place(x=50,y=350)

        entry_nic=Entry(self.root,textvariable=self.var_nic,font=("times new roman",18,"bold"),bg="white")
        entry_nic.place(x=250,y=100,width=150,height=35)
        Frame(self.root,bg="black")

        entry_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18,"bold"),bg="white")
        entry_name.place(x=250,y=150,width=300,height=35)

        entry_address=Entry(self.root,textvariable=self.var_address,font=("times new roman",18,"bold"),bg="white")
        entry_address.place(x=250,y=200,width=300,height=35)

        entry_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",18,"bold"),bg="white")
        entry_contact.place(x=250,y=250,width=135,height=35)

        enttry_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",18,"bold"),bg="white")
        enttry_email.place(x=250,y=300,width=255,height=35)

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
        treeviweframe.place(x=560,y=70,width=250,height=340)

        scrolly=Scrollbar(treeviweframe,orient=VERTICAL)
        scrollx=Scrollbar(treeviweframe,orient=HORIZONTAL)
        
        self.treeviwetable=ttk.Treeview(treeviweframe,columns=("nic","name",),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviwetable.xview)
        scrolly.config(command=self.treeviwetable.yview)

        self.treeviwetable.heading("nic",text="NIC")
        self.treeviwetable.heading("name",text="Name")

        self.treeviwetable["show"]="headings"
        self.treeviwetable.column("nic",width=80)
        self.treeviwetable.column("name",width=150)
  

        self.treeviwetable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviwetable.yview)
        self.treeviwetable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("select * from member")
        result=cur.fetchall()

        self.treeviwetable.delete(*self.treeviwetable.get_children())
        for row in result:
            self.treeviwetable.insert("",END,values=row)
    
    def getdata(self,ev):
        viweinfo=self.treeviwetable.focus()
        learnerdata=(self.treeviwetable.item(viweinfo))
        row=learnerdata['values']

        self.var_nic.set(row[0])
        self.var_name.set(row[1])
        self.var_address.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_date.set(row[5])    

    def save(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        try:
            if self.var_nic.get()=="":
                messagebox.showerror("Error","all field required",parent=self.root)
            else:
                cur.execute("insert into member (nic,name,address,contact,email,date) values(%s,%s,%s,%s,%s,%s)",
                (
                    self.var_nic.get(),
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
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
        cur.execute("update member set name=%s,address=%s,contact=%s,email=%s,date=%s where nic=%s",
                    
                  (
                      self.var_name.get(),
                      self.var_address.get(),
                      self.var_contact.get(),
                      self.var_email.get(),
                      self.var_date.get(),
                      self.var_nic.get(),

                  ) ) 
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success","Data updated successfully",parent=self.root)
        sqlcon.close()
        self.clear()
  
    
    
    def delete(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("delete from member where nic=%s",self.var_nic.get())
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success","Data deleted successfully",parent=self.root)
        sqlcon.close()
        self.clear()
                    
    def clear(self):
        self.var_nic.set(""),
        self.var_name.set(""),
        self.var_address.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_date.set("")
            
        


if __name__=="__main__":
    root=Tk()
    obj=membersclass(root)
    root.mainloop()    