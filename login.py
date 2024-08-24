from tkinter import *
from tkinter import messagebox
import dashboard

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        # Username Label and Entry
        self.lbl_username = Label(self.root, text="Username:", font=("Arial", 14))
        self.lbl_username.pack(pady=10)
        self.entry_username = Entry(self.root, font=("Arial", 14))
        self.entry_username.pack(pady=10)

        # Password Label and Entry
        self.lbl_password = Label(self.root, text="Password:", font=("Arial", 14))
        self.lbl_password.pack(pady=10)
        self.entry_password = Entry(self.root, show="*", font=("Arial", 14))
        self.entry_password.pack(pady=10)

        # Login Button
        self.btn_login = Button(self.root, text="Login", command=self.login, font=("Arial", 14))
        self.btn_login.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simple authentication logic (Replace with your actual authentication)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_dashboard(self):
        self.root.destroy()  # Close the login window
        dashboard.run_dashboard()  # Call the dashboard's run_dashboard function

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
