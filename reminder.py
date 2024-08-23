from tkinter import *
from PIL import Image, ImageTk
import pymysql
import datetime
from tkinter import messagebox
from tkinter import ttk,messagebox
from datetime import timedelta,date
import smtplib
from email.message import EmailMessage




class reminderclass:
    def __init__(self, root):
        self.root = root
        self.root.title("library management system")
        self.root.geometry("800x500+330+183")
        self.root.config(bg="#80AF81")
        self.root.resizable(False, False)

        title=Label(self.root,text="REMINDER",font=("times new roman",25,"bold"),bg="black",fg="white",pady=10,padx=10)
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
        
        #self.var_issuedate.set(date.today())
        #self.var_receivedate.set(date.today()+timedelta(days=7))
        #print(self.var_receivedate.get())
        #print(self.var_issuedate.get())

        #labal---------------------------
       
        #----Book detail lbl------
        

       

        #-----------entrybookcode_nic     
       

        

        #----------entrybook details

      


        btn_search1=Button(self.root,text="SEND",command=self.send,font=("times",20,"bold"),bg="black",fg="white")
        btn_search1.place(x=350,y=400,width=100,height=40)

       
      
        #button---------------------------
        #btn_save=Button(self.root,text="Save",command=self.save,font=("times",20,"bold"),bg="black",fg="white")
       # #btn_save.place(x=100,y=420,width=100,height=40)
        #btn_update=Button(self.root,text="Update",command=self.update,font=("times",20,"bold"),bg="black",fg="white")
        #btn_update.place(x=250,y=420,width=100,height=40)
        #btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times",20,"bold"),bg="black",fg="white")
        #btn_delete.place(x=400,y=420,width=100,height=40)
        #btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times",20,"bold"),bg="black",fg="white")
        #btn_clear.place(x=550,y=420,width=100,height=40)

        
        #----datevariable-------
        self.var_date=StringVar()
        self.var_date.set(date.today())
        
        #treeviwe-------------------------
        treeviweframe=Frame(self.root,bd=4,relief=RIDGE)
        treeviweframe.place(x=0,y=60,width=800,height=290)

        scrolly=Scrollbar(treeviweframe,orient=VERTICAL)
        scrollx=Scrollbar(treeviweframe,orient=HORIZONTAL)
        
        self.treeviwetable=ttk.Treeview(treeviweframe,columns=("nic","membername","bookcode","bookname","receivedate","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviwetable.xview)
        scrolly.config(command=self.treeviwetable.yview)

        self.treeviwetable.heading("nic",text="NIC")
        self.treeviwetable.heading("membername",text="Member Name")
        self.treeviwetable.heading("bookcode",text="Book Code")
        self.treeviwetable.heading("bookname",text="Book Name")
        self.treeviwetable.heading("receivedate",text="Date Receive")
        self.treeviwetable.heading("status",text="Status")

        self.treeviwetable["show"]="headings"
        self.treeviwetable.column("nic",width=70)
        self.treeviwetable.column("membername",width=150)
        self.treeviwetable.column("bookcode",width=100)
        self.treeviwetable.column("bookname",width=100)
        self.treeviwetable.column("receivedate",width=100)
        self.treeviwetable.column("status",width=70)
  

        self.treeviwetable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviwetable.yview)
        self.treeviwetable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()
   
    def send(self):
        # Email account credentials
        email_address = 'ishanrate@gmail.com'
        email_password = '01086891ishan'

        # Contacts to send the email to (in this case, just one contact from self.var_email)
        contacts = [self.var_email.get()]

        # Create the email content
        msg = EmailMessage()
        msg['From'] = email_address
        msg['Subject'] = "Reminder: Book Return Due"
        msg.set_content("""
        Dear Member,
    
        This is a friendly reminder that your borrowed book is due for return. 
    Please ensure you return it by the specified date to avoid any late fees.
    
        Thank you for your attention.

        Regards,
        Library Management
    """)

       # Send the email to each contact in the reminder list
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)

                for contact in contacts:
                    msg['To'] = contact
                    smtp.send_message(msg)
                    print(f"Email sent to {contact}")

            messagebox.showinfo("Success", "Reminder emails sent successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}", parent=self.root)


  
    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost",user="root",password="#@19is16Pro",database="studentdata")
        cur=sqlcon.cursor()
        today=datetime.date.today()
        cur.execute("SELECT nic,membername,bookcode,bookname,receivedate,status FROM bookissue WHERE status ='issued' AND receivedate < %s",(today,))
        result=cur.fetchall()

        self.treeviwetable.delete(*self.treeviwetable.get_children())
        for row in result:
            self.treeviwetable.insert("",END,values=row)

        sqlcon.close()
    
    def getdata(self,ev):
        viweinfo=self.treeviwetable.focus()
        learnerdata=(self.treeviwetable.item(viweinfo))
        row=learnerdata['values']

        self.var_nic.set(row[0])
        self.var_name.set(row[1])
        self.var_code.set(row[2])
        self.var_bookname.set(row[3])
        self.var_receivedate.set(row[4])
        self.var_status.set(row[5])   

  
    
                    
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
    obj=reminderclass(root)
    root.mainloop()    