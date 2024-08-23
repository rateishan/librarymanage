from tkinter import *
from PIL import Image, ImageTk
import pymysql
import datetime
from tkinter import messagebox
from tkinter import ttk,messagebox
from datetime import timedelta,date




class issuebookclass:
    def __init__(self, root):
        self.root = root
        self.root.title("library management system")
        self.root.geometry("800x500+330+183")
        self.root.config(bg="#80AF81")
        self.root.resizable(False, False)

        title=Label(self.root,text="ISSUE BOOK",font=("times new roman",25,"bold"),bg="black",fg="white",pady=10,padx=10)
        title.place(x=0,y=0,relwidth=1)

        #variables----------------------
       
        
        self.var_issuedate=StringVar()
        self.var_receivedate=StringVar()


        #book----------------
        self.var_code=StringVar()
        self.var_bookname=StringVar()
        self.var_author=StringVar()
        self.var_catagory=StringVar()
        self.var_rack=StringVar()
        self.var_status=StringVar()
        self.var_date=StringVar()
        
        #member-------------
        self.var_nic=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()

        self.var_searchtxet=StringVar()
        self.var_searchby=StringVar()
        
        self.var_issuedate.set(date.today())
        self.var_receivedate.set(date.today()+timedelta(days=7))
      
        #labal---------------------------
        lbl_bookcode=Label(self.root,text="Book Code",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl_bookcode.place(x=5,y=100)
        lbl_membernic=Label(self.root,text="NIC",font=("times new roman",20,"bold"),bg='#80AF81',fg="black")
        lbl_membernic.place(x=5,y=150)

        #----Book detail lbl------
        lbl_bookname=Label(self.root,text="Book name",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_bookname.place(x=420,y=80)
       
        lbl_author=Label(self.root,text="Author",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_author.place(x=420,y=110)

        lbl_catagory=Label(self.root,text="Catagory",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_catagory.place(x=420,y=140)

        lbl_rack=Label(self.root,text="Rack",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_rack.place(x=420,y=170)

        #-----------memmber details lbl-------
        lbl_membername=Label(self.root,text="Member",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_membername.place(x=420,y=230)
       
        lbl_address=Label(self.root,text="Address",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_address.place(x=420,y=260)

        lbl_catagory=Label(self.root,text="Contact",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_catagory.place(x=420,y=290)

        lbl_rack=Label(self.root,text="Email",font=("times new roman",14,"bold"),bg='#80AF81',fg="black")
        lbl_rack.place(x=420,y=320)


        #-----------entrybookcode_nic     
        entry_code=Entry(self.root,textvariable=self.var_code,font=("times new roman",18,"bold"),bg="white")
        entry_code.place(x=150,y=100,width=55,height=35)

        entry_nic=Entry(self.root,textvariable=self.var_nic,font=("times new roman",18,"bold"),bg="white")
        entry_nic.place(x=150,y=150,width=148,height=35)

        #----------entrybook details

        entry_bookname=Entry(self.root,textvariable=self.var_bookname,font=("times new roman",14),bg="#80AF81")
        entry_bookname.place(x=530,y=80,width=260,height=25)

        entry_author=Entry(self.root,textvariable=self.var_author,font=("times new roman",14),bg="#80AF81")
        entry_author.place(x=530,y=110,width=260,height=25)

        entry_catagory=Entry(self.root,textvariable=self.var_catagory,font=("times new roman",14),bg="#80AF81")
        entry_catagory.place(x=530,y=140,width=260,height=25)

        entry_rack=Entry(self.root,textvariable=self.var_rack,font=("times new roman",14),bg="#80AF81")
        entry_rack.place(x=530,y=170,width=260,height=25)

        #------entrymemberetails

        entry_bookname=Entry(self.root,textvariable=self.var_name,font=("times new roman",14),bg="#80AF81")
        entry_bookname.place(x=530,y=230,width=260,height=25)

        entry_author=Entry(self.root,textvariable=self.var_address,font=("times new roman",14),bg="#80AF81")
        entry_author.place(x=530,y=260,width=260,height=25)

        entry_catagory=Entry(self.root,textvariable=self.var_contact,font=("times new roman",14),bg="#80AF81")
        entry_catagory.place(x=530,y=290,width=260,height=25)

        entry_rack=Entry(self.root,textvariable=self.var_email,font=("times new roman",14),bg="#80AF81")
        entry_rack.place(x=530,y=320,width=260,height=25)



        btn_search1=Button(self.root,text="search",command=self.search1,font=("times",20,"bold"),bg="black",fg="white")
        btn_search1.place(x=315,y=100,width=100,height=40)

        btn_search2=Button(self.root,text="search",command=self.search2,font=("times",20,"bold"),bg="black",fg="white")
        btn_search2.place(x=315,y=150,width=100,height=40)

        btn_save=Button(self.root,text="Issue",command=self.save,font=("times",20,"bold"),bg="black",fg="white")
        btn_save.place(x=5,y=250,width=100,height=40)

        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times",20,"bold"),bg="black",fg="white")
        btn_delete.place(x=120,y=250,width=100,height=40)

        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times",20,"bold"),bg="black",fg="white")
        btn_clear.place(x=235,y=250,width=100,height=40)

        
        #button---------------------------
        #btn_save=Button(self.root,text="Save",command=self.save,font=("times",20,"bold"),bg="black",fg="white")
       # #btn_save.place(x=100,y=420,width=100,height=40)
        #btn_update=Button(self.root,text="Update",command=self.update,font=("times",20,"bold"),bg="black",fg="white")
        #btn_update.place(x=250,y=420,width=100,height=40)
        #btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times",20,"bold"),bg="black",fg="white")
        #btn_delete.place(x=400,y=420,width=100,height=40)
        #btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times",20,"bold"),bg="black",fg="white")
        #btn_clear.place(x=550,y=420,width=100,height=40)

        
        #----search frame-------
        searchframe=LabelFrame(self.root,text="Search By",font=("time",12,"bold"),bd=1,relief=RIDGE,bg="#80AF81")
        searchframe.place(x=10,y=300,width=400,height=50)

      

        txt_search=Entry(searchframe,textvariable=self.var_searchtxet,font=("times",12,"bold"),bg="white")
        txt_search.place(x=110,y=1,width=120)

        btn_search=Button(searchframe,text="Search",command=self.search,font=("times",14,"bold"),bg="white")
        btn_search.place(x=235,y=2,width=80,height=20)

        btn_search=Button(searchframe,text="Clear",command=self.clears,font=("times",14,"bold"),bg="white")
        btn_search.place(x=315,y=2,width=80,height=20)

        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select","bookcode","nic","name","date_issue"),state='readonly',justify=LEFT,font=('times',13,'bold'))
        cmb_search.place(x=5,y=1,width=100,height=25)
        cmb_search.current(0)
        #treeviwe-------------------------
        treeviweframe=Frame(self.root,bd=4,relief=RIDGE)
        treeviweframe.place(x=0,y=370,width=800,height=340)

        scrolly=Scrollbar(treeviweframe,orient=VERTICAL)
        scrollx=Scrollbar(treeviweframe,orient=HORIZONTAL)
        
        self.treeviwetable=ttk.Treeview(treeviweframe,columns=("nic","membername","bookcode","bookname","issuedate","receivedate","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviwetable.xview)
        scrolly.config(command=self.treeviwetable.yview)

        self.treeviwetable.heading("nic",text="NIC")
        self.treeviwetable.heading("membername",text="Member Name")
        self.treeviwetable.heading("bookcode",text="Book Code")
        self.treeviwetable.heading("bookname",text="Book Name")
        self.treeviwetable.heading("issuedate",text="Date Issue")
        self.treeviwetable.heading("receivedate",text="Date Receive")
        self.treeviwetable.heading("status",text="Status")

        self.treeviwetable["show"]="headings"
        self.treeviwetable.column("nic",width=70)
        self.treeviwetable.column("membername",width=150)
        self.treeviwetable.column("bookcode",width=100)
        self.treeviwetable.column("bookname",width=100)
        self.treeviwetable.column("issuedate",width=100)
        self.treeviwetable.column("receivedate",width=100)
        self.treeviwetable.column("status",width=70)
  

        self.treeviwetable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviwetable.yview)
        self.treeviwetable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()
    def search(self):
        pass   
    def clears(self):
        pass

    def search1(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("select * from addbooks where code=%s",self.var_code.get())
        result=cur.fetchall()
        for row in result:
            self.var_bookname.set(row[1])
            self.var_author.set(row[2])
            self.var_catagory.set(row[3])
            self.var_rack.set(row[4])

            
            


    def search2(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("select * from member where nic=%s",self.var_nic.get())
        result=cur.fetchall()
        for row in result:
            self.var_name.set(row[1])
            self.var_address.set(row[2])
            self.var_contact.set(row[3])
            self.var_email.set(row[4])
        

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        cur.execute("select nic,membername,bookcode,bookname,issuedate,receivedate,status from bookissue where status !='Received'")
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
        self.var_code.set(row[2])
        self.var_bookname.set(row[3])
        self.var_issuedate.set(row[4])
        self.var_receivedate.set(row[5])
        self.var_status.set(row[6])   

  
    def save(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="#@19is16Pro", database="studentdata")
        cur = sqlcon.cursor()
        try:
            if self.var_nic.get() == "" or self.var_code.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)

            
            else:
                
                cur.execute("SELECT * FROM bookissue WHERE bookcode=%s AND status='issued'", (self.var_code.get(),))
                row = cur.fetchone()

                if row is not None:
                   messagebox.showerror("Error", "This book code has already been issued", parent=self.root)
                else:
                    self.var_status.set("issued")

                # Convert the issue and receive dates to the correct format
                    issue_date = datetime.datetime.strptime(self.var_issuedate.get(), '%Y-%m-%d').date()
                    receive_date = datetime.datetime.strptime(self.var_receivedate.get(), '%Y-%m-%d').date()

                    cur.execute("INSERT INTO bookissue (nic, membername, bookcode, bookname, issuedate, receivedate, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (
                                self.var_nic.get(),
                                self.var_name.get(),
                                self.var_code.get(),
                                self.var_bookname.get(),
                                issue_date,
                                receive_date,
                                self.var_status.get(),
                            ))
                    sqlcon.commit()
                    messagebox.showinfo("Success", "Data saved successfully", parent=self.root)
                    self.displaydata()
                    self.clear()
            sqlcon.close()
        except Exception as ex:
           messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        
    
    def delete(self):
        if len(self.var_code.get()) == 0:
            messagebox.showerror("Error","Please select the data first",parent=self.root)
        elif self.var_issuedate.get() != str(date.today()):
            messagebox.showerror("Error","You can't delete this data",parent=self.root)    
        else:
            sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
            cur=sqlcon.cursor()
            cur.execute("delete from bookissue where bookcode=%s",self.var_code.get())
            sqlcon.commit()
            self.displaydata()
            messagebox.showinfo("Success","Data deleted successfully",parent=self.root)
            sqlcon.close()
            self.clear()
                    
    def clear(self):
        
        self.var_status.set(""),
        self.var_bookname.set(""),
        self.var_code.set(""),
        self.var_issuedate.set(""),
        self.var_receivedate.set(""),
        self.var_nic.set(""),
        self.var_name.set(""),
        self.var_address.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_date.set(""),
        self.var_author.set(""),
        self.var_catagory.set(""),
        self.var_rack.set(""),
        
       

            
        


if __name__=="__main__":
    root=Tk()
    obj=issuebookclass(root)
    root.mainloop()    