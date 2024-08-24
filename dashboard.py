from tkinter import *
from PIL import Image, ImageTk
from addbook import addbookclass
from member import membersclass
from issuebook import issuebookclass
from returnbook import returnbookclass
from reminder import reminderclass




class dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1000x600+80+80")
        self.root.config(bg="gray")
        self.root.resizable(False, False)

        title=Label(self.root,text="Library Management System",font=("times new roman",30,"bold"),bg="black",fg="white",pady=10,padx=10)
        title.place(x=0,y=0,relwidth=1)

        #Buttons-----------------

        btn_1=Button(self.root,text="Add Book",command=self.addbook,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_1.place(x=50,y=150,width=200,height=40)
        btn_2=Button(self.root,text="Members",command=self.member,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_2.place(x=50,y=200,width=200,height=40)
        btn_3=Button(self.root,text="Issue Book",command=self.issuebook,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_3.place(x=50,y=250,width=200,height=40)
        btn_4=Button(self.root,text="Return Book",command=self.returnbook,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_4.place(x=50,y=300,width=200,height=40)
        btn_5=Button(self.root,text="Reminder",command=self.reminder,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_5.place(x=50,y=350,width=200,height=40)
        btn_6=Button(self.root,text="Inquiry",font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_6.place(x=50,y=400,width=200,height=40)
        btn_7=Button(self.root,text="Exit",command=self.exit,font=("times new roman",20,"bold"),bg="black",fg="lightgray",cursor='hand2')
        btn_7.place(x=50,y=450,width=200,height=40)



    def addbook(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=addbookclass(self.new_win)

    def member(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=membersclass(self.new_win) 

    def issuebook(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=issuebookclass(self.new_win)

    def returnbook(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=returnbookclass(self.new_win)
    def reminder(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reminderclass(self.new_win)
    
    def exit(self):
        self.root.destroy()


def run_dashboard():
    root = Tk()
    obj = dashboard(root)
    root.mainloop()

# If this file is executed directly, run the dashboard
if __name__ == "__main__":
    run_dashboard()


